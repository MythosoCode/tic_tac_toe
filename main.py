# The board game tic-tac-toe
# Start a game for two players, X starts followed by O
# To win you need to get three in a row, horizontal, vertical or diagonal
# Enter coordinates as x y, with a space between


def print_board(board):
    loop: int = 1
    grid: str = "---------\n| "
    for item in board:
        grid += item + ' '
        if loop in (3, 6):
            grid += "|\n| "
        loop += 1
    grid += "|\n---------"
    print(grid)


def evaluate(board):
    eval_piece = 'X'
    for i in range(2):
        if (eval_piece == board[0] == board[1] == board[2]) \
                or (eval_piece == board[3] == board[4] == board[5]) \
                or (eval_piece == board[6] == board[7] == board[8]) \
                or (eval_piece == board[0] == board[3] == board[6]) \
                or (eval_piece == board[1] == board[4] == board[7]) \
                or (eval_piece == board[2] == board[5] == board[8]) \
                or (eval_piece == board[0] == board[4] == board[8]) \
                or (eval_piece == board[2] == board[4] == board[6]):
            print(eval_piece, 'wins')
            return True
        eval_piece = 'O'
    if ' ' not in board:
        print('Draw')
        return True
    else:
        return False


def move(board, piece):
    result = False
    while not result:
        new_move = input('{0} - Enter two coordinates, x y, with space between: '.format(piece)).split()  # row, column
        result = False
        if len(new_move) != 2 or new_move[0].isdigit() is False or new_move[1].isdigit() is False:
            print('You should enter two numbers!')
        else:
            i = int(new_move[1]) + 2
            j = int(new_move[0]) - 1
            index = (j * 3 + i) - 3
            if new_move[0] < '1' or new_move[0] > '3' or new_move[1] < '1' or new_move[1] > '3':
                print('Coordinates should be from 1 to 3!')
            elif board[index] not in ('X', 'O'):
                board[index] = piece
                result = True
            else:
                print('This cell is occupied! Choose another one!')
    return


def play():
    # Define variables
    board = []
    done = False
    eval_piece = 'X'

    # Create a list for an empty board
    for _i in range(9):
        board.append(' ')

    # Start the game and continue until X or O has won or there is no empty space left on the board
    while not done:
        print_board(board)

        # check status for a winner or full board
        done = evaluate(board)
        if not done:
            # Ask for next move
            move(board, eval_piece)
            if eval_piece == 'X':
                eval_piece = 'O'
            else:
                eval_piece = 'X'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play()


