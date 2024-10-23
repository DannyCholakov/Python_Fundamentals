class Email:
    def __init__(self, sender, receiver, content):
        # Initialize the sender, receiver, and content for the email
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False  # Email is not sent initially

    def send(self):
        # This method sets the is_sent flag to True when the email is sent
        self.is_sent = True

    def get_info(self):
        # This method returns a string with the email details and sent status
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


# List to store the emails
emails = []

# Reading email input
line = input()
while line != "Stop":
    tokens = line.split(" ")
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]

    # Create an Email object and store it in the list
    email = Email(sender, receiver, content)
    emails.append(email)

    line = input()

# Reading indices of emails to be sent
send_emails = list(map(lambda x: int(x), input().split(", ")))

# Marking the specified emails as sent
for x in send_emails:
    emails[x].send()

# Printing the info for all emails
for email in emails:
    print(email.get_info())