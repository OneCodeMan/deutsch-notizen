'''
February 17, 2020 (HAPPY BIRTHDAY DON, MY HOUSEMATE)
I want to practice spelling words in German using the correct
letter pronunciation. Therefore, I made a list of words to record
myself spelling and I want to see if the list contains all letters.

This program takes a list of words (all command line arguments) and
displays what letters are missing from that list.
'''
import string
import sys

UMLAUTS = list('äöü')
ESZETT = 'ß'
ALL_CHARACTERS = list(string.ascii_lowercase) + UMLAUTS
ALL_CHARACTERS.append(ESZETT)
CHARACTER_SET = set(ALL_CHARACTERS)

words = sys.argv[1:] # remember that 0th index is the program name
letter_set = set(''.join(words))

missing_letters = CHARACTER_SET.difference(letter_set)
if missing_letters:
    print("Missing these letters: ", missing_letters)
else:
    print("All letters are covered. :)")
