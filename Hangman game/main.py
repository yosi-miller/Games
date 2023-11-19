from Hangman_functions import *

def game():
    """This function runs the game"""

    # This is the opening screen of the game
    open_game()

    # and receives address file and number index
    file, index = file_open()

    # here receives the word to the game
    word_game = choose_word(file, index)

    # Counts the number of game attempts
    counter = 0

    border = create_border(word_game)

    old_letter_guessed = []

    # This is where the gameplay takes place
    win = False
    while not win:

        # this print status of hangman
        print_hangman(counter)

        flag1 = True
        while flag1:

            # check if is ok letter and not in the border
            letter_guessed, old_letter_guessed = check_valid_input(old_letter_guessed)

            # check if a letter in the choose word
            status_letter = try_update_letter_guessed(letter_guessed, word_game)

            # if a letter not in the choose word and not in the border, update the border
            border, flag1 = show_hidden_word(status_letter, letter_guessed, border, word_game)

            flag1 = border_full(border)

        counter += 1

        win = check_win(counter, border)


if __name__ == "__main__":
    game()