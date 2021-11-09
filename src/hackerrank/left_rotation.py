# https://www.hackerrank.com/challenges/array-left-rotation/problem

def rotate_left(d, arr):
    # left_rotation = []
    # for i in range(d, len(arr)):
    #     left_rotation.append(arr[i])
    #
    # for i in range(0, d):
    #     left_rotation.append(arr[i])

    # return left_rotation

    return arr[d:len(arr)] + arr[0:d] # [3, 4, 5] + [1, 2]


print(rotate_left(2, [1, 2, 3, 4, 5]))
