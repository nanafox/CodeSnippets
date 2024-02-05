#!/usr/bin/env python3

"""Prints all the public attributes and method of the Cmd framework"""

import cmd

if __name__ == "__main__":
    c = cmd.Cmd

    for attr in c.__dict__.keys():
        if attr.startswith("__"):
            continue

        print(f"{attr.ljust(10)}{type(c.__dict__[attr]).__name__.rjust(30)}")
