from math import sqrt

p = -1
q = -1

c_before = -q / 2 + (q**2 / 4 + p**3 / 27) ** (1 / 2)
c = c_before ** (1 / 3)

lamb = c - p / (3 * c)
coef = 1 / lamb

n = 3
x = coef * lamb**n
print(x)


def F(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    return F(n - 2) + F(n - 3)


print(F(30))
