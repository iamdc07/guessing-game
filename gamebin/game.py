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
game_id = 0
count = 0


def modify_score(user_input, status, user_guess, current_guess):
    global letter_frequency
    global game_data
    global game_id
    global count

    if user_input == 't':
        current_word = game_data[game_id]['word']
        score = game_data[game_id]['score']

        index = 0
        for eachLetter in current_guess:
            if eachLetter == '-':
                letter = current_word[index]
                points = letter_frequency[letter]
                score -= points
                index += 1

        if count > 0:
            score = score / count

        game_data[game_id]['score'] = score
        game_data[game_id]['status'] = 'Gave up'
    elif user_input == 'g':
        current_word = game_data[game_id]['word']
        score = game_data[game_id]['score']
        bad_guesses = game_data[game_id]['bad_guesses']
        index = 0

        if status:
            for eachLetter in current_guess:
                if eachLetter == '-':
                    letter = current_word[index]
                    points = letter_frequency[letter]
                    score += points
                    index += 1

            game_data[game_id]['score'] = score
            game_data[game_id]['status'] = 'Success'
        else:
            score -= (score * 0.1)
            bad_guesses += 1
            game_data[game_id]['bad_guesses'] = bad_guesses
            game_data[game_id]['score'] = score
    elif user_input == 'l':
        count += 1
        score = game_data[game_id]['score']
        missed_letters = game_data[game_id]['missed_letters']

        if status:
            points = letter_frequency[user_guess]
            score += points
        else:
            score -= (score * 0.1)
            missed_letters += 1
            game_data[game_id]['missed_letters'] = missed_letters

        if current_guess.find('-') != -1:
            score = score / 10
            game_data[game_id]['status'] = "Success"

        game_data[game_id]['score'] = score


def create_scoreboard(current_word):
    global game_data
    global game_id
    global count
    count = 0
    game_id += 1
    game_data[game_id] = {}
    game_data[game_id]['word'] = current_word
    game_data[game_id]['status'] = ''
    game_data[game_id]['bad_guesses'] = 0
    game_data[game_id]['missed_letters'] = 0
    game_data[game_id]['score'] = 0


def display_scoreboard():
    global game_data
    final_score = 0
    print("\n\nGame\t" + "Word" + "\tStatus" + "\tBad Guesses" + "\tMissed Letters" + "\tScore")
    print("----\t----\t------\t-----------\t--------------\t-----")

    for key, value in game_data.items():
        if value['status'] != '':
            line = "{}\t{}\t{}\t{}\t\t{}\t\t{}".format(key, value['word'], value['status'], value['bad_guesses'],
                                                       value['missed_letters'], value['score'])
            final_score += value['score']
            print(line)

    print('\nFinal score: ', final_score)
