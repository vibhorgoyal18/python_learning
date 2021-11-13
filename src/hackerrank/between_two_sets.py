# https://www.hackerrank.com/challenges/between-two-sets/problem

a = [2, 6]
b = [24, 36]

lowest_range = max(a)
highest_range = min(b)
count = 0

for number in range(lowest_range, highest_range + 1):
    a_factor_of_number = True
    number_factor_of_b = True
    for i in a:
        a_factor_of_number = (number % i == 0)
        if not a_factor_of_number:
            break

    for j in b:
        number_factor_of_b = (j % number == 0)
        if not number_factor_of_b:
            break

    if a_factor_of_number and number_factor_of_b:
        count += 1

print(count)
