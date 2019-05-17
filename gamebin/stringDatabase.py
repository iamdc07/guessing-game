import random
words = []


def load_game_data():
    """
    Load the words into the python script and store it in a data structure
    """
    global words
    f = open(r'four_letters.txt', 'r')
    for x in f.read().split():
        if '\n' in x:
            new_words = [x.split('\n')]
            words.extend(new_words)
        else:
            words.append(x)


def fetch_random_word():
    """
    Get a random word from the word pool
    """
    return words[random.randint(0, 4029)]