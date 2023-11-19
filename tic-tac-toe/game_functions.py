def open_game():
    """The function defines the opening of the game and create the board and counter and flag"""
    board = [["-" for _ in range(3)] for _ in range(3)]
    counter = 0
    return board, counter, True

def update_board(board, player_now, row, column):
    """This function updates the game board, according to the user's turn"""
    board[row][column] = player_now
    print_board(board)

def test_input(board, player_now):
    """
    This function testing if the input is valid
    :param board:
    :return:
    """
    print("Player %s, it's your turn!" % player_now)
    while True:
        row_number = int(input("Please enter the row:")) - 1
        column_number = int(input("Please enter the column:")) - 1
        if (str(row_number) in "012") and (str(column_number) in "012"):
            if board[row_number][column_number] == "-":
                break
            else:
                print('your input is not valid')
        else:
            print('your input is not valid')
    return row_number, column_number

def completed_challenge(board, player_now, counter):
    """
    This function testing if the player has completed the challenge
    :param counter:
    :param player_now:
    :param board:
    :return:
    """
    if counter > 3:
        for i in range(3):
            if (board[i][0] == board[i][1] == board[i][2] != "-")\
                    or (board[0][i] == board[1][i] == board[2][i] != "-")\
                    or (board[0][0] == board[1][1] == board[2][2] != "-")\
                    or (board[0][2] == board[1][1] == board[2][0] != "-"):
                print("Well done plyer %s is the winner!!!" % player_now)
                print_board(board)
                return True
    return False

def finish_game(status, counter):
    if status:
        print("the game is finsh!")
        return False
    elif counter == 9:
        print("The game is over because there is no winner in the game")
        return False
    return True

def print_board(board):
    """this function is print the board"""
    for row in board:
        print(' '.join(row))
    return


if __name__ == "__main__":
    pass
