#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from player import Player
from util import *

# ==========================================
# Player Alphabeta
# ==========================================

class AlphabetaPlayer(Player):

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, symbol):
        super(AlphabetaPlayer, self).__init__(symbol)

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        # TODO Bonus
        return None