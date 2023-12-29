#!/usr/bin/python3


def add(x: float, y: float) -> float:
    """
    Returns the sum of two numbers (intgers or floats)

    Args:
        x (float): the first number
        y (float): the second number

    Returns:
        float: the sum of the two numbers

    Raises:
        TypeError: when any of the arguments given is not either an integer or a
        float

    Tests:
        >>> add(10.5, .5)
        11.0

        >>> add("3", 1)
        Traceback (most recent call last):
        ...
        TypeError: operands must be an integer or float
    """
    if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
        raise TypeError("operands must be an integer or float")

    return x + y


def subtract(x: float, y: float) -> float:
    """
    Returns the difference of two numbers (intgers or floats)

    Args:
        x (float): the first number
        y (float): the second number

    Returns:
        float: the difference of the two numbers

    Raises:
        TypeError: when any of the arguments given is not either an integer or a
        float

    Tests:
        >>> subtract(10.5, .5)
        10.0

        >>> subtract("3", 1)
        Traceback (most recent call last):
        ...
        TypeError: operands must be an integer or float
    """
    if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
        raise TypeError("operands must be an integer or float")

    return x - y


def multiply(x: float, y: float) -> float:
    """
    Returns the product of two numbers (intgers or floats)

    Args:
        x (float): the first number
        y (float): the second number

    Returns:
        float: the product of the two numbers

    Raises:
        TypeError: when any of the arguments given is not either an integer or a
        float

    Tests:
        >>> multiply(10.5, .5)
        5.25

        >>> multiply("3", 1)
        Traceback (most recent call last):
        ...
        TypeError: operands must be an integer or float
    """
    if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
        raise TypeError("operands must be an integer or float")

    return x * y


def divide(x: float, y: float) -> float: 
    """
    Returns the quotient of two numbers (intgers or floats)

    Args:
        x (float): the first number
        y (float): the second number

    Returns:
        float: the quotient of the two numbers

    Raises:
        TypeError: when any of the arguments given is not either an integer or a
        float
        ZeroDivisionError: when a divisor is zero

    Tests:
        >>> divide(10, 5)
        2.0

        >>> divide(5, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: Cannot divide with zero

        >>> divide("10", 5)
        Traceback (most recent call last):
        ...
        TypeError: operands must be an integer or float
    """
    if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
        raise TypeError("operands must be an integer or float")
    
    if y == 0:
        raise ZeroDivisionError("Cannot divide with zero")

    return x / y
