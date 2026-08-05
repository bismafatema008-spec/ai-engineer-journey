# Python Day 9: Modules

# A module is simply a Python file containing useful code
# such as functions, variables, or classes.
# We can import a module when we need to use its code.

# 1. Importing a Module
import math

print(math.sqrt(25))
# Without importing the math module, we cannot use math.sqrt().

# 2. Importing a Specific Function from a Module
from math import sqrt

print(sqrt(16))

# 3. Using an Alias
import math as m

print(m.pi)

# 4. Random Module
import random

# randint() returns a random integer between the given numbers.
print(random.randint(1, 10))

# 5. Using Another Function from the Math Module
print(m.factorial(4))

# 6. Importing Our Own Custom Module
import calculator

print(calculator.add(10, 20))
print(calculator.multiply(2, 4))