def num(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Please enter a valid number.")


def pos(msg):
    while True:
        n = num(msg)

        if n > 0:
            return n

        print("Please enter a number greater than 0.")


def mode():
    while True:
        m = input("Enter mode (degrees/radians): ").lower()

        if m == "degrees" or m == "radians":
            return m

        print("Please enter degrees or radians.")