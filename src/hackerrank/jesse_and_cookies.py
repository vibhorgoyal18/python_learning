# https://www.hackerrank.com/challenges/jesse-and-cookies/problem

A = [1, 2, 9]
k = 9

more_mixes_required = True
number_of_tries = 0

while more_mixes_required and len(A) != 1:
    A = sorted(A)
    if A[0] >= k:
        more_mixes_required = False
    else:
        temp = A[0] + (2 * A[1])
        A[0] = temp
        A.pop(1)
        number_of_tries += 1

if len(A) == 1 and A[0] < k:
    print(-1)

else:
    print(number_of_tries)
