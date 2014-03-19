"""
 A sample program!

 ~cvolny
"""


def factorial(x):
    """
    Calculate the factorial of x iteratively.
    """
    y = 1
    if not float(x).is_integer():
        raise ValueError("Factorial undefined for non-integers.")
    if x < 1:
        raise ValueError("Factorial undefined for less than 1.")
    while x > 1:
        y *= x
        x -= 1
    return y


if "__main__" == __name__:
    """
    Main Program

    Loop until the user enters an integer to calculate the factorial of, then print and exit.
    """
    while True:
        try:
            m = raw_input("Enter an integer: ")
            d = int(m)
            r = factorial(d)
            print "{0:d}! = {1:d}".format(d, r)
            break
        except Exception:
            print "Invalid input, try again."