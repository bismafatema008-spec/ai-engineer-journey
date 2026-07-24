import os
if not os.path.exists("AI_Projects"):
    os.mkdir("AI_Projects")
    print("AI_Projects folder created!")
else:
    print ("AI_Projects already exxisted!")
file_path = os.path.join("AI_Projects", "python_notes.txt")
if not os.path.exists(file_path):
    with open (file_path, "w") as file:
        file.write("I am learning Python and AI Engineering!")
        print("file created and content added!")
else:
    print("file already existed")
with open(file_path, "r") as file:
    content = file.read()
    print (content) 
