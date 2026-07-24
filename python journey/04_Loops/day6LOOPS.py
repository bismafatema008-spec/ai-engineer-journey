# Python Day 6: Loops
# for loop, while loop, break, continue, pass, and nested loops
# ==============================
# INTRODUCTION TO LOOPS
# ==============================
# Loops allow us to repeat a block of code
# multiple times without writing it again and again.
# There are two main types of loops in Python:
# for loop - Used when you know how many times to repeat something.
# while loop - Used when you want to repeat something
# until a condition becomes false.
# ==============================
# FOR LOOP
# ==============================
for i in range(5):
    print("Hello")
# ==============================
# RANGE() FUNCTION
# ==============================

# range() generates a sequence of numbers.

# range(stop)
for i in range(5):
    print(i) 
# range(start, stop)
for i in range(2, 6):
    print(i)

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i) #start from 1 and goes up to 10 with a step of 2 STOP BEFORE 10 LIKE IN INDEXING
for i in range(1, 10, 3):
    print(i)
# ==============================
# WHILE LOOP
# ==============================

print("While LOOP")
i = 1
while i <= 5:
    print(i)
    i  +=1
# While loop with increment
print("While loop with increment")
i = 2
while i < 10:
    print(i)
    i += 3
# ==============================
# F-STRING
# ==============================
# f-strings allow us to insert variables
# directly inside a string.
name = "Alice"
age = 30
print(f"Hello, my name is {name} and I am {age} years old.")
# ==============================
# BREAK STATEMENT
# ==============================
# break stops the loop completely.
for i in range(1, 11):
    if i == 6:
        break
    print(i)
# ==============================
# CONTINUE STATEMENT
# ==============================
# continue skips the current iteration
# and moves to the next iteration.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Print only odd numbers
print("print only odd no")
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)
# ==============================
# PASS STATEMENT
# ==============================
# pass is used as a placeholder
# when we don't want to write code yet.
for i in range(5):
    pass
# ==============================
# LOOP THROUGH A LIST
# ==============================
colors=["red", "green", "blue"]
for color in colors:
    print(color)
# ==============================
# NESTED LOOPS
# ==============================
for i in range(3):
    for j in range(3):
        print(i,j)
for i in range(3):
    print(i)
    for j in range(2):
        print(j)

# print(i, j) prints both values
# in the same print() statement.
#
# Separate print(i) and print(j) statements
# print the values on separate lines.
# ==============================
# PRACTICE QUESTIONS
# ==============================

# Print numbers 1 to 10 using a for loop.

print(" numbers 1 to 10 using a for loop.")
for i in range(1,11):
    print(i)
# Print numbers 10 to 1 using a while loop.

print(" numbers 10 to 1 using a while loop.")
i=10
while(i>=1):
 print(i)
 i-=1
# Print numbers 10 to 1 using a while loop.
print(" even numbers from 2 to 20.")
i=2
while (i<=20):
 print(i)
 i+=2
# Print all odd numbers from 1 to 19.
print(" odd numbers from 1 to 19.")
i=1
while (i<=19):
 print(i)
 i+=2
# ==============================
# BOSS CHALLENGE
# ==============================
# Print the multiplication table of a number
num=int(input("Enter your number=" ))
i=1
while(i<=10):
  print(num,"x",i,"=",num*i)
  i+=1
  

