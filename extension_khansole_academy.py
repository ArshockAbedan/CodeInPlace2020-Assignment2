"""
File: extension_khansole_academy.py
-------------------------
This program is able to generate simple mathematical problems that involve operating
(subtraction, multiplication, division, and more) two 2-digit integers i.e., the numbers 10 through 99.
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
    This program that randomly generates simple mathematical problems for the user, reads in the answer from the user,
    and then checks to see if they got it right or wrong, until the user appears to have mastered the material.
    i.e. the program keep giving the user problems until the user has gotten 3 problems correct in a row.
    """
    # correct_counter variable counts the number of correct answers
    correct_counter = 0
    while correct_counter < ANSWERS_TO_PASS:
        # generate first random number
        first_rand = int(rand_num())
        # generate second random number
        second_rand = int(rand_num())
        # generate random operation
        opt_rand = (rand_operation())
        # ask the question
        print("What is", first_rand, opt_rand, str(second_rand) + '?')
        answer = int(input("Your answer: "))
        expected_answer = compute_answer(first_rand, opt_rand, second_rand)
        # compare_flag is True when expected_answer and answer are equal
        compare_flag = compare_values(expected_answer, answer)
        if compare_flag:
            correct_counter += 1
            print("Correct!  You've gotten", correct_counter, "correct in a row.")
            if correct_counter == 3:
                print("Congratulations!  You mastered Math.")
        else:
            correct_counter = 0
            print("Incorrect.  The expected answer is", str(expected_answer))


def rand_num():
    # Generate a random integer between MIN_RANDOM and MAX_RANDOM, inclusively.
    return random.randint(MIN_RANDOM, MAX_RANDOM)


def compute_answer(first_num, opt, second_num):
    """
    This function computes the result of applying the opt operation on first_num and second_num.
    This result would be returned as its returned values.
    Doctest
    >>> compute_answer(3, "+", 5)
    8
    >>> compute_answer(27, "-", 15)
    12
    >>> compute_answer(90, "//", 11)
    8
    >>> compute_answer(5, "%", 2)
    1
    """
    if opt == '+':
        result = first_num + second_num
    elif opt == '-':
        result = first_num - second_num
    elif opt == '//':
        result = first_num // second_num
    else:
        # it means %
        result = first_num % second_num
    return result


def compare_values(value, answer):
    """ This function Compares the value parameter with the answer parameter
    and if they were equal, the returned flag would be True, otherwise would be False.
    Doctest
    >>> compare_values(5, 5)
    True
    >>> compare_values(6, 4)
    False
    """
    if value == answer:
        return True
    else:
        return False


def rand_operation():
    """
    This Function Generate a random mathematical operation i.e. + , - , / , // and %
    """
    rand = random.randint(1, 4)
    if rand == 1:
        return "+"
    elif rand == 2:
        return "-"
    elif rand == 3:
        return "//"
    else:
        return "%"


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
