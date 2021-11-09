# https://www.hackerrank.com/challenges/arrays-ds/problem


a = [1, 4, 3, 2, 7]

# 1. [7, 4, 3, 2, 1] left_index = 0, right_index = -1
# 2. [7, 2, 3, 4, 1] left_index = 1, right_index = -2
# Output = [7, 2, 3, 4, 1]

left_element = 0
right_element = 0

for index in range(0, (len(a) // 2)):
    a[index], a[-(index + 1)] = a[-(index + 1)], a[index]

print(a)
