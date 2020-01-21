def init_board():  # Bende
    """Returns an empty 3-by-3 board (with zeros)."""
    board = []
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append(0)
    return board


def get_move(board, player):  # Bence
    """Returns the coordinates of a valid move for player on board."""
    col, row = 0, 0
    valid_letters = ['A', 'B', "C"]
    next_move = False
    while next_move is False:
        try:
            coordinates = input('Specify a coordinate: ').upper()
            col = int(coordinates[1])-1

            for i in range(len(valid_letters)):
                if coordinates[0] == valid_letters[i]:
                    row = i

            if board[row][col] == 0 and 0 <= col < 4 and coordinates[0] in valid_letters:
                next_move = True
        except IndexError:
            next_move = False
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):  # Bence
    """Marks the element at row & col on the board for player."""
    try:
        board[row][col] = player
    except:
        pass
    return board


def has_won(board, player):  # Bende
    """Returns True if player has won the game."""

    rArr = []
    lArr = []
    for i in range(len(board)):
        rowArr = []
        colArr = []
        lArr.append(board[i][i])

        for j in range(len(board[i])):
            rowArr.append(board[i][j])
            colArr.append(board[j][i])
            if i + j == 2:
                rArr.append(board[i][j])

        print_result(rowArr,board)
        print_result(colArr,board)

        print(str(rowArr) + "     " + str(colArr))
        print()

    print_result(lArr,board)  # bal atlo
    print_result(rArr,board)  # jobb atlo


def is_full():
    """Returns True if board is full."""
    print("The board is full - it is a draw")
    exit()


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    a = ""
    abc = ["A ", "B ", "C "]
    counter = 0

    print("   1   2   3\n")
    for i in board:
        a += abc[counter]
        for j in i:
            a += f" {j} |"
        a = a[:-2] + "\n  ---+---+---\n"
        counter += 1
    a = a.replace("0", ".")[:-15]
    print(a)


def print_result(arrAy,board):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if "0" not in arrAy:
        if "X" not in arrAy:
            print_board(board)
            print("O Nyert!")
            exit()
        elif "O" not in arrAy:
            print_board(board)
            print("X Nyert!")
            exit()

def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    player = 'X'


    for i in range(9):
        # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic

        print_board(board)
        row, col = get_move(board, player)
        mark(board, player, row, col)

        if i > 3:
            has_won(board,player)


        # print(is_full(board))

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    is_full()

def main_menu():
    tictactoe_game('HUMAN-HUMAN')
    # board1 = init_board()
    # print_board(board1)
    # row, col = get_move(board1, "X")
    # mark(board1, "X", row, col)
    # print_board(board1)


if __name__ == '__main__':
    main_menu()
