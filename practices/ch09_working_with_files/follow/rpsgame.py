import random
import json
import os
import datetime

rolls = {}


def main():
    log("App starting up...")
    load_rolls()
    show_header()
    show_leaders()
    player1, player2 = get_players()
    log(f"{player1} has logged in.")
    play_game(player1, player2)
    log("Game over!")


def show_header():
    print("---------------------------")
    print("    Rock Paper Scissors")
    print("     Modifiable Edition")
    print("---------------------------")


def show_leaders():
    # Call the leader function
    leaders = load_leaders()

    # Sort the leaders by creating a variable that lists the items in the leaderboard
    # Then that list is sorted in descending order
    # Bonus: lambda creates a mini-function
    sorted_leaders = list(leaders.items())
    sorted_leaders.sort(key=lambda l: l[1], reverse=True)

    print()
    print("LEADERS: ")
    for name, wins in sorted_leaders[0:5]:
        print(f"{wins:,} -- {name}")
    print()
    print("---------------------------")
    print()


def get_players():
    p1 = input("Player 1, what is your name? ")
    p2 = "Computer"

    return p1, p2


def play_game(player_1, player_2):
    log(f"New game starting between {player_1} and {player_2}.")
    wins = {player_1: 0, player_2: 0}
    roll_names = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll1 = get_roll(player_1, roll_names)
        roll2 = random.choice(roll_names)

        if not roll1:
            print("Try again!")
            continue

        log(f"Round: {player_1} rolls {roll1} and {player_2} rolls {roll2}.")
        print(f"{player_1} roll {roll1}")
        print(f"{player_2} rolls {roll2}")

        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            msg = "This round was a tie!"
            print(msg)
            log(msg)
        else:
            msg = f"{winner} takes the round!"
            print(msg)
            log(msg)
            wins[winner] += 1

        # print(f"Current win status: {wins}")

        msg = f"Score is {player_1}: {wins[player_1]} and {player_2}: {wins[player_2]}."
        print(msg)
        log(msg)

        print()

    overall_winner = find_winner(wins, wins.keys())
    msg = f"{overall_winner} wins the game!"
    print(msg)
    log(msg)
    record_win(overall_winner)


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name

    return None


def check_for_winning_throw(player_1, player_2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("The play was tied!")

    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        return player_1
    elif roll2 in outcome.get('defeated_by'):
        return player_2

    return winner


def get_roll(player_name, roll_names):
    print("Available rolls:")
    for index, r in enumerate(roll_names, start=1):
        print(f"{index}. {r}")

    text = input(f"{player_name}, what is your roll? ")
    selected_index = int(text) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {text} is out of bounds!")
        return None

    return roll_names[selected_index]


def load_rolls():
    global rolls

    # This is part of the library function, and it calls in the directory of json
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'rolls.json')

    # This is not safe, the CONTEXT MANAGER below is better
    # fin = open(filename, 'r', encoding='utf-8')
    # rolls = json.load(fin)
    # in.close()

    # NOTE: the 'r' means "read"
    with open(filename, 'r', encoding='utf-8') as fin:
        rolls = json.load(fin)

    print(f"Loaded rolls: {list(rolls.keys())}")

    log(f"Loaded Rolls: {list(rolls.keys())} from {os.path.basename(filename)}.")


def load_leaders():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


def record_win(winner_name):
    leaders = load_leaders()

    if winner_name in leaders:
        leaders[winner_name] += 1
    else:
        leaders[winner_name] = 1

    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'leaderboard.json')

    # json.dump saves a file as json
    # NOTE: the "w" means write (overwrite)
    with open(filename, 'w', encoding='utf-8') as fout:
        json.dump(leaders, fout)


# Create a function to log a file based on a message fed to it.
# And send the message to a file.
# Don't do this for actual logging!!! There are logging systems for that, like logbook.
# This is just to show you how a text file works in Python.
def log(msg):
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'rps.log')

    # The 'a' means APPEND
    with open(filename, 'a', encoding="utf-8") as fout:
        fout.write(f"[{datetime.datetime.now().isoformat()}]")
        fout.write(msg)
        # This next thing will add a blank line!
        fout.write('\n')


if __name__ == '__main__':
    main()