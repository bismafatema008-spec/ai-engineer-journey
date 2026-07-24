# Python Day 8: Functions
# A function is a block of reusable code that performs a specific task.
# 1. Creating and Calling a Function
def name():
    print("Bisma")
name()

# 2. Parameters and Arguments
def greet(name):  # name is a parameter
    print("Hello!", name)
greet("Bisma")   # "Bisma" is an argument
greet("Ahmed")   # "Ahmed" is an argument
greet("Sara")    # "Sara" is an argument

# 3. Multiple Parameters
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student("Bisma", 20)

# 4. Function with Multiple Parameters and Operations
def add(a, b):
    print(a + b)
add(20, 30)
def subtract(a, b):
    print(a - b)
subtract(70, 30)


# 5. Function with Parameters
def intro(name, city):
    print("Name:", name)
    print("City:", city)
intro("Bisma", "Parbhani")

# 6. return Statement
def add_numbers(a, b):
    return a + b
result = add_numbers(10, 20)
print(result)  # The returned value can be stored in a variable.

# 7. Returning a Calculated Value
def square(num):
    return num * num
answer = square(5)
print(answer)

# 8. print() vs return
def square_print(num):
    print(num * num)
square_print(5)
square_print(4)

# print() displays the result but does not return it for later use.
def square_return(num):
    return num * num
result = square_return(5)
print(result)
# return sends the value back to the caller and allows us to store and reuse it.

# 9. Returning True or False
def is_even(num):
    return num % 2 == 0
print(is_even(4))
print(is_even(7))

# 10. return Stops Function Execution
# As soon as Python sees return, the function stops immediately.
def test():
    print("A")
    return
    print("B")  # This line will never execute.
test()

# 11. Using Returned Values in Calculations
def add_values(a, b):
    return a + b
x = add_values(5, 10)
y = add_values(2, 3)
print(x)
print(y)
print(x + y)

# 12. Storing a Returned String
def student_result():
    print("Calculating result...")
    return "Grade A"
grade = student_result()
print(grade)

# 13. Function with print() and return
def welcome(name):
    print("Hello", name)
    return "Welcome"
message = welcome("Bisma")
print(message)