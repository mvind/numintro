# Numpy Notes
import numpy as np

a = np.array([1,2,3])
#rint(type(a)) # (3, )
#print(a.shape)
a[0] = 5

b = np.array([[1,2,3],[4,5,6]])
#print(b.shape)
#print(b[1,2])

# Matricer
# Lav en N x M nul matrice
a = np.zeros((2,2))

# Lav en N x M et tals matrice
a = np.ones((1,2))

# Lav en N x M konstant matrice
a = np.full((2,2,), 8)

# Lav en N x N identitets matrice
a = np.eye(2)

# Random entries N x M matrice
a = np.random.random((2,2))

# Extraction
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) # Shape = 3,4
# print(a) ->
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

b = a[:2,1:3] # De 2 første rækker og søljer fra 1-2.
# [[2 3]
#  [6 7]]

# Modifying a slice of data, will modify the orginal data aswell
a[0,0] # == 12

# Math
x = np.array([[1,2],[3,4]],dtype=np.float64)
y = np.array([[5,6],[7,8]],dtype=np.float64)

# adding to elementwise sum and same shamp as input
print(x+y)
print(np.add(x,y))

# Subtraction
x-y
np.subtract(x,y)

# elementwise multiplying / dividing
x * y
x / y
print(np.multiply(x,y))
print(np.divide(x,y))

# elementwise squareroot
np.sqrt(x)

# Vectors
v = np.array([9,10])
w = np.array([11,12])

# Inner product of two Vectors or matrices
print(v.dot(w))
print(np.dot(v,w))

x.dot(y)
np.dot(x,y)
