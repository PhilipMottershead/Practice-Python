# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input)
# compare them, print out a message of congratulations to the winner
# ask if the players want to start a new game
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_one_win = "Player One Won"
player_two_win = "player Two Won"


def game():
    new_game = True
    while new_game:
        if is_one_or_two_player():
            player_one_input = user_game_input()
            player_two_input = ai_game_input()
            print("CPU played " + player_two_input)
        else:
            player_one_input = user_game_input()
            player_two_input = user_game_input()
        check_result(player_one_input, player_two_input)
        if not is_new_game():
            new_game = False


def ai_game_input():
    return random.choice([rock, paper, scissors])


def check_result(player_one, player_two):
    if draw(player_one, player_two):
        print("Draw")
    else:
        print(rock_paper_scissors(player_one, player_two))


def is_new_game():
    while True:
        input_value = input("New Game?\nY for yes\nN for N\n")
        if input_value == "Y" or input_value == "y":
            return True
        elif input_value == "N" or input_value == "n":
            return False
        else:
            print("Invalid argument Enter Y for Yes or N for No\n")


def is_one_or_two_player():
    while True:
        input_value = input("One or two Player?\n1 for one player vs CPU\n2 for two player with second user \n")
        if input_value == "1":
            return True
        elif input_value == "2":
            return False
        else:
            print("Invalid argument Enter 1 for one player or 2 for two player\n")


def user_game_input():
    while True:
        input_value = input("Rock, Paper, Scissors?\nR for Rock\nP for Paper\nS for Scissors : \n").capitalize()
        if input_value == "R":
            return rock
        elif input_value == "S":
            return scissors
        elif input_value == "P":
            return paper
        else:
            print("Invalid argument")


def draw(player_one, player_two):
    if player_one == player_two:
        return True
    else:
        return False


def rock_paper_scissors(player_one, player_two):
    outcomes = {
        (rock, scissors): "Rock breaks Scissors",
        (scissors, paper): "Scissors cuts Paper",
        (paper, rock): "Paper beats Rock"
    }

    # checks if player 1 or 2 has won
    if (player_one, player_two) in outcomes:
        print(outcomes.get((player_one, player_two)))
        return player_one_win
    elif (player_two, player_one) in outcomes:
        print(outcomes.get((player_two, player_one)))
        return player_two_win


game()
