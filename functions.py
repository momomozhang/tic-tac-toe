#!/usr/bin/env python3
"""
Tic-Tac-Toe Game

A simple implementation of the classic Tic-Tac-Toe game with a command-line interface.
Players take turns marking X and O on a 3x3 grid, aiming to get three of their marks in a row.
"""

import os
import random

# Set up the data structure
# Board is a 3x3 grid. it's data structure is a dictionary. 
# The dictionary keys are the name of 9 squares from A1 - C3.
valid_cells = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# Before each square is taken, the square's name will be shown, so it's easy for the players to choose.
board = {cell: f"({cell})" for cell in valid_cells}


def display_game(board):
    """Display the board, update it according to players' choices"""
    print("\n" + "="*30 + "\n")
    print(board["A1"] + " | " + board["A2"] + " | " + board["A3"])
    print("__________________")
    print(board["B1"] + " | " + board["B2"] + " | " + board["B3"])
    print("__________________")
    print(board["C1"] + " | " + board["C2"] + " | " + board["C3"])

def player_order():
    """Automatically decide the player order."""
    print("Now enter both your names!")

    #get users' names
    player_a = input("Enter the first name: ")
    player_b = input("Enter the second name: ")
    print(f"We have {player_a} and {player_b}!")

    #draw the random order
    players = [player_a, player_b]
    random.shuffle(players)

    #print the player order
    print(f"{players[0] goes first!}")
    



