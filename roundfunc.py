"""
Round function after TDD
Function created and modified after tests were written
"""


def my_round(number):
    """ doc string """
    if not number:
        raise TypeError("Invalid input")
    if not isinstance(number, float):
        raise TypeError("Input should be number")
    return round(number)
