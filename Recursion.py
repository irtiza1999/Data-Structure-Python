# Find the sum of digits of a positive integer number using recursion?

# def sumofDigits(n):
#     assert n >= 0 and int(n) == n, 'The number has to be a positive integer only!'
#     if n == 0:
#         return 0
#     else:
#         print(n)
#         return int(n % 10) + sumofDigits(int(n / 10))
#
#
# print("Result", sumofDigits(12))


# # Calculate power of a number using recursion?

# # x^n = n * x^n-1
#
# def power(base, exponent):
#     assert exponent >= 0 and int(exponent) == exponent and int(base) == base, 'The number has to be a positive integer only!'
#     if exponent == 0:
#         return 1
#     if exponent == 1:
#         return base
#     else:
#         return base * power(base, exponent - 1)
#
#
# print(power(2, 4))

# Find GCD (Greatest Common Divisor) of two numbers using resursion?
# Euclidean algorithm
# def Gcd(a, b):
#     assert int(a) == a and int(b) == b, 'Some error occoured!!'
#     if a < 0:
#         a = a * -1
#     if b < 0:
#         b = b * -1
#     if b == 0:
#         return a
#     else:
#         return Gcd(b, a % b)
#
#
# print(Gcd(18, -48))

# Convert a decimal number into binary using recursion

# def convBinary(num):
#     assert num >= 0 and int(num) == num, "An error occoured"
#     if num == 0:
#         return 0
#     else:
#         return num % 2 + 10 * convBinary(int(num / 2))
#
#
# print(convBinary(-1))
