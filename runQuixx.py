from Quixx import *
import numpy as np
from utilityFunctions import *
import matplotlib.pyplot as plt
from strategies import *


def run_quixx(player_list):
    print_details = False
    gameInfo = Quixx(player_list[0], player_list[1], print_details)

    gameInfo.game_not_over = True
    while gameInfo.game_not_over:

        gameInfo.round += 1
        gameInfo.dice = roll_dice()
        new_crosses = 0

        for kk in range(0, 2):
            gameInfo.action = kk
            if gameInfo.game_not_over:
                if print_details:
                    print('*********************************')
                    print('Round', gameInfo.round, ' Action', gameInfo.action)
                    print('*********************************\n')

                for i in range(0, gameInfo.num_players):
                    playerID = gameInfo.turn_order[i]

                    # Ask for player decision from everyone on round 1 or from roller i == 1 on round 2
                    if gameInfo.action == 0 or (gameInfo.action == 1 and i == 0):

                        (color, number) = player_decision(gameInfo, playerID)
                        valid_selection = is_valid_choice(playerID, gameInfo, color, number)
                        if valid_selection:
                            update_card(playerID, gameInfo, color, number)
                            # if its the roller, check to see if crosses were made
                            if i == 0:# the roller has made a selection, update new crosses
                                new_crosses += 1

                        if gameInfo.action == 1:
                            # check for misthrow after roller finishes action 1
                            if new_crosses == 0:
                                mt = int(sum(gameInfo.player[gameInfo.turn_order[0]].scorecard['misthrow']))
                                gameInfo.player[gameInfo.turn_order[0]].scorecard['misthrow'][mt] = 1

                update_closed_colors(gameInfo)

            score_game(gameInfo)
            check_game_over(gameInfo)
        gameInfo.turn_order = [gameInfo.turn_order[1], gameInfo.turn_order[0]]

    if print_details:
        fig, ax = plt.subplots()
        ax.plot(gameInfo.player[0].state_action_pair_list)

        fig, ax = plt.subplots()
        ax.plot(gameInfo.player[0].reward_list)

        fig, ax = plt.subplots()
        ax.plot(gameInfo.player[1].reward_list)

        plt.show()

    if gameInfo.player[0].scorecard['score'] > gameInfo.player[1].scorecard['score']:
        winner = 0
        print(gameInfo.player_names[0] + ' WINS !!!')
    elif gameInfo.player[0].scorecard['score'] < gameInfo.player[1].scorecard['score']:
        print(gameInfo.player_names[1] + ' WINS !!!')
        winner = 1
    else:
        print('TIE!!!')
        winner = -1

    for i in range(0, gameInfo.num_players):
        print('Player ' + gameInfo.player_names[i] + ' has ' + str(gameInfo.player[i].scorecard['score']) + ' points ')

    for i in range(0, gameInfo.num_players):
        gameInfo.player[i].clear_score_card()

    return winner, gameInfo


def player_decision(gameInfo, playerID):
    func_name = gameInfo.player_names[playerID]
    arg_list = '(gameInfo, playerID)'

    try:
        (color, number) = eval(func_name + arg_list)
        return color, number

    except ValueError:
        print("No player function for player " + gameInfo.player_names[playerID] + " found")

