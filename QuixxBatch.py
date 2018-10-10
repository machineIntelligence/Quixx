from Quixx import *
from runQuixx import run_quixx
import numpy as np
import matplotlib.pyplot as plt


def main():
    player1 = Player('gideon')
    player2 = Player('nimaOptimus1')
    player_list = [player1, player2]
    num_games = 10
    num_ties = 0

    if num_games == 1:
        display_text = True
    else:
        display_text = False

    num_wins = np.zeros(len(player_list))

    for j in range(0, num_games):
        print(j)
        winner, game_info = run_quixx(player_list)

        # didn't result in a tie
        if winner != -1:
            num_wins[winner] += 1
        else:
            num_ties += 1

    # This is the final tally at the end of all the games
    print('num wins = ' + str(num_wins))
    print('num ties = ' + str(num_ties))
    labels = player1.name, player2.name
    explode = (0, .05)
    plt.pie(num_wins, explode=explode, labels=labels)
    plt.show()
    return


if __name__ == '__main__':
    main()
