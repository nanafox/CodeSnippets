#!/usr/bin/python3


def square_me(x: int) -> int:
    """
    Returns the square of an integer.

    Args:
        x (int): The integer number to square.

    Returns:
        int: The square of x.

    Raises:
        TypeError: When the value received is non-integer.
    """
    if isinstance(x, str):
        raise TypeError("do not square strings")

    if isinstance(x, float):
        raise TypeError("not handling float values yet, use integers")

    if not isinstance(x, int):
        raise TypeError("use only integers")

    return x**2
