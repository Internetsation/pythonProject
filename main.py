# This is a simple version of tic-tac-toe.
# The computer plays "X's", User plays "O's".
# Each game begins with computer playing X in the middle square.
# Each square is numbered by row starting with 1.
# The user can only play on squares that contain a corresponding number
# The game ends with a win, loss or tie.

# Import random function for computer moves
from random import randrange


# Creates the game board
def create_board():
    global current_player
    board = [['' for x in range(3)] for i in range(3)]
    pos = 1
    for row in range(3):
        for column in range(3):
            board[row][column] = pos
            pos += 1

    board[1][1] = 'X'
    current_player = 'O'
    return board


# Displays a visual of the game board for the user
def display_board(board):
    print('+-------' * 3, '+', sep='')
    for row in range(3):
        print('|       ' * 3, '|', sep='')
        for col in range(3):
            print('|  ', str(board[row][col]) + '   ', end='')
        print('|')
        print('|       ' * 3, '|', sep='')
        print('+-------' * 3, '+', sep='')


# Allows the user to take their turn
def enter_move(board):
    turn_ok = False

    while not turn_ok:
        move = input('Enter the number of the box you want to mark with your O: ')

        if len(move) != 1 or move <= '0' or move > '9':
            print("Invalid move. Try again.")
            continue

        move = int(move) - 10
        row = move // 3
        col = move % 3

        if board[row][col] in ['O', 'X']:
            print("Invalid move. Try again.")
            continue

        turn_ok = not turn_ok
        board[row][col] = 'O'


# Defines the play area on the board
def make_list_of_free_fields(board):
    free_squares = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['O', 'X']:
                free_squares.append((row, column))
    return free_squares


# Places the computers "random" X
def draw_move(board):
    free_squares = make_list_of_free_fields(board)

    free_squares_length = len(free_squares)
    if free_squares_length > 0:
        random = randrange(free_squares_length)
        row, col = free_squares[random]
        board[row][col] = 'X'


# Checks for a winner
def victory_for(board, sign):
    # check rows
    for row in range(3):
        if board[row][0] == sign and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            return sign

    # check columns
    for column in range(3):
        if board[0][column] == sign and board[0][column] == board[1][column] and board[0][column] == board[2][column]:
            return sign

        # check diagonals
        if board[0][0] == sign and board[0][0] == board[1][1] and board[1][1] == board[2][2] or \
                board[0][2] == sign and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return sign

        return None


# Starts the game
def start_the_game():
    game_start = '0'
    while game_start != '1':
        game_start = input('To play\nTic-Tac-Toe\nEnter 0 to start or 1 to quit: ')

        if type(game_start) != "<class 'str'>" and game_start not in ['0', '1']:
            print('\nPlease reread the instructions:\n')
            continue

        if game_start == '1':
            print('\nGoodbye quitter!\n')
            break

        # main program
        board = create_board()
        play(board)
        display_board(board)

        if winner is not None:
            print('\nCongratulations! You won!\n')

        else:
            print('Tie game !')


# initiates a round of play
def play(board):
    free_squares = len(make_list_of_free_fields(board))
    global winner
    global current_player

    while free_squares != 0:
        display_board(board)

        if current_player == 'O':
            # User turn
            enter_move(board)
        else:
            # computer turn
            draw_move(board)

        game_winner = victory_for(board, current_player)

        if game_winner is not None:
            winner = game_winner
            break
        else:
            if current_player == 'O':
                current_player = 'X'
            else:
                current_player = 'O'

        free_squares = len(make_list_of_free_fields(board))


start_the_game()
