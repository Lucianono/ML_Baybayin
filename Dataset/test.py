import os
import shutil

# Get the directory where this script is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Loop through all files in the current directory
for filename in os.listdir(current_folder):
    # Skip the script file itself
    if filename == os.path.basename(__file__):
        continue

    file_path = os.path.join(current_folder, filename)
    if not os.path.isfile(file_path):
        continue  # Skip subdirectories or non-files

    # Split at the first period to get the prefix (e.g., 'xx' from 'xx.image1.jpg')
    prefix = filename.split('.')[0]

    # Create target folder if it doesn't exist
    target_folder = os.path.join(current_folder, prefix)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Move the file
    shutil.move(file_path, os.path.join(target_folder, filename))

print("Done organizing images.")
