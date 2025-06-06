import numpy as np

# ------------------------------
# 1. Creating Arrays from Lists
# ------------------------------

# 1D array

arr1 = np.array([1,2,3]) # Static declaration using a list. Dynamic declaration can be done using loops just like Cpp or C

# 2D array

arr2 = np.array([[1,2],[3,4]]) #list of lists

# 3D array

arr3= np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) #list of lists of lists xD

# Mixed types will be promoted (e.g., int + float => float)
# so array: 1.0, 2.5, 3.5 | you can use dtype=(e.g ==> float,int,np.int32 ,etc) to change data-type
arr3 = np.array([1, 2.5, 3])
a = np.array([2, 3, 4], dtype=np.uint32)
b = np.array([5, 6, 7], dtype=np.uint32)
c_unsigned32 = a - b


'''
The 1D array creation functions e.g. numpy.linspace and numpy.arange generally need at least two inputs, start and stop:

import numpy as np

np.arange(10)                   --> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

np.arange(2, 10, dtype=float)   --> array([2., 3., 4., 5., 6., 7., 8., 9.])

np.arange(2, 3, 0.1)            --> array([2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])

np.linspace(1., 4., 6)          --> array([1. ,  1.6,  2.2,  2.8,  3.4,  4. ])
'''


# 2. Predefined 2D Arrays (Zeros, Ones, Empty)
# ------------------------------

# Array of zeros
zeros = np.zeros((2, 3))  # 2 rows, 3 columns

# Array of ones
ones = np.ones((3, 2))    # 3x2 matrix filled with 1s

# Empty array (values uninitialized — depends on memory garbage)
empty = np.empty((2, 2))

# Full array with a specific value
full = np.full((2, 2), 9)


# ------------------------------
# 3. Identity & Diagonal Matrices
# ------------------------------

# Identity matrix
identity = np.eye(3)  # 3x3 identity matrix

# Diagonal matrix
diag = np.diag([1, 2, 3])  # Diagonal elements only




# ------------------------------
# 4. Random Arrays
# ------------------------------

# Random floats in [0.0, 1.0)
rand = np.random.rand(2, 3)  # Uniform distribution

# Random integers between 10 and 20
randint = np.random.randint(10, 20, size=(3, 2))

# Random samples from standard normal distribution (mean=0, std=1)
normal = np.random.randn(4)

# Random choice from a list
choice = np.random.choice([1, 2, 3, 4], size=(2, 2))

# ------------------------------
# 6. Reshaping and Resizing
# ------------------------------

arr = np.arange(12)           # [0..11]
reshaped = arr.reshape(3, 4)  # Shape into 3 rows x 4 columns
'''
[[ 0  1  2  3] 
 [ 4  5  6  7] 
 [ 8  9 10 11]]
'''

# Resize will modify the array in-place and change size
resized = np.resize(arr, (2, 8))
'''
[[ 0  1  2  3  4  5  6  7] 
 [ 8  9 10 11  0  1  2  3]]
'''
# ------------------------------
# 7. Copying Arrays
# ------------------------------

# Shallow copy (view)
view = arr.view()

# Deep copy (independent)
copy = arr.copy()

# ------------------------------
# 8. Structured Arrays (Advanced)
# ------------------------------

# Useful for labeled datasets like tables
dtype = [('name', 'U10'), ('age', 'i4'), ('weight', 'f4')]
structured = np.array([('Alice', 25, 55.5), ('Bob', 30, 67.3)], dtype=dtype)

# Accessing a field
names = structured['name']

# ------------------------------
# 9. Multidimensional with np.ndindex
# ------------------------------

shape = (2, 2, 2)
multi_dim = np.zeros(shape)

# Assigning values using multidimensional indexing
for index in np.ndindex(shape):
    multi_dim[index] = sum(index)

# ------------------------------
# 10. Using fromfunction (generate values based on index)
# ------------------------------

def func(i, j):
    return i + j

grid = np.fromfunction(func, (3, 3), dtype=int)
# Output:
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]

