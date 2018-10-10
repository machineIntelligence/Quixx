import numpy as np
from utilityFunctions import *

debug = False

class Quixx:

    '''The Quixx Game Engine'''

    def __init__(self, player1, player2, displayText):
        self.player_names = [player1.name, player2.name]
        self.num_players = 2   #len(playerList) #Hard coded for now
        self.turn_order = range(0, self.num_players)
        self.closed_colors = np.zeros(4).astype(int)
        self.game_not_over = 1
        self.action = 0
        self.dice = roll_dice()
        self.color_options = ['red', 'yellow', 'green', 'blue']
        self.round = 0
        self.red = range(2, 12+1)
        self.yellow = range(2, 12+1)
        self.green = range(12, 2-1, -1)
        self.blue = range(12, 2-1, -1)
        self.list = (self.red, self.yellow, self.green, self.blue)
        self.player = [player1, player2]
        #self.size_state = self.get_size_state()


class Player(Quixx):

    def __init__(self, name):
        self.name = name
        self.scorecard = {'red': np.zeros(12), 'yellow': np.zeros(12), 'green': np.zeros(12), 'blue': np.zeros(12), 'misthrow': np.zeros(4), 'score': int(0), 'right_most_index': np.zeros(4).astype(int)}

    def clear_score_card(self):
        self.scorecard = {'red': np.zeros(12), 'yellow': np.zeros(12), 'green': np.zeros(12), 'blue': np.zeros(12),
                          'misthrow': np.zeros(4), 'score': int(0), 'right_most_index': np.zeros(4).astype(int)}


















