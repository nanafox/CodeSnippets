#!/usr/bin/python3


def do_something(*ingredients: str, **names: list[str]) -> None:
    for i, ingredient in enumerate(ingredients, start=1):
        print(f"{i}: {ingredient}")

    print()
    for key, value in names.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    ingredients = ("tomatoes", "onion", "pepper")
    chefs = {
        "morning_shift": ["Eze", "Value"],
        "afternoon_shift": ["Zoba", "Clarkson"],
        "evening_shift": ["Maxwell", "Eze"],
    }

    do_something(*ingredients, **chefs)
