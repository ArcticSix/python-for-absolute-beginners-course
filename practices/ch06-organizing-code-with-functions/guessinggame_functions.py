# Import the Random library to use for M&M count
import random


# Define the main program
def main():
    show_header()

    play_game(input("What is your name? "))


def show_header():
    # Print a snazzy title and basic description
    print('--------------------------------------------------------')
    print('|                   M&M Guessing Game                  |')
    print('--------------------------------------------------------')
    print()
    print("Guess the number of M&Ms and you get lunch on the house!")
    print()


def play_game(customer):
    # They get 5 guesses
    attempt_limit = 5
    attempts = 0

    # Generate a random M&M count between 1 and 100
    mm_count = random.randint(1, 100)

    while attempts < attempt_limit:
        guess = get_guess(customer, mm_count, attempts)

        win = check_guess(customer, mm_count, guess)

        if win == 0:
            if attempts < 4:
                print(f"Guess again, {customer}!")
                attempts += 1
            elif attempts == attempt_limit:
                print(f"Sorry, {customer}, try again later!")
                break
        elif win == 1:
            print(f"Congratulations, {customer}! You got a free lunch! There were {mm_count} M&Ms in the jar.")
            break

    print(f"Goodbye, {customer}. You finished in {attempts} rounds!")


def check_guess(customer, mm_count, guess):
    win = 0
    if mm_count == guess:
        win += 1
    elif guess < mm_count:
        print(f"{guess} is too low!")
    else:
        print(f"{guess} is too high!")

    return win


def get_guess(customer, mm_count, attempts):
    if attempts == 0:
        guess_text = input(f"{customer}, how many M&Ms are in the jar? ")
        print()
    elif attempts < 4:
        guess_text = input(f"What is your guess? ")
        print()
    else:
        guess_text = input(f"Last chance! How many M&Ms are in the jar? ")
        print()

    # Convert the user's guess to integer
    guess = int(guess_text)

    return guess


if __name__ == '__main__':
    main()
