"""
File: hailstones.py
-------------------
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
"""


def main():
    """
    The problem can be expressed as follows:
        * Pick some positive integer and call it n.
        * If n is even, divide it by two.
        * If n is odd, multiply it by three and add one.
        * Continue this process until n is equal to one.
    """
    steps = 0
    n = int(input("Enter a number: "))
    while n <= 0:
        n = int(input("Enter a positive number: "))
    while n > 1:
        if n % 2 == 0:
            # n is even. So, divide it by two.
            print(n, "is even, so I take half:", end=" ")
            n //= 2
            print(n)
        else:
            # user_num is Odd. So, multiply it by three and add one.
            print(n, "is odd, so I make 3n + 1:", end=" ")
            n *= 3
            n += 1
            print(n)
        steps += 1
    print("The process took", steps, "steps to reach 1")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
