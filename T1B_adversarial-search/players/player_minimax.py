#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from player import Player
from util import *

# ==========================================
# Player Minimax
# ==========================================

class MinimaxPlayer(Player):

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, symbol):
        super(MinimaxPlayer, self).__init__(symbol)

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):

        # TODO Here you will implement the Minimax algorithm.
        # This method may return the best movement based on Minimax score
        # for the current board.

        # If you want, you can use here some helper functions:
        #
        # - find_winner(board): This method checks if someone wins in the
        #   parametrized board and return a tuple (Winner, Winner movement).
        #
        # - find_empty_cells(board): This method checks if there are available
        #   moves in the parametrized board. It returns an array containing
        #   the available moves.
        #
        # - print_board(board): This method helps you debugging your code.
        #   It prints a board filled with the executed moves.
        #   WARNING: printing can slow your code. Use it just for debug.
        #

        return None