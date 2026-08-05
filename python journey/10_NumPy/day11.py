#NumPy array,type and  Properties
import numpy as np
print ("NumPy is ready!")
print (np.__version__)
# ==============================
# Numpy Array!
# ==============================
#NumPy array:is a data structure that stores multiple numerical values in single variable.
#especially for numerical data and efficient mathematical operations.
# ==============================
# 1D Array! =stores elements in single row or linear sequence
# ==============================
numbers = np.array([5, 10, 15, 20, 25, 30])
print (numbers)
#print 15 using inndexing
print (numbers[2])
#Print 25 usin indexing.
print(numbers[4])
# ==============================
# 2D Array!  stores element in a row and cloumns like a table or matrix.
# ==============================
matrix =np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
)
print (matrix)
#in 2D array both row and column have indexing.
#        Col 0  Col 1  Col 2
# Row 0  10     20     30
# Row 1  40     50     60
# Row 2  70     80     90
print (matrix[0,1])
#0 → Row index
#1 → Column index
# ==============================
# Array property Shape
# ==============================
print (matrix.shape)
print (numbers.shape) 
#with default values : for future use!
#for zero no
zeros_array =np.zeros(3)
print (zeros_array)  #output [0. 0. 0.]

print (zeros_array)
#for one no
ones_array =np.ones([2,3])
print (ones_array)
ones_array =np.ones([5])
print (ones_array)    #output [1. 1. 1. 1. 1.]
#Create an array filled with a specific value
filled_array =np.full(4,6)
print (filled_array)
filled_array =np.full([2,3],7)
print (filled_array)
# ==============================
# sequence of number!
# ==============================
#arrange (start,stop,step)
arr =np.arange(1,10,2)
print (arr)
# ==============================
# creating identity matrices!
# ==============================
#eye(size)
identity_matrix =np.eye(4)
print (identity_matrix)
# ==============================
# NumPy array properties!
# ==============================
#1.shape
arr_2d=np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print (arr_2d.shape)
#2.size
array_size =np.size([[10, 20,30],[40,50,60]])
print (array_size)

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr.size)
#3.ndim no of dimensions.
arr_1d =np.array([1,2,3])
arr_2d =np.array([
    [1,2,3],
    [4,5,6]
])
arr_3d =np.array(
    [
        [
            [1,2],
                [3,4],
                   [5,6],
                       [7,8]
        ]
            ]
                )
print (arr_1d.ndim) #output:1 means 1 dimension
print (arr_2d.ndim) #output:2 2 dimension
print (arr_3d.ndim) #output:3 3 dimension
#4.Datatype
arr =np.array([10,20,30.5,40])
print(arr.dtype)
#5.datatype interconversion.(astype)
arr =np.array([1.2,2.3,3.4])
int_arr =arr.astype(int) 
print(int_arr) #astype(int) decimal ko round nahi karta, decimal part ko remove karta hai.

