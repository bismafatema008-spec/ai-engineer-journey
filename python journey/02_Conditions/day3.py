# Python Day 3: Conditional Statements
# if, elif, else
# ==============================
# VOTING ELIGIBILITY
# ==============================
age=18
if age>=18:
    print("Your are eligible to vote")
else:
    print("You are not eligible to vote")

# ==============================
# MARKS AND GRADE CALCULATOR
# ==============================

marks=int(input("Enter your marks= "))
if marks < 0 or marks > 100:
    print("Invalid marks") 
elif marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Invalid marks")

