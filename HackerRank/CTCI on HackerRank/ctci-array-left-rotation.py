# 'Arrays: Left Rotation'
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
"""
Sample Input
5 4
1 2 3 4 5
"""

# O(n) time, O(n*k) space
# def array_left_rotation(array, n_array, k_rotations):
#     for e in range(k_rotations):
#         output = array[-1:] + array[:-1]
#     return(array)

# O(1) time, O(2) space
def array_left_rotation(array, n_array, k_rotations):
    k = k_rotations % n_array
    output = array[k_rotations:]+array[:k_rotations]
    return output


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k)
print ' '.join(map(str, answer))