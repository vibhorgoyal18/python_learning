# https://www.hackerrank.com/challenges/the-birthday-bar/problem

s = [1, 2, 1, 3, 2]
d = 3
m = 2
count = len([i for i in range(0, len(s) - (1 if m > 1 else 0)) if sum(s[i:i + m]) == d])

print(count)
