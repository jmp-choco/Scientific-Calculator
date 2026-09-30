from calculator import add, sub, mul, div, rem, power

from scientific import sqrt, square, cube, sin, cos, tan, log, ln, fact

from validators import num, pos, mode


def menu():
    print()
    print("===== SCIENTIFIC CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Power")
    print("7. Square Root")
    print("8. Square")
    print("9. Cube")
    print("10. Sin")
    print("11. Cos")
    print("12. Tan")
    print("13. Log")
    print("14. Natural Log")
    print("15. Factorial")
    print("16. Exit")
    print()


def main():

    while True:

        menu()

        ch = input("Enter your choice: ")

        try:

            if ch == "1":

                a = num("Enter first number: ")
                b = num("Enter second number: ")

                print("Result:", add(a, b))


            elif ch == "2":

                a = num("Enter first number: ")
                b = num("Enter second number: ")

                print("Result:", sub(a, b))


            elif ch == "3":

                a = num("Enter first number: ")
                b = num("Enter second number: ")

                print("Result:", mul(a, b))


            elif ch == "4":

                a = num("Enter first number: ")
                b = num("Enter second number: ")

                print("Result:", div(a, b))


            elif ch == "5":

                a = num("Enter first number: ")
                b = num("Enter second number: ")

                print("Result:", rem(a, b))


            elif ch == "6":

                a = num("Enter base: ")
                b = num("Enter power: ")

                print("Result:", power(a, b))


            elif ch == "7":

                n = num("Enter number: ")

                print("Result:", sqrt(n))


            elif ch == "8":

                n = num("Enter number: ")

                print("Result:", square(n))


            elif ch == "9":

                n = num("Enter number: ")

                print("Result:", cube(n))


            elif ch == "10":

                x = num("Enter angle: ")
                m = mode()

                print("Result:", sin(x, m))


            elif ch == "11":

                x = num("Enter angle: ")
                m = mode()

                print("Result:", cos(x, m))


            elif ch == "12":

                x = num("Enter angle: ")
                m = mode()

                print("Result:", tan(x, m))


            elif ch == "13":

                n = pos("Enter positive number: ")

                print("Result:", log(n))


            elif ch == "14":

                n = pos("Enter positive number: ")

                print("Result:", ln(n))


            elif ch == "15":

                n = num("Enter non-negative whole number: ")

                print("Result:", fact(n))


            elif ch == "16":

                print("Thank you!")

                break


            else:

                print("Invalid choice.")


        except ValueError as e:

            print("Error:", e)


main()