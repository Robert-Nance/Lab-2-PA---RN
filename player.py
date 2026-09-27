
from coin import Coin

class Player:
    def __init__(self, name):
        self.__player_name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        self.__coin.toss()

    def get_coin(self):
        return self.__coin.this_sideup()

    def win(self):
        self.__wallet += 1

    def lose(self):
        self.__wallet -= 1

    def get_wallet(self):
        return self.__wallet

    def get_name(self):
        return self.__player_name