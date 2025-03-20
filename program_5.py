# Programmer: Austin Long
# Date: 2025-03-19
# Program: Course Info

# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."
# Then ask the user for a subject (like "COS").
# Finally, the program will display the ID and name of all the courses having that subject.

# Pseudocode

# Create dictionary
# While user enters input
#   Get course id and course description from user
#   Get category from course ID
#   Put course id and description into dictionary under category
# Get course IDs for subject
# For course id
#   Get course name
#   Print course ID and name

import re
from program_3 import get_input, interactive_get_input


def input_course(directory):
    def validate_course_id(course_id):
        return not not re.match(r"^[A-Za-z]{3}[0-9]{4}$", course_id)

    (done, course_id) = interactive_get_input(
        "Enter the course ID (empty for done): ",
        str,
        "That is an invalid course ID. Course IDs are in the format ABC1234.",
        validate_course_id,
    )

    if done:
        return False

    norm_course_id = course_id.upper().strip()

    course_category = re.match(r"^[A-Z]{3}", norm_course_id).group(0)

    if directory.get(course_category) == None:
        directory[course_category] = []

    course_info = input("Enter the course information: ")

    directory[course_category].append(norm_course_id + ": " + course_info)

    return True


def main():
    course_directory = {}

    while input_course(course_directory):
        continue

    def input_conversion(user_input):
        try:
            return course_directory[user_input.strip().upper()]
        except KeyError:
            raise ValueError()

    courses = get_input(
        f"Enter a category: ",
        input_conversion,
        err_message=f"That category is not in the directory.",
    )

    for course in courses:
        print(course)


if __name__ == "__main__":
    main()
