import random
words = []


def load_game_data():
    global words
    f = open(r'/home/dc/Concordia/Courses/Comp 6411/Assignment_1/four_letters.txt', 'r')
    for x in f.read().split():
        if '\n' in x:
            new_words = [x.split('\n')]
            words.extend(new_words)
        else:
            words.append(x)


def fetch_random_word():
    return words[random.randint(0, 4029)]