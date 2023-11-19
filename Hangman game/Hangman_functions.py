def open_game():
    """This is the opening screen of the game"""
    HANGMAN_ASCII_ART = """
    welcome to the hangman game
     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |
                        |___/"""
    MAX_TRIES = "for any player has 6 attempts ☺️"
    print(f"{HANGMAN_ASCII_ART}\n {MAX_TRIES}")

def file_open():
    """
    This function receives the address of the file and the index of the word
    :return: address file and index of the secret word
    """
    file = input("Please enter a file path:")
    index = int(input("Please Enter index:"))
    return file, index


def choose_word(file_path, index):
    """this function return the word of game
    :param file_path: str
    :param index: int
    :return: word"""
    with open(file_path, "r") as file:
        c = file.read().split(" ")
    return c[(index - 1) % len(c)]

def print_hangman(num_of_tries):
    """
    This function prints the hangman status according to the number of attempts
    :param num_of_tries: num of tries value
    :return: hangman status
    """
    HANGMAN_PHOTOS = {  # picture 1
        0: "x-------x",
        # picture 2
        1: """x-------x\n|\n|\n|\n|\n|""",
        # picture 3
        2: """x-------x\n|\t\t|\n|\t\t0\n|\n|\n|""",
        # picture 4
        3: """x-------x\n|\t\t|\n|\t\t0\n|\t\t|\n|\n|""",
        # picture 5
        4: """x-------x\n|\t\t|\n|\t\t0\n|      /|\\\n|\n|""",
        # picture 6
        5: """x-------x\n|\t\t|\n|\t\t0\n|      /|\\\n|      /\n|""",
        # picture 7
        6: """x-------x\n|\t\t|\n|\t\t0\n|      /|\\\n|      / \\\n|"""}
    print(HANGMAN_PHOTOS[num_of_tries])
    return

def create_border(word_game):
    """
    This function creates a border for the word
    :param word_game: word game value
    :return: border
    """
    print("you have a word in -", len(word_game), "letter")
    return ["_" for i in range(len(word_game))]

def check_valid_input(old_letters_guessed):
    """
    The function checks if the letter is valid and if it is not in the list of letters that have already been guessed
    :param letter_guessed: letter_guessed value
    :param old_letters_guessed: old_letters_guessed value
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True or False
    :rtype: bool
    """
    while True:
        letter_guessed = input("please enter a letter")
        only_letter = letter_guessed.isalpha()
        if_in = letter_guessed.lower() not in old_letters_guessed
        if if_in and only_letter and (len(letter_guessed) == 1):
            old_letters_guessed.append(letter_guessed)
            return letter_guessed, old_letters_guessed
        else:
            print("X," + " -> ".join(sorted(old_letters_guessed)))

def try_update_letter_guessed(letter_guessed, word_game):
    """
    testing if a letter in the choose word
    :param letter_guessed: letter_guessed value
    :param word_game: word_game value
    :return: True or False
    :rtype: bool
    """
    if letter_guessed in word_game:
        return True
    else:
        return False

def show_hidden_word(status_letter, letter_guessed, border, word_game):
    """
    This function prints the word with the letters that have already been guessed
    :param status_letter: The status of the letter in the word
    :param letter_guessed: the letter that the player guessed
    :param border: border game
    :param word_game: The word the player must guess
    :return: border and True or False
    """
    if status_letter:
        for i in range(len(word_game)):
            if word_game[i] == letter_guessed:
                border[i] = letter_guessed
        print(" ".join(border))
        return border, True
    else:
        print("😒😒😒")
        return border, False

def check_win(counter, border):
    """
    This function checks if the player has won or lost
    :param counter: Number of attempts the player has played
    :param border: The word with the letters that have already been guessed
    :return: True or False
    :rtype: bool
    """
    if "_" not in border:
        print("You Win")
        return True
    elif counter == 6:
        print("LOSE")
        return True

def border_full(border):
    """
    This function checks if the border is full
    :param border: border game
    :return: True or False
    """
    if "_" not in border:
        return False
    return True

if __name__ == "__main__":
    pass