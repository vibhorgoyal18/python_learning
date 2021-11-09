# https://www.hackerrank.com/challenges/2d-array/problem


arr = [[-9, -9, -9, 1, 1, 1],
       [0, -9, 0, 4, 3, 2],
       [-9, -9, -9, 1, 2, 3],
       [0, 0, 8, 6, 6, 0],
       [0, 0, 0, -2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

sum = []

for row in range(0, len(arr) - 2):
    for col in range(0, len(arr) - 2):
        current_sum = (arr[row][col] + arr[row][col + 1] + arr[row][col + 2] + arr[row + 1][col + 1] + arr[row + 2][col] +
                       arr[row + 2][col + 1] + arr[row + 2][col + 2])
        sum.append(current_sum)
        print(current_sum)

print('Max sum: {}'.format(max(sum)))
