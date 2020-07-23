import os
import json
from colorama import init, Fore
init()


def main():
    show_title()
    show_leaders()
    players = get_players()

    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None]
    ]

    # Get the players and set tokens
    active_player_index = 0

    print(Fore.RED)
    token1 = input(f"{players[0]}, what is your symbol? ")
    print(Fore.YELLOW)
    token2 = input(f"{players[1]}, what is your symbol? ")
    print(Fore.WHITE)

    tokens = [token1, token2]
    player = players[active_player_index]

    while not find_winner(board, player):
        player = players[active_player_index]
        token = tokens[active_player_index]

        announce_turn(player)
        print(Fore.BLUE)
        show_board(board)
        print(Fore.WHITE)

        if check_tie(board):
            print(Fore.CYAN + "The game is a tie" + Fore.WHITE)
            break

        if not choose_column(board, token):
            print(Fore.CYAN + "Sorry, that column is not available! Try again." + Fore.WHITE)
            print()
            continue

        active_player_index = (active_player_index + 1) % len(players)

    show_board(board)
    print()


def show_title():
    print(Fore.WHITE)
    print()
    print(Fore.BLUE + "---------------------------------")
    print("-" + Fore.GREEN + "      CONNECT FOUR V2" + Fore.BLUE + "         -")
    print("-" + Fore.CYAN + "      Now with colors!" + Fore.BLUE + "        -")
    print("---------------------------------" + Fore.WHITE)
    print(Fore.WHITE)
    print()


def show_leaders():
    leaders = load_leaders()
    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)

    print()
    print(Fore.CYAN + "CONNECT 4 LEADERS: " + Fore.WHITE)
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins:,} -- {name}")
    print()
    print("---------------------------")
    print()


def get_players():

    print(Fore.RED)
    player1 = input("Who is Player 1? ")
    print(Fore.YELLOW)
    player2 = input("Who is Player 2? ")
    print(Fore.WHITE)
    players = [player1, player2]
    return players


def choose_column(board, token):
    # Choose a column:
    col = int(input("Choose the column you want to play [1-7]: "))
    print()

    # set the column to the correct index
    col -= 1

    # if column is not available, return false
    if col < 0 or col >= len(board[0]):
        return False

    # Within the chosen column: play the first row:
    row = len(board) - 1

    # the chosen cell is the first row in the chosen column
    cell = board[row][col]

    # if that cell is occupied, add one to the row
    while cell is not None and row >= 0:
        row -= 1
        cell = board[row][col]

    # if all rows in that column are occupied, choose again
    if cell is not None and row < 0:
        return False

    # add a token to the board
    board[row][col] = token
    return True


def show_board(board):
    # Print the columns for ease of choice
    # Maybe find a way to make this modular. ;)
    print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    for row in board:
        print("| ", end='')
        for cell in row:
            token = cell if cell is not None else "_"
            print(token, end=' | ')
        print()


def announce_turn(player):
    print()
    print(Fore.YELLOW + f"It is {player}'s turn!" + Fore.WHITE)
    print()


def find_winner(board, player):
    sequences = winning_sequence(board)

    for cells in sequences:
        token1 = cells[0]
        if token1 and all(token1 == cell for cell in cells):
            print(f"Game over! {player} has won with the board: ")
            add_win(player)
            return True


def winning_sequence(board):
    sequence = []

    # range(len(board[0]) is the number of columns.
    # range(len(board) is the number of rows.
    # when checking the win by rows, we need cols - 3.
    # when checking the win by columns, we need rows - 3.
    # when checking the upward diagonal, both row and column need to be -3.
    # when checking the downward diagonal, column -3 and row is range (3, rows).
    #   that happens because we're adding and subtracting from rows, so they need
    #   to start in the middle

    # Win by rows: 4 in a row
    for c in range(len(board[0]) - 3):
        for r in range(len(board)):
            rows = [[board[r][c], board[r][c + 1], board[r][c + 2], board[r][c + 3]]]
        sequence.extend(rows)

    # Win by columns: 4 in a column
    for c in range(len(board[0])):
        for r in range(len(board) - 3):
            cols = [[board[r][c], board[r + 1][c], board[r + 2][c], board[r + 3][c]]]
        sequence.extend(cols)

    # Win by diagonals: Slope upward
    for c in range(len(board[0]) - 3):
        for r in range(len(board) - 3):
            d1 = [[board[r][c], board[r + 1][c + 1], board[r + 2][c + 2], board[r + 3][c + 3]]]
        sequence.extend(d1)

    # Win by diagonals: Slope downward
    for c in range(len(board[0]) - 3):
        for r in range(3, len(board)):
            d2 = [[board[r][c], board[r - 1][c + 1], board[r - 2][c + 2], board[r - 3][c + 3]]]
        sequence.extend(d2)

    return sequence


def check_tie(board):
    # Checks all elements of all rows to see if any are None/False:
    # If there are no False/None elements in board, the board is full.
    return all(all(row) for row in board)


# function to load the leaderboard
def load_leaders():
    # The folder is the location of this file
    folder = os.path.dirname(__file__)
    # The filename is 'leaderboard.json' and it goes in the folder
    filename = os.path.join(folder, 'leaderboard.json')

    # If the path doesn't exist, return a blank dictionary
    if not os.path.exists(filename):
        return {}

    # Using the file as an input [remember: 'r' is "read"
    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


# function to add leaders to the leaderboard:
def add_win(winner_name):
    # load the leaderboard
    leaders = load_leaders()

    # if the person is already on the board, add one
    if winner_name in leaders:
        leaders[winner_name] += 1

    # otherwise, create their entry and add one
    else:
        leaders[winner_name] = 1

    # set the directory
    folder = os.path.dirname(__file__)
    filename = os.path.join(folder, 'leaderboard.json')

    with open(filename, 'w', encoding='utf-8') as fout:
        return json.dump(leaders, fout)


if __name__ == '__main__':
    main()
