import math

from calculator import add, sub, mul, div, rem, power

from scientific import sqrt, square, cube, sin, cos, tan, log, ln, fact


def check(name, a, b):

    if math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9):
        print(name, ": PASS")
    else:
        print(name, ": FAIL")


print("===== TESTING SCIENTIFIC CALCULATOR =====")
print()


check("Addition", add(10, 5), 15)

check("Subtraction", sub(10, 5), 5)

check("Multiplication", mul(10, 5), 50)

check("Division", div(10, 5), 2)

check("Remainder", rem(10, 3), 1)

check("Power", power(2, 3), 8)

check("Square Root", sqrt(25), 5)

check("Square", square(5), 25)

check("Cube", cube(3), 27)

check("Sin 30", sin(30, "degrees"), 0.5)

check("Cos 60", cos(60, "degrees"), 0.5)

check("Tan 45", tan(45, "degrees"), 1)

check("Log 100", log(100), 2)

check("Natural Log", ln(math.e), 1)

check("Factorial", fact(5), 120)


try:

    div(10, 0)

    print("Division by zero : FAIL")

except ValueError:

    print("Division by zero : PASS")


try:

    sqrt(-1)

    print("Negative square root : FAIL")

except ValueError:

    print("Negative square root : PASS")


print()
print("===== ALL TESTS COMPLETED =====")