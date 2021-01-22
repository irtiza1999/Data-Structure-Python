# Given N, find the number of ways to express N as a sum of 1, 3, 4.

def numberFactor(n):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        sub1 = numberFactor(n - 1)
        sub2 = numberFactor(n - 3)
        sub3 = numberFactor(n - 4)
        return sub1 + sub2 + sub3


print(numberFactor(15))
