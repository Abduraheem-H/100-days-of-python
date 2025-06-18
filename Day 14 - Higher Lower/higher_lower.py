# higher_lower.py
# A Higher Lower game where players guess which of two options has more followers.

import random
from game_data import data
from art import logo, vs
import os


def clear():
    # Clear the console screen
    os.system("cls" if os.name == "nt" else "clear")


print(logo)

rand_comp = random.choice(data)


def higher_lower(compare):

    score = 0

    while True:
        against = random.choice(data)
        while against == compare:
            against = random.choice(data)

        print(
            f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}"
        )
        print(vs)
        print(
            f"Against B: {against['name']}, a {against['description']}, from {against['country']}"
        )
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if (
            choice == "a" and compare["follower_count"] < against["follower_count"]
        ) or (choice == "b" and compare["follower_count"] > against["follower_count"]):
            return score
        else:
            score += 1
            compare = against
            print(f"You are right! Current score: {score}")


score = higher_lower(rand_comp)
clear()
print(logo)
print(f"Sorry, that was wrong. Final score {score}")
