# main.py - sort files in a folder into subfolders by type or by date.
# Run it with:  python main.py

import os
import shutil
from datetime import datetime

# Folder name -> list of file extensions that belong in it
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt", ".rtf", ".md"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".m4a"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".json"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

# ---- Ask the user what to do ----
folder = input("Folder to organise (press Enter for current folder): ").strip()
if folder == "":
    folder = "."

if not os.path.isdir(folder):
    print("That folder does not exist.")
    exit()

mode = input("Sort by (1) type or (2) date? ").strip()
preview = input("Preview only, without moving files? (y/n): ").strip().lower()

# ---- Go through each file in the folder ----
count = 0
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    # Skip folders, hidden files, and this script
    if not os.path.isfile(file_path):
        continue
    if filename.startswith("."):
        continue
    if filename == "main.py":
        continue

    # Work out which subfolder this file belongs in
    if mode == "2":
        # By date: use the last-modified date, e.g. "2025-03"
        date = datetime.fromtimestamp(os.path.getmtime(file_path))
        subfolder = date.strftime("%Y-%m")
    else:
        # By type: look up the extension, e.g. "photo.JPG" -> ".jpg"
        extension = os.path.splitext(filename)[1].lower()
        subfolder = "Other"
        for folder_name in categories:
            if extension in categories[folder_name]:
                subfolder = folder_name

    target_folder = os.path.join(folder, subfolder)

    # If a file with this name already exists, add (1), (2), ... to the name
    name, extension = os.path.splitext(filename)
    new_name = filename
    number = 1
    while os.path.exists(os.path.join(target_folder, new_name)):
        new_name = name + " (" + str(number) + ")" + extension
        number = number + 1

    print(filename + "  ->  " + subfolder + "/" + new_name)

    if preview != "y":
        os.makedirs(target_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(target_folder, new_name))

    count = count + 1

if preview == "y":
    print("\nWould move " + str(count) + " file(s).")
else:
    print("\nMoved " + str(count) + " file(s).")
