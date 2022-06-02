import json
import pickle
import operator
import os

from game.player import Player

score = {}


def load_score():
    global score
    with open("../data/score.json", "r") as read_file:
        score = json.load(read_file)
    sort_score()
    return score


def save_score():
    global score
    with open("../data/score.json", "w") as read_file:
        json.dump(score, read_file)


def add_to_score(name, added_score):
    global score
    score.setdefault(name, added_score)


def sort_score():
    global score
    sorted_tuples = sorted(score.items(), key=operator.itemgetter(1))
    sorted_tuples.reverse()
    score = {k: v for k, v in sorted_tuples}


def load_data():
    with open("../data/data.json", "r") as read_file:
        return json.load(read_file)


def load_player_data(player):
    if os.path.exists(f"../data/player-meta-{player}.pickle"):
        with open(f"../data/player-meta-{player}.pickle", "rb") as read_file:
            return pickle.load(read_file)
    else:
        return Player(player)


def save_player_data(player):
    with open(f"../data/player-meta-{player.name}.pickle", "wb") as read_file:
        return pickle.dump(player, read_file)
