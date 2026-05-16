# File Organizer Script
# This script arranges downloaded files into folders by file type

import os
import shutil

# Path to Downloads folder
source_folder = r"C:\Users\DELL\Downloads"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Zip_Files": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"],
}

# Create folders if not exist
for folder_name in file_types.keys():
    folder_path = os.path.join(source_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Move files into folders
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        moved = False

        for folder_name, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(source_folder, folder_name, file))
                moved = True
                break
            print("Starting organizer...")
            print(f"Moved {file} to {folder_name}")

        if not moved:
            other_folder = os.path.join(source_folder, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file))

print("Files arranged successfully!")