import tkinter as tk
from tkinter import scrolledtext, messagebox, StringVar, OptionMenu
import threading
import os
from groq import Groq

# Initialize Groq API client
client = Groq(
    api_key='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',  # Replace with your own API key
)

# Available models
AVAILABLE_MODELS = ["llama3-8b-8192", "groq-large-12b", "gpt-neox-20b"]  # Add more as needed

# Store conversation messages for multi-turn conversations
conversation_history = []

# Function to save chat history to a text file
def save_chat_history(chat_text):
    with open("chat_history.txt", "a") as file:
        file.write('\n')
        file.write(chat_text + " \n")

# Function to get chat completion from Groq API
def get_ai_response(user_input, selected_model):
    try:
        # Add the user's message to the conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Call Groq API with the full conversation history
        chat_completion = client.chat.completions.create(
            messages=conversation_history,
            model=selected_model,
        )

        # Add AI response to the conversation history
        ai_message = chat_completion.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": ai_message})

        return ai_message
    except Exception as e:
        return f"Error: {e}"

# Function to handle sending user input and updating the chat history
def send_message():
    user_input = input_box.get()  # Get user input from the entry box
    if user_input.strip() == "":
        return  # Do nothing if the input is empty

    # Display user's message in the chat window
    chat_history.configure(state='normal')
    chat_history.insert(tk.END, f"You: {user_input}\n")
    chat_history.configure(state='disabled')
    chat_history.yview(tk.END)  # Auto scroll to the bottom

    # Save user's message to chat history file
    save_chat_history(f"You: {user_input}")

    # Clear the input box after sending
    input_box.delete(0, tk.END)

    # Run the API call in a separate thread to keep the UI responsive
    threading.Thread(target=handle_response, args=(user_input, model_var.get())).start()

# Function to get AI response and update the chat history
def handle_response(user_input, selected_model):
    ai_response = get_ai_response(user_input, selected_model)

    # Update chat history with the AI response
    chat_history.configure(state='normal')
    chat_history.insert(tk.END, f"AI: {ai_response}\n")
    chat_history.configure(state='disabled')
    chat_history.yview(tk.END)  # Auto scroll to the bottom

    # Save AI's response to chat history file
    save_chat_history(f"AI: {ai_response}")

# Create the main application window
root = tk.Tk()
root.title("Groq AI Chat")

# Set window size and make it not resizable
root.geometry("750x500")
root.resizable(False, False)

# Chat history (scrollable text widget)
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=20)
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input box
input_box = tk.Entry(root, width=80)
input_box.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X, expand=True)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

# AI Model Selection Dropdown
model_var = StringVar(root)
model_var.set(AVAILABLE_MODELS[0])  # Set the default model

model_menu = OptionMenu(root, model_var, *AVAILABLE_MODELS)
model_menu.pack(padx=10, pady=10)

# Function to handle the Enter key press
def on_enter_key(event):
    send_message()

# Bind Enter key to send message
root.bind('<Return>', on_enter_key)

# Start the Tkinter event loop
root.mainloop()