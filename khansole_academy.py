"""
File: khansole_academy.py
-------------------------
This program is able to generate simple addition problems that involve adding two 2-digit integers
(i.e., the numbers 10 through 99).
The user is asked for an answer to each problem.  This program determines if the answer was correct or not,
and give the user an appropriate message to let them know.
This program keeps giving the user problems until the user has gotten 3 problems correct in a row.
"""

import random
ANSWERS_TO_PASS = 3
MIN_RANDOM = 10
MAX_RANDOM = 99


def main():
    """
    This program that randomly generates simple addition problems for the user, reads in the answer from the user,
    and then checks to see if they got it right or wrong, until the user appears to have mastered the material.
    i.e. the program keep giving the user problems until the user has gotten 3 problems correct in a row.
    """
    usr_correct_answer = 0
    while usr_correct_answer < ANSWERS_TO_PASS:
        # generate first random number
        first_rand = int(get_rand())
        # generate second random number
        second_rand = int(get_rand())
        # ask the question
        print("What is", first_rand, "+", str(second_rand) + '?')
        answer = int(input("Your answer: "))
        if first_rand + second_rand == answer:
            usr_correct_answer += 1
            print("Correct!  You've gotten", usr_correct_answer, "correct in a row.")
            if usr_correct_answer == 3:
                print("Congratulations!  You mastered addition.")
        else:
            usr_correct_answer = 0
            print("Incorrect.  The expected answer is", str(first_rand + second_rand))


def get_rand():
    # Generate a random integer between MIN_RANDOM and MAX_RANDOM, inclusively.
    return random.randint(MIN_RANDOM, MAX_RANDOM)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
