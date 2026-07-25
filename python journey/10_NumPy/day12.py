# ==============================
# Mathematical Operator!
# ==============================
import numpy as np
arr =np.array([10,20,30])

print (arr + 5) #addition
print (arr - 2) #substraction
print (arr * 3) #multiplication
print (arr / 2) #division
print (arr ** 2) #square

# ==============================
# Agreegesion function!
# ==============================
arr =np.array([10,20,30])

print (np.sum(arr))
print (np.mean(arr))
print (np.max(arr))
print (np.min(arr))
print (np.std(arr))
print (np.var(arr))

# ==============================
# Indexing and SLicing!
# ==============================
array = np.array([10,20,30,40,50])
#indexing! 
#numpy follows zero based indexing
print (array[0])
print (array[2])
print (array[-1])

#Slicing!
print (array[1:4])
print (array[:4])
print (array[1:])
print (array[:])

print (array[::2])
print (array[::3])

print (array[0:4:2])

# ==============================
# Reshaping & Manuplating Arrays!
# ==============================
#1.Reshaping array!
#1D to Multiple dimensional
ar =np.array([1,2,3,4,5,6])
reshaped_ar = ar.reshape(2,3)
print (reshaped_ar)

#2.Flatenning array!
#Multiple dimension to 1D
arra_2d =np.array(
    [
     [1,2,3],
      [4,5,6]
    ]
)
print (arra_2d.ravel()) #usually returns a view when possible, 
#so changes to the result may affect the original array.
print (arra_2d.flatten()) #always returns a copy, so changes to the result do not affect the original array.

# ==============================
# Advanced NumPy!
# ==============================

#1.Insert()
arr = np.array([10,20,30,40,50])
print(arr)
new_arr =np.insert(arr, 2,100)
print (new_arr)

arra_2d =np.array(
    [
     [1,2],
      [3,4]
    ]
)
print (arra_2d)

#insert a new row at index 1
new_2d =np.insert(arra_2d, 1, [5,6], axis=0)
print(new_2d)
 #axis 0 work row wise
 #axis 1 works column wise
new_2d =np.insert(arra_2d, 1, [5,6], axis=1)
print(new_2d)

#2.Append()
arr = np.array([10,20,30])
new_arr = np.append(arr, [40,50,60])
print (new_arr)

#3concatenate()
arr1 = np.array([1,2,3])
arr2 = np.array([3,4,5])

new_array = np.concatenate((arr1, arr2))
print (new_array)

#4.delete()
arr = np.array([10,20,30,40,50])
print (arr)
new_arr =np.delete(arr, 0)
print (new_arr)

arra_2d =np.array(
    [
     [1,2],
      [3,4],
        [5,6]

    ]
)
print (arra_2d)
new_2d =np.delete(arra_2d, 0, axis=0)
print (new_2d)
new2_3d = np.delete(arra_2d, 1, axis=1)
print (new2_3d)
new2_3d = np.delete(arra_2d, 0, axis=1)
print (new2_3d)

