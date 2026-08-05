# ==============================
# Stacking
# ==============================

import numpy as np

arr1 =np.array([1,2,3])
arr2 =np.array([4,5,6])

print (np.vstack((arr1, arr2)))   #vertically stacking-row wise
print (np.hstack((arr1, arr2)))   #horizontally stacking- column wise

# ==============================
# Spliting
# ==============================

arr =np.array([10,20,30,40,50,60])

print (np.split(arr, 2)) #split() in two parts
print (np.hsplit (arr, 3)) #horixontal split
#print (np.vsplit (arr, 2)) #dont work for 1d array!

# ==============================
# Broadcasting
# ==============================

arr =np.array([1,2,3,4])
result =arr*5
print (result)

A =np.array(
             [[10,20,30],
           [40,50,60] 
           ]
           )
B =np.array([1,2,3])
print (A+B)

print ("incompatible shape error")

"""X =np.array(
             [[10,20,30],
           [40,50,60] 
           ]
           )
Y =np.array([1,2])
print (X+Y)"""

# ==============================
# Vectorisation
# ==============================

arr1 =np.array([1,2,3])
arr2 =np.array([4,5,6])
print(arr1+arr2)

a =np.array([[1,2,3],
             [4,5,6]
             ]
            )
            
b =np.array([[10],
             [20]
             ]
            )
print(a+b)

#operations 
arr =np.array([10,20,30,40])
multi =arr*2
print(multi)

# ==============================
# Finding missing values!
# ==============================

arr = np.array([10, 20, np.nan, 40, np.nan, 60])

print(arr)

print(np.isnan(arr))

print(np.sum(np.isnan(arr))) 

print (np.where(np.isnan(arr)))

print (np.nan_to_num(arr))

print (np.nan_to_num(arr,nan=100))

#infinite
arr =np.array([1,2,np.inf,4,-np.inf,5])

print(np.isinf(arr))

cleaned_ar =np.nan_to_num(arr, posinf=1000, neginf=-1000)
print (cleaned_ar)
       



