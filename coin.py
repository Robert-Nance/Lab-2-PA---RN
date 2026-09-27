
"""coin.py, Robert Nance, flips a coin, Lab 2 Programming Assignment Page, 09/27/2026"""

import random

class Coin:
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        flipped_side = random.randint(0, 1)

        if flipped_side == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def this_sideup(self):
        return self.__sideup