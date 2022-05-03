import json
import operator

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
