# https://www.hackerrank.com/challenges/kangaroo/problem?h_r=next-challenge&h_v=zen

x1, v1, x2, v2 = 0, 3, 4, 2
same_location_possible = False
while (x1 < x2 and v1 > v2) or (x1 > x2 and v1 < v2):
    x1, x2 = (x1 + v1), (x2 + v2)
else:
    if x1 == x2:
        same_location_possible = True

print('YES' if same_location_possible else 'NO')