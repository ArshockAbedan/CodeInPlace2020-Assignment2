"""
File: nimm.py
-------------------------
Nimm is an ancient game of strategy that is named after the old German word for "take."
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China.
Players alternate taking stones until there are zero left.
The game of Nimm goes as follows:
1.The game starts with a pile of 20 stones between the players
2.The two players alternate turns
3. On a given turn, a player may take either 1 or 2 stone from the center pile
4.The two players continue until the center pile has run out of stones.The last player to take a stone loses.
"""


def main():
    """
    This program simulate playing Nimm game for two players. It will determine the winner at the end.
    """
    stones = 20
    player_turn = 1
    input_is_invalid = False
    while stones > 0:
        print("There are", stones, "stones left")
        print("Player", player_turn, end=" ")
        input_stones = int(input("would you like to remove 1 or 2 stones? "))
        input_is_invalid = is_input_invalid(input_stones)
        while input_is_invalid:
            input_stones = int(input("Please enter 1 or 2: "))
            input_is_invalid = is_input_invalid(input_stones)
        if player_turn == 1:
            player_turn = 2
        else:
            player_turn = 1
        stones -= input_stones
        print("")
    print("Player", player_turn, "wins!")


def is_input_invalid(user_input):
    """
    This function checks whether the user input is invalid or not.
    Doctest
    >>> is_input_invalid(2)
    False
    >>> is_input_invalid(4)
    True
    >>> is_input_invalid(-1)
    True
    """
    if user_input == 1 or user_input == 2:
        return False
    else:
        return True


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
