# Python Day 7: Lists
# A list is a data type used to store multiple values in a single variable.
# Creating a List
shopping = ["Milk", "Bread", "Eggs", "Butter"]
print(shopping)
# List Indexing
fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])
# Finding the Length of a List
names = ["Ali", "Sara", "Ahmed"]
print(len(names))
# List Slicing
cities = ["Mumbai", "Delhi", "Pune", "Nagpur"]
print(cities[1:4])
# List Slicing with Step
letters = ["A", "B", "C", "D", "E", "F"]
print(letters[::2])
# List Slicing with Negative Index
print(letters[1:-1])
# ==============================
# LIST METHODS
# ==============================

# 1. append() = Adds one item at the end of the list.
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)

# 2. extend() = Adds multiple items from another list.
a = [1, 2, 3]
a.extend([4, 5, 6, 7])
print(a)

# 3. insert() = Adds an item at a specific index.
colors = ["red", "green", "purple"]
colors.insert(2, "blue")
print(colors)

# 4. remove() = Removes the first occurrence of a value.
num = [10, 20, 30, 40, 50]
num.remove(20)
print(num)

# 5. pop() = Removes an item by index and returns the removed value.
# pop() with an index
nums = [10, 20, 30]
nums.pop(1)
print(nums)
# pop() without an index removes the last item.
nums = [10, 20, 30]
nums.pop()
print(nums)

# Storing the removed value
num = [10, 20, 30]
x = num.pop(1)
print(x)
print(num)

# 6. clear() = Removes all items from the list.
a = [1, 2, 3]
a.clear()
print(a)

# 7. index() = Returns the index of a value.
fruits = ["apple", "banana", "mango"]
print(fruits.index("banana"))

# 8. count() = Counts how many times a value occurs.
b = [1, 2, 2, 2, 5, 3, 2, 4, 2]
print(b.count(2))

# 9. sort() = Sorts the original list in ascending order.
c = [2, 6, 4, 1, 3]
c.sort()
print(c)

# Sorting in descending order
d = [2, 6, 4, 1, 3]
d.sort(reverse=True)
print(d)

# 10. reverse() = Reverses the order of the list.
lis = [1, 2, 3, 4]
lis.reverse()
print(lis)

# 11. copy() = Creates a copy of the list.
x = [1, 2, 3, 4, 5]
new_x = x.copy()
print(new_x)
# pop() without an index removes the last item.
z = ["100", "200", "300"]
z.pop()
print(z)
# Difference between pop() and remove()
# Use pop() when you know the position (index) of the item
# and/or need the removed value.
#
# Use remove() when you know the value you want to delete.

# 12. sorted() = Returns a new sorted list without changing the original list.
numbers = [4, 2, 8, 1]
new_list = sorted(numbers)
print(new_list)
print(numbers)