"""
NumPy is the fundamental package for scientific computing that provides a multidimensional 
array object, various derived objects (masked arrays and matrices), and an assortment of 
routines for fast operations on arrays, including mathematical, logical, shape manipulation, 
sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic 
statistical operations, random simulation and much more
    - np arrays have a fixed size at creation, changing the size of an ndarray will create 
      a new array and delete the original
    - The elements in a NumPy array are all required to be of the same data type, and thus will 
      be the same size in memory. The exception: one can have arrays of objects, thereby allowing 
      for arrays of different sized elements
    - Element-by-element operations are the 'default mode'
    - Fast because of vectorization and broadcasting

Vectorization (Abstraction?) describes the absence of any explicit looping, indexing, etc.
Broadcasting is the term used to describe the implicit element-by-element behaviour or operations
"""

import numpy as np

# np.array([]) Define array
a1D = np.array([1, 2, 3])
print('a1D: ', a1D)

print('\n')

a2D = np.array([[1, 2, 3], [4, 5, 6]])
print('a2D: \n', a2D)

print('\n')

a3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('a3D: \n', a3D)

print('\n')

# An 8-bit signed integer represents integers from -128 to 127, overflow when assigning integers
# outside the range
# np.array([], dtype = np.int8)
bit8 = np.array([127, 128, 129], dtype=np.int8)
print('bit8: ', bit8)

print('\n')

bit16 = np.array([127, 128, 129], dtype=np.int16)
print('bit16: ', bit16)

print('\n')

# Operations on two arrays of the same type return the same type
au32 = np.array([2, 3, 4], dtype = np.uint32)
bu32 = np.array([5, 6, 7], dtype = np.uint32)
cu32 = au32 - bu32

print('cu32:', cu32, cu32.dtype)

print('\n')

# Two different types will return a type that satifies all elements involved in computation
cu32 = au32 - bu32.astype(np.int32)
print('cu32:', cu32, cu32.dtype)

print('\n')

# 1D array creation functions np.arange() and np.linspace()

# np.linspace() will create arrays with a specified number of elements, and spaced equally 
# between the specified beginning and end values
print(np.linspace(1., 4., 6))

print('\n')

# np.arange(x) Creates arrays with regularly incrementing values
print(np.arange(10))
print(np.arange(2, 10, dtype=float))
print(np.arange(2, 3, 0.1))

print('\n')

# 2D array creation functions np.eye(), np.diag(), define np.vander define properties of special matrices 

# np.eye(n, m) defines a 2D identity matrix. The elements where i=j (row index and column index are equal)
# are 1 and the rest are 0
# In linear algebra a identity matrix of size n is the n x n square matrix with ones on the main diagonal and zeros else where
print(np.eye(4))
print(np.eye(3, 5))

print('\n')

# np.diag(v, k=0) can define either a square 2D array with given values along the diagonal or if 
# given a 2D array returns a 1D array that is only the diagonal elements
# k = Use k>0 for diagonals above the main diagonal, and k<0 below the main diagonal
print(np.diag([1, 2, 3, 4]))
print('\n')
print(np.diag([1, 2, 3, 4], 1))
print('\n')
print(np.diag([1, 2, 3, 4], -1))
print('\n')
a = np.array([[1, 2], [3, 4]])
print(a)
print('\n')
print(np.diag(a))

print('\n')
# nDarray creation functions

# np.zeros() will create an array filled with 0 values with the specified shape. default dtype=float64
print(np.zeros((2, 4)))
print('\n')
print(np.zeros((3, 3, 3)))
print('\n')

# np.ones()
print(np.ones((2, 4)))
print('\n')
print(np.ones((3, 3, 3)))
print('\n')

# np.indices() will create a set of arrays (stacked as a one-higher dimensioned array), one per 
# dimension with each representing variation in that dimentsion
print(np.indices((3, 3)))
print('\n')

# np.copy() if you want to create a new array rather than a view
a = np.array([1, 2, 3, 4])
b = a[:2].copy()
b *= 3
print('a=', a, 'b=', b)
print('\n')

# np.array.shape = (x, y): change to 2D array 
z = np.arange(10)
z.shape = (2, 5)
print(z)
print('z[1, 3]:', z[1,3])
print('z[1, -1]:', z[1,-1])