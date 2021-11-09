# https://www.hackerrank.com/challenges/apple-and-orange/problem

s, t, a, b, m, n, apples, oranges = 7, 11, 5, 15, 3, 2, [-2, 2, 1], [5, -6]

print(f"Number of apples {len([apple for apple in apples if t >= (a + apple) >= s])}")
print(f"Number of oranges {len([orange for orange in oranges if t >= (b + orange) >= s])}")