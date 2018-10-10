import random


def gideon(gameInfo, playerID):
    color, number = random_strategy(gameInfo, playerID)
    return color, number


def nimaOptimus1(gameInfo, playerID):
    color, number = random_strategy(gameInfo, playerID)
    return color, number


def random_strategy(gameInfo, playerID):
    color = 'blue'
    number = -1
    if gameInfo.action == 0:
        color = gameInfo.color_options[random.randint(0, 3)]
        number = gameInfo.dice['white1'] + gameInfo.dice['white2']
    if gameInfo.action == 1:
        color = gameInfo.color_options[random.randint(0, 3)]
        number = gameInfo.dice['white1'] + gameInfo.dice[color]

    return color, number

