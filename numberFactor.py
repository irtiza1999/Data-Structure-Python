# Given N, find the number of ways to express N as a sum of 1, 3, 4.

# Divide and conqure
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


# Top Down Approach

def numberFactorTD(n, tempdict):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in tempdict:
            sub1 = numberFactorTD(n - 1, tempdict)
            sub2 = numberFactorTD(n - 3, tempdict)
            sub3 = numberFactorTD(n - 4, tempdict)
            tempdict[n] = sub1 + sub2 + sub3
        return tempdict[n]


# Bottom up approach

def numberFactorBU(n):
    tempArr = [1, 1, 1, 2]
    for i in range(4, n + 1):
        tempArr.append(tempArr[i - 1] + tempArr[i - 3] + tempArr[i - 4])
    return tempArr[n]


print(numberFactorBU(5))
