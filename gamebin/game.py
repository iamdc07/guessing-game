letter_frequency = {
    "a": 8.17,
    "b": 1.49,
    "c": 2.78,
    "d": 4.25,
    "e": 12.70,
    "f": 2.23,
    "g": 2.02,
    "h": 6.09,
    "i": 6.97,
    "j": 0.15,
    "k": 0.77,
    "l": 4.03,
    "m": 2.41,
    "n": 6.75,
    "o": 7.51,
    "p": 1.93,
    "q": 0.10,
    "r": 5.99,
    "s": 6.33,
    "t": 9.06,
    "u": 2.76,
    "v": 0.98,
    "w": 2.36,
    "x": 0.15,
    "y": 1.97,
    "z": 0.07,
}

game_data = {}
round_score = 0
gameid = 0


def modify_score(user_input, status, user_guess, current_guess):
    global letter_frequency
    global game_data
    global gameid

    if user_input == 't':
        current_word = game_data[gameid]['word']
        score = game_data[gameid]['score']

        index = 0
        for eachLetter in current_guess:
            if eachLetter == '-':
                letter = current_word[index]
                points = letter_frequency[letter]
                score -= points
                index += 1

        game_data[gameid]['score'] = score
        game_data[gameid]['status'] = 'Gave up'
    elif user_input == 'g':
        current_word = game_data[gameid]['word']
        score = game_data[gameid]['score']
        bad_guesses = game_data[gameid]['bad_guesses']
        index = 0

        if status:
            for eachLetter in current_guess:
                if eachLetter == '-':
                    letter = current_word[index]
                    points = letter_frequency[letter]
                    score += points
                    index += 1

            game_data[gameid]['score'] = score
            game_data[gameid]['status'] = 'Success'
        else:
            score -= (score * 0.1)
            bad_guesses += 1
            game_data[gameid]['bad_guesses'] = bad_guesses
            game_data[gameid]['score'] = score
    elif user_input == 'l':
        score = game_data[gameid]['score']
        missed_letters = game_data[gameid]['missed_letters']

        if status:
            points = letter_frequency[user_guess]
            score += points
            game_data[gameid]['score'] = score
        else:
            score -= (score * 0.1)
            missed_letters += 1
            game_data[gameid]['missed_letters'] = missed_letters
            game_data[gameid]['score'] = score


def create_scoreboard(current_word):
    global game_data
    global gameid
    gameid += 1
    game_data[gameid] = {}
    game_data[gameid]['word'] = current_word
    game_data[gameid]['status'] = ''
    game_data[gameid]['bad_guesses'] = 0
    game_data[gameid]['missed_letters'] = 0
    game_data[gameid]['score'] = 0


def display_scoreboard():
    global game_data
    sum = 0
    print("\n\nGame\t" + "Word" + "\tStatus" + "\tBad Guesses" + "\tMissed Letters" + "\tScore")
    print("----\t----\t------\t-----------\t--------------\t-----")

    for key, value in game_data.items():
        if value['status'] != '':
            line = "{}\t{}\t{}\t{}\t\t{}\t\t{}".format(key, value['word'], value['status'], value['bad_guesses'],
                                                       value['missed_letters'], value['score'])
            sum += value['score']
            print(line)

    print('\nFinal score: ', sum)
