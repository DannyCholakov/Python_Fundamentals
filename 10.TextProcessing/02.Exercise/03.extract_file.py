def extract_file_details(file_path):
    file_full_name = file_path.split("\\")[-1]

    file_name, file_extension = file_full_name.split(".")

    print(f"File name: {file_name}")
    print(f"File extension: {file_extension}")

file_path = input()

extract_file_details(file_path)
