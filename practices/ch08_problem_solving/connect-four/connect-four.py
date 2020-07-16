# 0. set main and title
# 1. get the players
# 2. show the board
# 3. choose a first player
# 4. check for a winner until someone wins
# 4.1 check rows
# 4.2 check columns
# 4.3 check diagonals
# 5. mark the location chosen
# 5.1. only need to choose a column; can't exceed top row
# 6. switch the active player
# 7. todo: in case of a tie


def main():
    show_title()

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
    players = [input("Who is Player 1? "), input("Who is Player 2? ")]
    tokens = ["X", "O"]
    player = players[active_player_index]

    while not find_winner(board, player):
        player = players[active_player_index]
        token = tokens[active_player_index]

        announce_turn(player)
        show_board(board)

        if check_tie(board):
            print("The game is a tie")
            break

        if not choose_column(board, token):
            print("Sorry, that column is not available! Try again.")
            print()
            continue

        active_player_index = (active_player_index + 1) % len(players)

    show_board(board)
    print()


def show_title():
    print()
    print("---------------------------------")
    print("-        CONNECT FOUR V1        -")
    print("---------------------------------")
    print()


def choose_column(board, token):
    # Choose a column:
    col = int(input("Choose the column you want to play [1-7]: "))

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
    print(f"It is {player}'s turn!")
    print()


def find_winner(board, player):
    sequences = winning_sequence(board)

    for cells in sequences:
        token1 = cells[0]
        if token1 and all(token1 == cell for cell in cells):
            print(f"Game over! {player} has won with the board: ")
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


if __name__ == '__main__':
    main()
