# Programmer: Austin Long
# Date: 2025-03-19
# Program: Capital Quiz

# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys,
# and their capitals as values.
# The program should then randomly quiz the user by displaying the name of a state
# and asking the user to enter the state's capital.
# The program should count of the number of correct and incorrect responses.
# (You could alternatively use another country and provinces,
# or countries of the world and capitals).

import random
import os
import sys
from typing import Any, Callable

# I copied the data off a site and formatted it with Vim. Quite the pleasure!
CAPITALS = {
    "ALABAMA": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "WYOMING": "Cheyenne",
}

# These were copied from last week's programs


# Gets input where the user is not expected to quit.
def get_input(
    prompt: str,
    conversion: Callable[[str], Any],
    err_message: str = "Invalid input.",
    validation: Callable[[Any], bool] = lambda _: True,
) -> Any:
    return interactive_get_input(prompt, conversion, err_message, validation, None)[1]


# Gets input. If the user inputs terminator, then the function signals this to the caller.
def interactive_get_input(
    prompt: str,
    conversion: Callable[[str], Any],
    err_message: str = "Invalid input.",
    validation: Callable[[Any], bool] = lambda _: True,
    terminator: str | None = "",
) -> tuple[bool, Any]:
    try:
        # Gets input from user. If the program isn't running in interactive
        # mode, this skips prompting.
        user_input = input(prompt if os.isatty(0) else "")

        # If terminator found, signal to caller.
        if terminator != None and user_input == terminator:
            return (True, None)

        # convert input
        converted = conversion(user_input)

        # Check input validity
        if validation(converted):
            # Return successful value
            return (False, converted)
    except ValueError:
        pass

    # Retry input if error
    print(err_message, file=sys.stderr)
    return interactive_get_input(
        prompt, conversion, err_message, validation, terminator
    )


def main():
    capitals_keys = list(CAPITALS.keys())

    num_correct = 0
    num_incorrect = 0

    while True:
        state = random.choice(capitals_keys)

        (done, response) = interactive_get_input(
            f"Enter the capital for {state} (leave empty if done) ",
            str,
        )

        if done:
            break

        normalized_response = response.strip().upper()
        capital = CAPITALS[state]
        normalized_capital = capital.upper()

        if normalized_response == normalized_capital:
            print("Correct!")
            num_correct += 1
        else:
            print(f"Incorrect. The correct answer was {capital}.")
            num_incorrect += 1

    total = num_correct + num_incorrect

    if total == 0:
        print("Aww, come on! At least try!")
        return  # avoid division by zero

    print("Thanks for playing!")
    print(f"Your final score is {num_correct}/{total} ({num_correct/total:.2%}).")


if __name__ == "__main__":
    main()
