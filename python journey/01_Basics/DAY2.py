#TYPE CASTING
age="20"
print(type(age))
num="25" 
print(float(num))  #converting a string to float
#OPERATORS
#1. Arithmetic Operators ➕➖✖️➗

#Used for calculations.
#| Operator | Meaning             | Example   | Output |
#|`+`      | Addition            | `10 + 5`  | `15`   |
#| `-`      | Subtraction         | `10 - 5`  | `5`    |
#| `*`      | Multiplication      | `10 * 5`  | `50`   |
#| `/`      | Division            | `10 / 5`  | `2.0`  |
#| `//`     | Floor Division      | `10 // 3` | `3`    |
#| `%`      | Modulus (remainder) | `10 % 3`  | `1`    |
#| `**`     | Power               | `2 ** 3`  | `8`    |
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(2 ** 3)
#/ → Performs normal division and returns the answer with decimals (if any).
# Example: 15 / 2 = 7.5
# // → Performs floor division and removes the decimal part (rounds down toward negative infinity for positive numbers).
# Example: 15 // 2 = 7
# = means assign a value.

# == means compare two values.
a = 10
b = 10
print(a == b)
#COMPARION OPERATORS
# == (equal to)
# != (not equal to)
print(10 == 10)
print(10 != 5)
print(10 > 5)
print(10 < 5)
print(10 >= 10)
print(10 <= 10)
#LOGICAL OPERATORS
#and (returns True if both statements are true)
# or (returns True if one of the statements is true)
# not (returns True if the statement is false)
print(10 > 5 and 20 > 10)
print(10 > 5 or 20 < 10)
print(not (10 > 5))

#PROJECT: AGE CALCULATOR
name=input("Enter your name: ")
print(name)
age=int(input("Enter your age: "))
print(age)
print(age+5)
print("Hello", name)
print("your age is", age)
print("your age after 5 years will be", age+5)
#some examples
x = 25
y = 4
print (x//y) #FLOOR DIVISION
a =18
b =5
print (a//b)
print(25 // 4)
print(17 // 2 + 3)
print((15 + 5) // 4)
num = 125
hundreds = num // 100
print(hundreds)