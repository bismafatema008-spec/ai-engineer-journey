# Python Day 10: DateTime, OS Module & File Handling
# ==========================================
# 1. DATETIME MODULE
# ==========================================

import datetime

# Getting the Current Date and Time
print("Current Date and Time:")
print(datetime.datetime.now())

# Getting Today's Date
print("Today's Date:")
print(datetime.date.today())


# Formatting Date and Time
now = datetime.datetime.now()

print("Today's Date:", now.strftime("%d-%m-%Y"))
print("Today's Time:", now.strftime("%H-%M-%S"))


# ==========================================
# 2. OS MODULE
# ==========================================

# The OS module allows Python to interact with
# the operating system, files, and folders.

import os


# Getting the Current Working Directory
print("Current Folder:")
print(os.getcwd())


# Listing Files and Folders
print("List of Files and Folders:")
print(os.listdir())


# ==========================================
# 3. CREATING A FOLDER
# ==========================================

if not os.path.exists("Practice"):
    os.mkdir("Practice")
    print("Practice folder created successfully!")
else:
    print("Practice folder already existed!")


# ==========================================
# 4. CREATING, RENAMING & DELETING A FOLDER
# ==========================================

if not os.path.exists("AI_Projects"):
    os.mkdir("AI_Projects")
    print("AI_Projects folder created!")
else:
    print("AI_Projects folder already existed!")


# Renaming the folder
if os.path.exists("AI_Projects"):
    os.rename("AI_Projects", "My_AI_Projects")
    print("Folder renamed successfully!")


# Removing the folder
if os.path.exists("My_AI_Projects"):
    os.rmdir("My_AI_Projects")
    print("Folder removed successfully!")


# ==========================================
# 5. CREATING & WRITING TO A FILE
# ==========================================

if not os.path.exists("note.txt"):
    with open("note.txt", "w") as file:
        file.write("I am learning Python!")

    print("Content added!")
    print("File created!")
else:
    print("File already exists!")


# ==========================================
# 6. READING A FILE
# ==========================================

with open("note.txt", "r") as file:
    content = file.read()
    print(content)


# ==========================================
# 7. APPENDING CONTENT TO A FILE
# ==========================================

with open("note.txt", "a") as file:
    file.write("\nPython is fun to learn!")


# Reading the updated file
with open("note.txt", "r") as file:
    content = file.read()
    print(content)


# ==========================================
# 8. DELETING A FILE
# ==========================================

if os.path.exists("note.txt"):
    os.remove("note.txt")
    print("File deleted!")
else:
    print("File not found!")


# ==========================================
# 9. RENAMING A FILE
# ==========================================

if os.path.exists("note.txt"):
    os.rename("note.txt", "python_notes.txt")
    print("File renamed!")
else:
    print("File not found!")


# ==========================================
# 10. CHECKING IF A FILE EXISTS
# ==========================================

print(os.path.exists("note.txt"))