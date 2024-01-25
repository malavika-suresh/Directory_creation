import os


text_file = r"C:\Users\malavika\Desktop\file.txt"

# Read directory names from the text file
with open(text_file, 'r') as file:
    directory_names = file.read().splitlines()

base_directory = 'plug'

# Create folders one by one
for directory_name in directory_names:
    folder_path = os.path.join(base_directory, directory_name)


    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{directory_name}' created at '{folder_path}'")
    else:
        print(f"Folder '{directory_name}' already exists at '{folder_path}'")
