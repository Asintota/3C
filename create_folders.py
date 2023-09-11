import os
import shutil
import openpyxl

# Specify the path to your Excel file
file_path = 'C:\Users\pablo\OneDrive\Github\3C\actitud.xlsx'

# Load the workbook
workbook = openpyxl.load_workbook(file_path)

# Select the desired worksheet (for example, the first sheet)
worksheet = workbook.active

# Count the number of rows in the worksheet
num_rows = worksheet.max_row

# Print the number of rows
print(f'Total number of rows: {num_rows}')

# Close the workbook (optional, but recommended)
workbook.close()



source_folder = r'C:\Users\pablo\OneDrive\Github\3C\1'
destination_base = r'C:\Users\pablo\OneDrive\Github\3C'
num_copies = num_rows-1  # Change this to the number of copies you want to make

for i in range(2, num_copies + 1):
    # Create a new folder name based on the iteration index
    new_folder_name = f'copy_{i}'
    
    # Create the full path for the destination folder
    destination_folder = os.path.join(destination_base, new_folder_name)
    
    # Copy the source folder to the destination
    shutil.copytree(source_folder, destination_folder)
    
    # Rename a file within the copied folder (e.g., rename 'file.txt' to 'new_file.txt')
    file_to_rename = os.path.join(destination_folder, '1.html')
    new_file_name = f'new_file_{i}.html'
    os.rename(file_to_rename, os.path.join(destination_folder, new_file_name))
    
    print(f'Copy {i} completed.')

