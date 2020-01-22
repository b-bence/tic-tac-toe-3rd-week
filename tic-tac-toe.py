from os import system
import random


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
            coordinates = input(f'\n{player}: Specify a coordinate: ').upper()
            system("clear")
            print_board(board)
            if coordinates == 'QUIT':
                exit()

            col = int(coordinates[1])-1

            for i in range(len(valid_letters)):
                if coordinates[0] == valid_letters[i]:
                    row = i

            if board[row][col] == 0 and 0 <= col < 4 and coordinates[0] in valid_letters:
                next_move = True
        except (ValueError, IndexError):
            next_move = False
            system("clear")
            print_board(board)
    return row, col


def get_ai_move(board):
    """Returns the coordinates of a valid move for player on board."""
    system("clear")
    row, col = 0, 0
    go = False
    while go is False:
        row = random.randrange(0, 3)
        col = random.randrange(0, 3)
        if board[row][col] == 0:
            go = True

    return row, col


def mark(board, player, row, col):  # Bence
    """Marks the element at row & col on the board for player."""
    board[row][col] = player
    return board


def has_won(board, player):  # Bende
    """Returns True if player has won the game."""

    rArr = []
    lArr = []
    for i in range(len(board)):
        colArr = []
        lArr.append(board[i][i])

        for j in range(len(board[i])):
            colArr.append(board[j][i])
            if i + j == 2:
                rArr.append(board[i][j])

        print_result(board[i], board)
        print_result(colArr, board)

    print_result(lArr, board)  # bal atlo
    print_result(rArr, board)  # jobb atlo


def is_full(board):
    """Returns True if board is full."""
    print_board(board)
    print("\nIt's a tie!")
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


def print_result(arrAy, board):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if 0 not in arrAy:
        system("clear")
        if "X" not in arrAy:
            print_board(board)
            print("\nO Won!")
            exit()
        elif "O" not in arrAy:
            print_board(board)
            print("\nX Won!")
            exit()


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    player = 'X'

    for i in range(9):
        system("clear")
        print_board(board)
        if mode == 'HUMAN-HUMAN':
            row, col = get_move(board, player)
        elif mode == 'HUMAN-AI':
            if i % 2 != 0:
                row, col = get_ai_move(board)
            elif i % 2 == 0:
                row, col = get_move(board, player)
        elif mode == 'AI-HUMAN':
            if i % 2 == 0:
                row, col = get_ai_move(board)
            elif i % 2 != 0:
                row, col = get_move(board, player)
        mark(board, player, row, col)
        if i > 3:
            has_won(board, player)
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    is_full(board)


def main_menu():
    tictactoe_game('AI-HUMAN')


if __name__ == '__main__':
    main_menu()
