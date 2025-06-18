import random
from number_art import logo

number = random.randint(1, 100)
easy_level_attempts = 10
hard_level_attempts = 5
print(logo)
print("Welcome to the number guessing game! ")
print("I am thinking of number between 1 and 100")
# print(f"random number {number}") for debugging purpose only

difficulty = input("Choose difficulty: Type easy or hard: ").lower()


def game(game_level, guess):

    while guess != number and game_level > 1:
        game_level -= 1
        if guess > number:

            print("Too high")
            print("Guess again")
            print(f"You have {game_level} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))

        else:

            print("Too low")
            print("Guess again")
            print(f"You have {game_level} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
    if game_level > 0 and number == guess:
        print(f"You got it the answer was {guess}")
    else:
        if guess > number:
            print("Too high")
        else:
            print("Too low.")
        print("You run out of guesses you lose")


if difficulty == "easy":
    print(f"You have {easy_level_attempts} attempts remaing")
    guess = int(input("Make a guess: "))
    game(easy_level_attempts, guess)
else:
    print(f"You have {hard_level_attempts} attempts remaing")
    guess = int(input("Make a guess: "))
    game(hard_level_attempts, guess)
