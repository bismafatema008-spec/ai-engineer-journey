#TYPE CASTING
age="20"
print(type(age))
num="25" 
print(float(num))
#OPERATORS
"""1. Arithmetic Operators ➕➖✖️➗

Used for calculations.
| Operator | Meaning             | Example   | Output |
| -------- | ------------------- | --------- | ------ |
| `+`      | Addition            | `10 + 5`  | `15`   |
| `-`      | Subtraction         | `10 - 5`  | `5`    |
| `*`      | Multiplication      | `10 * 5`  | `50`   |
| `/`      | Division            | `10 / 5`  | `2.0`  |
| `//`     | Floor Division      | `10 // 3` | `3`    |
| `%`      | Modulus (remainder) | `10 % 3`  | `1`    |
| `**`     | Power               | `2 ** 3`  | `8`    |
"""
#/ → Performs normal division and returns the answer with decimals (if any).
# Example: 15 / 2 = 7.5
# // → Performs floor division and removes the decimal part (rounds down toward negative infinity for positive numbers).
# Example: 15 // 2 = 7
"""= means assign a value.

== means compare two values."""
#COMPARION OPERATORS
"""== (equal to)
!= (not equal to)"""
#LOGICAL OPERATORS
"""and (returns True if both statements are true)
or (returns True if one of the statements is true)
not (returns True if the statement is false)"""
#PROJECT
name=input("Enter your name: ")
print(str(name))
age=int(input("Enter your age: "))
print(age)

print(age+5)
print("Hello", name)
print("your age is", age)
print("your age after 5 years will be", age+5)
x = 25
y = 4
print (x//y) #floor divisionb

a =18
b =5
print (a//b)
print(25 // 4)
print(17 // 2 + 3)
print((15 + 5) // 4)
num = 125
hundreds = num // 100
print(hundreds)