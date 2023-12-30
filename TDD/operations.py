#!/usr/bin/python3


def square_me(x: int) -> int:
    if isinstance(x, str):
        raise TypeError("do not square strings")

    if isinstance(x, float):
        raise TypeError("not handling float values yet, use integers")

    if not isinstance(x, int):
        raise TypeError("use only integers")

    return x ** 2
