# Python Day 4: Strings
# Indexing, Slicing, and String Methods
# ==============================
# STRING INDEXING
# ==============================
name = "Bisma"
# Positive indexing starts from 0
print(name[0])
# Negative indexing starts from -1 at the end
print(name[-1])
# ==============================
# STRING SLICING
# ==============================
# Starts at index 0 and stops before index 4
print(name[0:4]) 
# Starts at index 0 and stops before index 3
print(name[ :3]) 
# Starts at index 1 and goes to the end
print(name[1:])
# Returns the complete string
print(name[:])
# Negative indexing and slicing
text="Artificial Intelligence"
print(text[-12:-1]) 
# ==============================
# STRIP()
# ==============================
word="Hello     World"
print(word.strip())
# Removes leading and trailing whitespace
a="    bisma   "
print(a.strip())
# ==============================
# STRING CASE METHODS
# ==============================
sentence="Python Programming"
# Converts all characters to uppercase
print(sentence.upper()) 
# Converts all characters to lowercase
print(sentence.lower()) 
# Capitalizes the first character
print(sentence.capitalize())
# Capitalizes the first character of each word
print(sentence.title())
# ==============================
# REPLACE()
# ==============================
# Replaces "Python" with "Java"
print(sentence.replace("Python", "Java"))
# ==============================
# SPLIT()
# ==============================
# Splits the string into a list of words
print(sentence.split()) 
# Splits the string using "o" as the delimiter
print(sentence.split("o"))
# Splits the string using space as the delimiter 
print(sentence.split(" "))
# ==============================
# FIND()
# ==============================
lang = "Python"
print(lang.find("t"))
model = "Artificial Intelligence"
print(model.find("Intelligence"))
# Returns -1 if the text is not found
print(lang.find("java"))
# ==============================
# COUNT()
# ==============================
# count() tells us how many times
# a character or word appears in a string.
text = "banana"
print(text.count("a"))
# Returns 0 if the text is not found
print(text.count("apple"))
# count() is case-sensitive
# ==============================
# PRACTICE WITH USER INPUT
# ==============================
name = input("Enter your full name: ")
# Splits the full name into a list of words
words = name.split()
print(words)
# Splitting using a custom delimiter
text = "Python-AI-ML"
print(text.split("-"))
# Accessing an item from the resulting list
text = "one two three four"
result = text.split()
print(result[2])


