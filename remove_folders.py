import os
import shutil

script_directory = os.path.dirname(os.path.abspath(__file__))
directory_path = script_directory

# Get a list of subdirectories in the specified directory
subdirectories = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]

# Iterate through the subdirectories
for folder in subdirectories:
    if folder.isdigit() and folder != "1":
        folder_path = os.path.join(directory_path, folder)
        print(f"Removing folder: {folder_path}")
        shutil.rmtree(folder_path)

print("Done")