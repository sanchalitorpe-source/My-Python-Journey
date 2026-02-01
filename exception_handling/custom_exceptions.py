class NegativeNumberError(Exception):
    """Raised when a negative number is entered"""
    pass


def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    else:
        print("Valid number:", num)


try:
    number = int(input("Enter a number: "))
    check_number(number)
except NegativeNumberError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Please enter a valid integer")
