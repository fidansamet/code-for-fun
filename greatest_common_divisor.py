"""Calculates the greatest common divisor (GCD) of a and b is the
largest number that divides both of them with no remainder."""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(36,8))
