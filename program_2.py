# Programmer: Austin Long
# Date: 2025-03-19
# Program: Word Separator

# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together,
# but the first character of each word is uppercase.
# Convert the sentence to a string in which the words are separated by spaces,
# and the first word starts with an uppercase.
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence: str):

    new_sentence = ""
    #    Add your logic here

    # iterate over characters
    for ch in sentence:
        # If lowercase, append
        if ch.islower():
            new_sentence += ch
        # If uppercase, start a new word.
        else:
            new_sentence += " " + ch.lower()

    return new_sentence.strip()

# Example usage

if __name__ == "__main__":
    sentence = "StopAndSmellTheRoses"

    new_sentence = word_separator(sentence)

    print(new_sentence)
