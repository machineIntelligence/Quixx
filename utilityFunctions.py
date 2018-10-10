import random
import numpy as np
from Quixx import *

debug = False
switch = {
        'red': 1,
        'yellow': 2,
        'green': 3,
        'blue': 4
    }


def roll_dice():
    red = random.randint(1, 6)
    yellow = random.randint(1, 6)
    green = random.randint(1, 6)
    blue = random.randint(1, 6)
    white1 = random.randint(1, 6)
    white2 = random.randint(1, 6)
    roll = {'red': red, 'yellow': yellow, 'green': green, 'blue': blue, 'white1': white1, 'white2': white2}
    return roll


# this is done in player class init now, can be removed
def init_score_card():
    red = np.zeros(12)
    yellow = np.zeros(12)
    green = np.zeros(12)
    blue = np.zeros(12)
    misthrow = np.zeros(4)
    score = 0
    right_most_index = np.zeros(4).astype(int)
    return [red, yellow, green, blue,
            misthrow, score, right_most_index]


def is_valid_choice(playerID, gameInfo, color, number):
    valid = True
    not_valid = False

    if number == -1:
        if debug:
            print('Misthrow')
        return not_valid

    if number < 2 or number > 12:
        if debug:
            print(number)
            print('value not in range')
        return not_valid

    if gameInfo.closed_colors[switch.get(color)-1]:
        if debug:
            print('Color ' + str(switch.get(color)-1) + 'is closed')
        return not_valid

    if gameInfo.action == 0:
        if number != gameInfo.dice['white1'] + gameInfo.dice['white2']: # These are the two white dice
            if debug:
                print('Value not the sum of the two white dice')
                print('{Player = ' + str(gameInfo.player_names[playerID]))
                print('Dice = ' + str(gameInfo.dice))
            return not_valid

    if gameInfo.action == 1 and gameInfo.turn_order == 0:
        possible_value1 = gameInfo.dice[color] + gameInfo.dice['white1']
        possible_value2 = gameInfo.dice[color] + gameInfo.dice['white2']
        if number != possible_value1 and number != possible_value2:
            if debug:
                print('Value not the sum of a color and a white die')
                print('{Player = ' + str(gameInfo.player_names[playerID]))
                print('Dice = ' + str(gameInfo.dice))
                print('Color = ' + str(color))
                print('possible value 1 = ' + str(possible_value1))
                print('possible value 2 = ' + str(possible_value2))
                print('number = ' + str(number))
            return not_valid

    # -1 to account for zero based indexing. Red above starts at 1, but is zeroth index of the array
    index_rmc = gameInfo.player[playerID].scorecard['right_most_index'][switch.get(color)-1]
    index_of_number = get_index_of_number(color, number)
    if index_rmc >= index_of_number:
        if debug:
            print('number is marked or there exists a cross to the right')
        return not_valid

    if index_of_number == 10:
        num_crosses_to_left_of_value = sum(gameInfo.player[playerID].scorecard[color])
        if num_crosses_to_left_of_value < 5:
            if debug:
                print('Closing number but < 5 crosses')
            return not_valid

    return valid


def get_index_of_number(color, number):
        if color == 'red':
            index = number - 2
        elif color == 'yellow':
            index = number - 2
        else:
            index = abs(number - 12)
        return index


def update_card(playerID, gameInfo, color, number):
        index_of_number = get_index_of_number(color, number)
        # if allowed to close numbers by selecting last index, give the bonus and lock the row
        if index_of_number == 10:
            gameInfo.player[playerID].scorecard[color][index_of_number] = 1
            gameInfo.player[playerID].scorecard[color][index_of_number + 1] = 1
            gameInfo.player[playerID].scorecard['right_most_index'][switch.get(color)-1] = index_of_number + 1
        else:
            gameInfo.player[playerID].scorecard[color][index_of_number] = 1
            gameInfo.player[playerID].scorecard['right_most_index'][switch.get(color)-1] = index_of_number

        return


def update_closed_colors(gameInfo):
    # check rows for locked state (idx == 11)
    gameInfo.closed_colors = np.zeros(4).astype(int)
    for i in range(0, gameInfo.num_players):
        if gameInfo.player[i].scorecard['red'][11] == 1:
            gameInfo.closed_colors[0] = 1
        if gameInfo.player[i].scorecard['yellow'][11] == 1:
            gameInfo.closed_colors[1] = 1
        if gameInfo.player[i].scorecard['green'][11] == 1:
            gameInfo.closed_colors[2] = 1
        if gameInfo.player[i].scorecard['blue'][11] == 1:
            gameInfo.closed_colors[3] = 1


def score_game(gameInfo):
    for i in range(0, gameInfo.num_players):
        temp = 0
        temp = temp + crosses_to_points(sum(gameInfo.player[i].scorecard['red']))
        temp = temp + crosses_to_points(sum(gameInfo.player[i].scorecard['yellow']))
        temp = temp + crosses_to_points(sum(gameInfo.player[i].scorecard['green']))
        temp = temp + crosses_to_points(sum(gameInfo.player[i].scorecard['blue']))
        gameInfo.player[i].scorecard['score'] = int(temp)


def crosses_to_points(num_crosses):

    points = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]
    if num_crosses > len(points) or num_crosses < 0:
        num_points = 0
    else:
        num_points = points[int(num_crosses)]
        #print(num_crosses)
    return num_points


def check_game_over(gameInfo):
    for i in range(0, gameInfo.num_players):
        if debug:
            print('Miisthrows for player ' + str(i))
            print(gameInfo.player[i].scorecard['misthrow'])
        # too many misthrows
        if sum(gameInfo.player[i].scorecard['misthrow']) == 4:
            gameInfo.game_not_over = False

    if sum(gameInfo.closed_colors) >= 2:
        gameInfo.game_not_over = False

    return


































