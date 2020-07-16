# Import the random library
import random

# Dictionary key: R/P/S; each key has a dictionary of defeats & defeated by
rolls = {
    'rock': {
        'defeats': ['scissors'],
        'defeated by': ['paper']
    },
    'paper': {
        'defeats': ['rock'],
        'defeated by': ['scissors']
    },
    'scissors': {
        'defeats': ['paper'],
        'defeated by': ['rock']
    }
}


def main():
    show_header()

    play_game(input("What is your name? "), "Computer")


# Define a function that prints the header:
def show_header():
    # Introduce the game
    print("-------------------------------")
    print("-   Rock Paper Scissors v2    -")
    print("-   Data Structures Edition   -")
    print("-------------------------------")


# The function that plays the game
def play_game(player_1, player_2):
    # Create a dictionary containing each player's wins
    wins = {player_1: 0, player_2: 0}
    # Establish the valid rolls
    roll_names = list(rolls.keys())

    # Set up the rounds
    while not find_winner(wins, wins.keys()):
        # Get the rolls from the player and the computer by calling the get_roll function
        roll1 = get_roll(player_1, roll_names)
        roll2 = random.choice(roll_names)

        if not roll1:
            continue

        # Show player rolls
        print(f"{player_1} rolls {roll1}.")
        print(f"{player_2} rolls {roll2}.")

        winner = check_for_winning_roll(player_1, player_2, roll1, roll2)

        if winner is None:
            print("It was a tie!")
        else:
            print(f'{winner} won the round!')
            print()
            wins[winner] += 1

        print(f"Score is {player_1}: {wins[player_1]} and {player_2}: {wins[player_2]}.")
        print()

    overall_winner = find_winner(wins, wins.keys())
    print(f"{overall_winner} won the game!")


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name
    return None


# The function that checks for the winning roll
def check_for_winning_roll(player_1, player_2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("The play was tied!")

    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        return player_1
    elif roll2 in outcome.get('defeated by'):
        return player_2

    return winner


# The function that gets the roll
def get_roll(player_name, roll_names):
    print("Available rolls: ")
    for index, r in enumerate(roll_names, start=1):
        print(f"{index}. {r}")

    text = input(f"{player_name}, what is your roll? ")
    selected_index = int(text) - 1

    # Check for "bad" rolls
    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry, {text} is not a valid play!")
        return None

    return roll_names[selected_index]


if __name__ == '__main__':
    main()
