#!/usr/bin/env python3

"""This module defines a simple command-line calculator"""

import cmd
import os
import sys

class Calculator(cmd.Cmd):
    if os.isatty(sys.stdin.fileno()):
        prompt = "calc$ "
    else:
        prompt = ""

    intro = "Calculator v1.0. Type '?' or 'help' for available commands\n"

    @staticmethod
    def do_EOF(_):
        print()
        return True

    @staticmethod
    def do_quit(_):
        return True

    def emptyline(self):
        pass

    def do_add(self, line):
        """Prints the sum of numbers

        Args:
            line (str): The line received from the prompt.
        """
        args = self.get_numbers(line)

        print(sum(args))

    @staticmethod
    def help_add():
        print("Prints the sum of numbers. Usage: add <numbers> ...")

    @staticmethod
    def get_numbers(line):
        return list(map(int, line.split()))


if __name__ == "__main__":
    Calculator().cmdloop()
