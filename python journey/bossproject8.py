import os
if not os.path.exists("AI_Projects"):
    os.mkdir("AI_Projects")
    print ("Folder created!")
else:
    print ("folder already existed!")
file_path =os.path.join('AI_Projects\\python_notes.txt')
if not os.path.exists(file_path):
    with open (file_path,"w") as file:
       file.write("I am becoming an AI Engineer! \n Python is my foundation.")
       print ("file created content added!")
else:
    print ("file already existed!")
with open(file_path, "r") as file:
     cont = file.read() 
     print (cont) 
new_file_path = os.path.join("AI_Projects", "AI_Engineer_Notes.txt")
if os.path.exists(file_path):
    os.rename(file_path, new_file_path)
    print("file renames!")
else:
    print ("file not found!")
        
