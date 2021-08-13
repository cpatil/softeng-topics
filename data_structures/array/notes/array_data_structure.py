"""
Array Data Structure Notes W/ Examples
 
By: Joshua Henriques 

Arrays:
- Collection of elements (values or vaiables), each identified by at 
    lease one array index or key
- Needs a memory block for allocation, called consecutive memory location
- Stores elements at a contiguous memory location
- Is stored such that the position of each element can be computed from
    its index tuple by a mathematical formula.
- Memory is a one-dimensional array of words, whose indices are their 
    addresses
- Processors/Vector processors are optimized for array operations
- Useful mostly because the element indices can be computed at run time,
    this feature allows a single iterative statement to process arbitrarily
    many elements.
- Required to have the same size and should use the same data representation (homogenous)
- The set of valid index tuples and the addresses of the elements are usually,
    but not always, fixed while the array is in use
- Associative array (abstract array)*
- In order to create a shorter or longer array, you need to create a new array and
  copy all elements from old to new
- Immutable, mutable arrays are called list

Usages:
- To implement mathematical vectors and matrices, as well as other rectangular
  tables
- Databases consist of (or include) 1D arrays whose elements are records
- To implement lists, heaps, hash tables, deques, queues, stacks, strings, VLists
- Used to emulate in-program dynamic memory allocation, particularly memory pool
  allocation
- To implement control tables that are used in conjection with a purpose built
  interpreter whose control flow is altered according to the elements

Efficiency:
- Offers fast O(1) search if you know the index, but adding and removing an element is slow
  because you cannot change the size 
- Both store and select take (deterministic worst case) constant time. Arrays 
  take linear O(n) space in the number of elements n that they hold
*- Sequential iteration over an array is noticeably faster in practice than iteration
    over many other data structures, a property called locality of reference 
    - Locality is a type of predicatable behaviour that occurs in computer systems
    - Systems with strong locality of reference are greate candidates for performance
      optimization through the use of caching, prefetching for memory and advanced
      branch predictors at the pipelining stage of a processor core   
    - Locality of reference (princible of locality): is the tendency of a processor
        to access the same set of memory locations repetitively over a short period of 
        time. Two types: 
        - Temporal locality refers to the reuse of specific data and/or
          resources within a relatively small time duration.
        - Spatial locality (data locality) refers to the use of data elements within 
          relatively close storage locations 
        - Sequential locality, a special case of spatial locality, occurs when data
          elements are arranged and accessed linearly, such as traversing the elements
          in a one-dimensional array
- Memory-wise, arrays are compact data structures with no per-element overhead.
- Elements stored in an array can require less memory because several array elements 
  can be stored in a single word; such arrays are called packed arrays
    - Word: Is a fixed-sized piece of data handled as a unit by the instruction set or
      the hardware of the processor
        - The number of bits in a word is an important characteristic of any specification
          processor design or computer architecture
"""


"""
Type Code               C Type                Python Type               Min size in bytes to
'b'                     signed char           int                       1
'B'                     unsigned char         int                       1
'u'                     wchar_t               unicode char              2
'h'                     signed short          int                       2
'H'                     unsigned short        int                       2
'i'                     signed int            int                       2
'I'                     unsigned int          int                       2
'l'                     signed long           int                       4
'L'                     unsigned long         int                       4
'q'                     signed long long      int                       8
'Q'                     unsigned long long    int                       8
'f'                     float                 int                       4
'd'                     double                int                       8
"""

# array module for simple 1d arrays 
import array

# declaration
numbers = array.array('i', [32, 133, 5, 573, 4, 908]) 

print('numbers: ', numbers)

print('\n')

unicode = array.array('u', 'hello \u2641')
print(unicode)

print('\n')

# index 2
print('numbers[2]: ', numbers[2])

print('\n')

# second from last
print('numbers[-2]: ', numbers[-2])

print('\n')

# slice from 1 inclusive to 5 exclusive
print('numbers[1:5]: ', numbers[1:5])

print('\n')

# slice from 0 to 2 exclusive
print('numbers[:2]: ', numbers[:2])

print('\n')

# assign index 5
numbers[5] = 829
print('numbers: ', numbers)

print('\n')

# Array methods:

# array.typecode
# The typecode character used to create the array
print('numbers.typecode:', numbers.typecode)

print('\n')

# array.itemsize
# The length in bytes of one array item in the internal representation
print('numbers.itemsize:', numbers.itemsize)

print('\n')

# array.index(x) 
# Return the smalles i such that i is the index of the first occurrence of x in the array
index = numbers.index(5)
print('index = numbers.index(5): ', numbers)

print('\n')

# array.append(x) 
# Append a new item with value x to the end of the array
numbers.append(444)
print('numbers.append(4): ', numbers)

print('\n')

# array.buffer_info()
# Return a tuple (address, length) giving the current memory address and the length in 
# elements of the buffer used to hold array's contents.
buffer_info = numbers.buffer_info()
print('numbers.buffer_info(): ', buffer_info)

# The size of the memory buffer in bytes can be computed as array.buffer_info()[1] * array.itemsize
memory_buffer_size = numbers.buffer_info()[1] * numbers.itemsize
print('memory_buffer_size: ', memory_buffer_size)

print('\n')

# array.insert(i, x) 
# Insert a new item with value x in the array before position i. Negative values are 
# treated as being relative to the end of the array
numbers.insert(3, 888)
print(numbers)

print('\n')

# array.count(x) 
# Return the number of occurrences of x in the array
numbers.append(829)
student_count = numbers.count(829)
print('student_count 829: ', student_count)

print('\n')

# array.extend(iterable) 
# Append items from iterable to the end of the array. If iterable is another array, 
# it must have exactly the same type code; if not, TypeError will be raised. If iterable 
# is not an array, it must be iterable and its elements must be the right type to be 
# appended to the array
more_numbers = array.array('i', [3954, 637, 108])
numbers.extend(more_numbers)
print('numbers.extend(more_numbers): ', numbers)

print('\n')

# array.pop([i]) 
# Removes the item with the index i from the array and returns it. The optional 
# argument defaults to -1, so that by default the last item is removed and returned
numbers.pop(2)
print('numbers.pop([2]): ', numbers)

print('\n')

# array.remove(x)
# Remove the first occurrence of x from the array
numbers.remove(32)
print('numbers.remove(32): ', numbers)

print('\n')

# array.reverse()
# Reverse the order of the items in the array
numbers.reverse()
print('numbers.reverse(): ', numbers)

print('\n')

# array.tobytes()
# Convert the array to an array of machine values and return the bytes representation 
# (the same sequence of bytes that would be written to a file by the tofile() method)
numbers_tobytes = numbers.tobytes()
print('numbers_tobytes: ', numbers_tobytes)