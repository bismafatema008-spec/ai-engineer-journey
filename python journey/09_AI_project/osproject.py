# AI Project: File and Folder Manager
import os
# 1. Create AI_Projects Folder
if not os.path.exists("AI_Projects"):
    os.mkdir("AI_Projects")
    print("Folder created!")
else:
    print("Folder already existed!")
# 2. Create a File Inside the Folder
file_path = os.path.join("AI_Projects", "project_notes.txt")

if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write(
            "My AI Engineering journey has started!\n"
            "I am learning Python every day.")
    print("File created and content added!")
else:
    print("File already existed!")
# 3. Read the File
with open(file_path, "r") as file:
    content = file.read()
    print(content)
# 4. Rename the File
new_file_path = os.path.join(
    "AI_Projects",
    "Python_AI_Notes.txt")

if os.path.exists(file_path):
    os.rename(file_path, new_file_path)
    print("File renamed!")
else:
    print("File not found!")
# 5. Verify the Renamed File
if os.path.exists(new_file_path):
    print("File successfully renamed and verified!")
else:
    print("File verification failed!")