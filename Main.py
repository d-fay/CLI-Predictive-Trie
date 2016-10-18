"""

A CLI based python program used to demonstrate the use of a trie data structure, (pronounced 'try'),
for storing a dictionary of words and generating lists of all possible outcomes provided some input.

Program starts by searching the working directory for a .txt file containing a list of words which
are then imported into a trie data structure. After constructing a trie containing all words. The
program then asks the user to enter a word character by character. After each character is entered
into the CLI, the user presses enter/return and the program responds with a list of possible words
(contained in the provided dictionary file). This list of possible words is limited in length by
the variable num_words_to_select (defined below).

REQUIREMENTS:

    - Interpreter: python2.7
    - File: WordTrie.py

"""

import WordTrie
import os
import sys
import fileinput
import random

num_words_to_select = 10      # the number of suggested words to provide
current_string = ""


"""
Import dictionary file and create trie data structure (character-by-character)
-----------------------------------------------------------------------------------------------------------------
Create a new WordTrie object. Read file line-by-line, insert_word each word into tree object.

 - Checks working directory for any file with .txt extension
 - Intended for use with only one .txt dictionary file located in the working directory

"""
file_names = os.listdir(os.curdir)
found = False   # flag to inform program if no .txt file exists
print "Searching in working directory for .txt file(s)"
print(". . . \n")
for file_name in file_names:
    if os.path.isfile(file_name) and file_name.endswith('.txt'):
        found = True    # dictionary file found
        print "Importing file " + file_name + " and creating dictionary trie."
        trie = WordTrie.WordTrie()
        count = 0       # count number of words imported
        for line in fileinput.input([file_name]):
            trie.insert_word(line)
            count += 1
        print "Finished " + file_name + " import. " + str(count) + " words successfully added to dictionary.\n"
if not found:
    sys.stderr.write('No .txt files found in working directory.')


"""
Searching & user interaction via CLI
-----------------------------------------------------------------------------------------------------------------
Input/output via command line

 - User is prompted to enter a prefix string for searching the tree by typing one single character at a time.
 - Input string (prefix) is checked for length and when it is at least one character long the program enters
   an infinite loop until the user types in the word 'exit' to terminate the program. Otherwise it will
   indefinitely prompt the user for more characters to accommodate words of infinite length.
 - Requires two responses from the user before searching the dictionary.
 - Each time the user presses the enter/return key the current character(s) entered will be appended to the
   existing search term.
 - Once the prefix results in a list of one or less possible words the program terminates.
 - If the dictionary contains only one word for the given prefix, it will inform the user that there is only
   one compatible word with the prefix they entered, display that word, and proceed to end the program.

"""

# Prompt user for the first character of the word they are 'searching' and append to search term (current_string)
while len(current_string) < 1:
    current_input = raw_input("Please type the first character in the word you would like to search for "
                              "and then press enter. (Type \'exit\' to quit)\n")
    current_string += current_input
    print("Current string: " + current_string)

exit_flag = False   # controls flow of while loop and provides user the option to quit the program

# Once the prefix string contains_word at least one character, we start the main loop
while not exit_flag:

    # Ask user for input and assign to variable
    current_input = raw_input("Please type the next character in your word and press enter. "
                              "(Type \'exit\' to quit)\n")

    # provide user ability to quit program before it is finished
    if not current_input == "exit":

        # append current new character input to existing prefix
        current_string += current_input
        print("Current prefix string: " + current_string + "_")

        # create a new array containing all possible word outcomes given the provided input (prefix)
        array_of_words_with_prefix = trie.get_all_possible_words(current_string)  # CALL TO TRIE CLASS

        # check if we need to reduce the amount of words returned to the user
        if len(array_of_words_with_prefix) >= num_words_to_select:
            print("\n" + str(num_words_to_select) + " randomly selected words contained in dictionary with prefix "
                                              "\'" + current_string + "-\' include: \n")

            # create list of words (for current prefix) in random order & reduce list length to 'num_words_to_select'
            list_of_random_valid_words = random.sample(array_of_words_with_prefix, num_words_to_select)

            # print all words in list_of_random_words (will only print amount of words defined in num__words_to_select)
            for word in list_of_random_valid_words:
                print(word)

        # condition for no words matching prefix input
        elif len(array_of_words_with_prefix) == 0:
            print "No word in dictionary with matching prefix: " + current_string + "\n"
            print "Ending program..."
            break

        # condition for list of one word (occurs when input the only possible match)
        elif len(array_of_words_with_prefix) == 1:
            print "There is only one word in the dictionary that matches your input: \n"
            print array_of_words_with_prefix[0]
            print "Ending program..."
            break

        # default condition (for all other cases)
        else:
            print "There are " + str(len(array_of_words_with_prefix)) + " words matching your input: \n"

            # print all words in list_of_random_words (will only print amount of words defined in num_words_to_select)
            for word in array_of_words_with_prefix:
                print(word)

        # display the current prefix characters
        print "------------------------------------------------------------------------------"
        print("\nCurrent string: " + current_string)

    # end of program
    else:
        # end the while loop
        exit_flag = True

# terminate
sys.exit()
