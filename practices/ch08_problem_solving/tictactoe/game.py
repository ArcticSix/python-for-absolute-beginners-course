# create the board
# choose an initial player
# until someone wins, check for a winner
#   show the board
#   choose a location, mark it
#   toggle the active player

# game over, active player won!

def main():
    print()
    print("Welcome to TIC TAC TOE by Russell. :)")
    # Create the Board
    # Board is a list of rows
    # Rows are a list of cells
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    # Choose initial symbol:
    active_player_index = 0
    players = [input("Who is Player 1? "), "Computer"]
    symbols = ["X", "O"]
    player = players[active_player_index]

    # UNTIL SOMEONE WINS
    while not find_winner(board):
        # Show the board
        player = players[active_player_index]
        symbol = symbols[active_player_index]

        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That is not an option. Try again.")
            continue

        active_player_index = (active_player_index + 1) % len(players)

    print(f"Game over! {player} has won with the board: ")
    show_board(board)
    print()


def choose_location(board, symbol):
    row = int(input("Choose which row: "))
    col = int(input("Choose which column: "))

    row -= 1
    col -= 1
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[0]):
        return False

    cell = board[row][col]
    if cell is not None:
        return False

    board[row][col] = symbol
    return True


def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f" It's {player}'s turn. Here's the board: ")
    print()


def find_winner(board):
    sequences = get_winning_sequence(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequence(board):
    sequences = []

    # Win by rows
    rows = board
    sequences.extend((rows))

    # Win by cols
    for col_idx in range(0, 3):
        col = [
            board[0][col_idx],
            board[1][col_idx],
            board[2][col_idx]
        ]
        sequences.append(col)

    # Win by diagonals
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    sequences.extend(diagonals)

    return sequences


if __name__ == '__main__':
    main()
