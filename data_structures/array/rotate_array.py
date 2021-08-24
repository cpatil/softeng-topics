"""
Given an unsorted array arr[] of size N, rotate it by D elements (clockwise). 

Input:
The first line of the input contains T denoting the number of testcases. First line of each test case contains two space separated elements, N denoting the size of the array and an integer D denoting the number size of the rotation. Subsequent line will be the N space separated array elements.

Output:
For each testcase, in a new line, output the rotated array.

Constraints:
1 <= T <= 200
1 <= N <= 107
1 <= D <= N
0 <= arr[i] <= 105

Example:
Input:
2
5 2
1 2 3 4 5 
10 3
2 4 6 8 10 12 14 16 18 20

Output:
3 4 5 1 2
8 10 12 14 16 18 20 2 4 6

Explanation :
Testcase 1: 1 2 3 4 5  when rotated by 2 elements, it becomes 3 4 5 1 2.
"""
import array

# My Solution
def rotate_my_solution(arr, d, n):
    for i in range(n):
        arr[i] += d
        if arr[i] > n:
            arr[i] -= n
            continue
    return arr

# Method 2: Rotate one by one
# Time complexity: O(n*d)
# Auxiliary Space: O(1)
def left_rotate_one_by_one(arr, d, n):
    for i in range(d):
        left_rotate_one(arr, n)

def left_rotate_one(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n-1] = temp

# Method 3: A juggling algorithm
# Divide array in sets which is equal to the GCD of n and d and move the elements within sets
# If GCD is 1 as is for the above example array (n=7 and d=2), then elements will be moved 
# within one set only, we just start with temp = arr[0] and keep moving arr[i+d] to arr[i] and 
# finally store temp at the right place
# Time complexity: O(n)
# Auxiliary Space: O(1)
def left_rotate_by_sets(arr, d, n):
    d = d % n
    for i in range(gcd(d, n)):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def gcd(d, n): 
    if n == 0:
        return d
    else:
        return gcd(n, d % n) 

def print_arr(arr, size):
    for i in range(size):
        print("% d" % arr[i], end=" ")

arr0 = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr1 = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

left_rotate_one_by_one(arr0, 2, len(arr0))
print_arr(arr0, len(arr0))

print('\n')

left_rotate_by_sets(arr1, 2, len(arr1))
print_arr(arr1, len(arr1))
