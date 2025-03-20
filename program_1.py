# Programmer: Austin Long
# Date: 2025-03-19
# Program: Initials

# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names,
# and displays their first, middle, and last initials.
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11


def initials_generator(persons_name):

    persons_initials = ""
    #    Add your logic here

    # Get first character from each word
    initials = [s[0] for s in persons_name.split(" ")]

    # Append each inital with separators to the accumulator
    for inital in initials:
        persons_initials += inital + ". "

    return persons_initials.strip()


if __name__ == "__main__":
    personsName = input("Enter the users first, middle, and last name")

    initials = initials_generator(personsName)

    print(initials)
