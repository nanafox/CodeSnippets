#!/usr/bin/env python3

from datetime import date


class Student:
    threshold = 75  # class attribute

    def __init__(self, name, age, course, cohort):
        self.name = name
        self.age = age
        self.course = course
        self.cohort = cohort

    def __str__(self):
        return (
            f"Name: {self.name}\nAge: {self.age}\n"
            f"Course: {self.course}\nCohort: {self.cohort}"
        )

    def defer(self, to_cohort, option="start afresh"):
        if self.cohort == to_cohort:
            print("Can't defer to the same cohort")
            return

        print(f"Sorry to see you go {self.name}.")
        print(f"You've deffered to cohort {to_cohort}.")
        print(f"And you have chosen to {option}")
        
        self.cohort = to_cohort

    @classmethod
    def update_threshold(cls, new_threshold):
        cls.threshold = new_threshold

    @staticmethod
    def is_captains_log_day(date):
        if date.isoweekday() >= 5 and date.isoweekday() <= 7:
            return True

        return False


student_1 = Student("Samson Ekeno", 24, "Electrical Engineering", 19)
student_2 = Student("Ahmed Nule", 24, "Software Engineering", 17)

print(student_1, end="\n\n")
print(student_2, end="\n\n")

result = student_1.is_captains_log_day(date(2024, 2, 12))

if result is True:
    print("Today is a Captain's log day. Have you logged it yet?")
else:
    print("Today is not a Captain's log day. Enjoy your day")
