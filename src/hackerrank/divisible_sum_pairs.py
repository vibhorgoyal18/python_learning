# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

ar = [1, 3, 2, 6, 1, 2]
k = 3
count = 0
for i in range(0, len(ar) - 1):
    for j in range(i + 1, len(ar)):
        if (ar[i] + ar[j]) % k == 0:
            count += 1

print(count)
