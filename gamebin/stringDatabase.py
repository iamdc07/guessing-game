words = []


def create_game_data():
    global words
    f = open(r'/home/dc/Concordia/Courses/Comp 6411/Assignment_1/four_letters.txt', 'r')
    for x in f.read().split():
        if x.__contains__('\n'):
            new_words = [x.split('\n')]
            words.extend(new_words)
        else:
            words.append(x)

