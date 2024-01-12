#!/usr/bin/python3


def print_score(name: str, **kwargs) -> None:
    print(name)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    print_score("Israel", math="89", science="98", DSA="100")
