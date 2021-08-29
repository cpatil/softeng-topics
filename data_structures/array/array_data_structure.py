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