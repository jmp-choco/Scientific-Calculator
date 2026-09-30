import math


def sqrt(n):
    if n < 0:
        raise ValueError("Cannot find square root of a negative number.")
    return math.sqrt(n)


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


def sin(x, m):
    if m == "degrees":
        x = math.radians(x)
    return math.sin(x)


def cos(x, m):
    if m == "degrees":
        x = math.radians(x)
    return math.cos(x)


def tan(x, m):
    if m == "degrees":
        x = math.radians(x)
    return math.tan(x)


def log(n):
    if n <= 0:
        raise ValueError("Log requires a positive number.")
    return math.log10(n)


def ln(n):
    if n <= 0:
        raise ValueError("Natural log requires a positive number.")
    return math.log(n)


def fact(n):
    if n < 0 or n != int(n):
        raise ValueError("Factorial requires a non-negative whole number.")
    return math.factorial(int(n))