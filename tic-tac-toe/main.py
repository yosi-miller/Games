# import game_functions as my
from game_functions import *

def run_game():
    print("hello: player 1 is 'O', player 2 is 'X'")
    player_now, player_later = "O", "X"

    board, counter, flag = open_game()
    while flag:

        # step 1: input the number of row and column, and testing if the input is valid
        row_number, column_number = test_input(board, player_now)

        # step 2: will now update the game board
        update_board(board, player_now, row_number, column_number)

        # step 3: now testing If the player has completed the challenge
        status = completed_challenge(board, player_now, counter)

        # step 4: this testing if the game is finsh
        counter += 1
        flag = finish_game(status, counter)

        # step 5: this replaces the player's turn
        player_now, player_later = player_later, player_now


run_game()

# "9 - פונקציה שקולטת שם מהשחקנים 7 - שגיות: שלא מוקש מספר, להדפיס הוראות שימוש, להדפיס את הלוח בהתחלה. 6 - לכתוב תיאור לפונקציות, 7 - לסדר פונקציה בדיקה של הקלט
