import stringDatabase as dB
import sys

dB.load_game_data()


def start_game():
    print("\n")
    print("*** Guessing Game ***")
    display_ui()


def display_ui(random_word=None, guess="----"):
    if random_word is None and guess == "----":
        random_word = dB.fetch_random_word()

    print("\nCurrent Guess: ", random_word)
    print("Current Guess: ", guess)

    user_input = input("\nWhat you'd like to do? g = guess, t = tell me, l for guess a letter, and q to quit\n")

    if user_input.lower() == 'q':
        # Display the scoreboard
        sys.exit()
    elif user_input.lower() == 't':
        print("\nBetter luck next time!!")
        print("Word: ", random_word)
    elif user_input.lower() == 'l':
        user_guess = input("\nEnter your guess: ")
        guess = check_letter_guess(guess, user_guess, random_word)

        if guess.find('-') == -1:
            print("\nGood guess, genius!")
            print("The word was ", guess)
            print("-----------------------")
            display_ui()
        else:
            display_ui(random_word, guess)
    elif user_input.lower() == 'g':
        user_guess = input("\nEnter your guess: ")
        check_word_guess(user_guess, random_word)
    else:
        print("\nWrong input, Try again!")
        print("-----------------------")
        display_ui(random_word)

    display_ui(guess=guess)


def check_word_guess(user_guess, current_word):
    if user_guess == current_word:
        print("\nGood guess, genius!")
        print("The word was ", current_word)
        print("-----------------------")
    else:
        print("\nHaha, You thought you had that! :P")
        print("The word was ", current_word)
        print("-----------------------")


def check_letter_guess(current_guess, user_guess, current_word):
    word = ''
    index = 0
    count = 0

    if current_guess.find(user_guess) != -1:
        print("You have already guessed the letter!")
        return current_guess
    elif current_word.find(user_guess) == -1:
        print("Wrong guess, no such letter!")
        return current_guess
    else:
        for eachLetter in current_guess:
            if eachLetter == '-':
                if user_guess == current_word[index]:
                    word += user_guess
                    count += 1
                else:
                    word += '-'
            else:
                word += eachLetter
            index += 1
        print("You have found ", count, " letters")

    return word


if __name__ == '__main__':
    start_game()
