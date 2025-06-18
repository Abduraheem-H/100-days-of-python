import random
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(deck):
    score = sum(deck)
    # Adjust for Ace (11) if score is over 21
    while score > 21 and 11 in deck:
        deck[deck.index(11)] = 1
        score = sum(deck)
    return score


def blackJack():
    choice = input(
        "Do you want to play black jack game? Press any key except N "
    ).lower()
    if choice != "n":
        clear()

    player_deck = []
    computer_deck = []
    for _ in range(2):
        player_deck.append(random.choice(cards))
        computer_deck.append(random.choice(cards))
    user_score = calculate_score(player_deck)
    computer_score = calculate_score(computer_deck)

    if calculate_score(computer_deck) == 21 and calculate_score(player_deck) != 21:
        print(f"Your final hand: {player_deck}, final score: {user_score}")
        print(f"Computer final hand: {computer_deck}, final score: {computer_score}")
        print("Computer win with blackJack😱")
        blackJack()
    elif calculate_score(player_deck) == 21 and calculate_score(computer_deck) != 21:
        print(f"Your final hand: {player_deck}, final score: {user_score}")
        print(f"Computer final hand: {computer_deck}, final score: {computer_score}")
        print("You win with blackjack😱")
        blackJack()
    elif calculate_score(computer_deck) == 21 and calculate_score(player_deck) == 21:
        print(f"Your final hand: {player_deck}, final score: {user_score}")
        print(f"Computer final hand: {computer_deck}, final score: {computer_score}")
        print("You both draw with blackjack😱😱😱")
        blackJack()

    while choice != "n":

        print(f"Your cards: {player_deck}, current score {user_score}")
        print(f"Computer first card: {computer_deck[0] }")
        another = input("Type y to get another card or n to pass: ").lower()
        if another == "y":
            player_deck.append(random.choice(cards))
            computer_deck.append(random.choice(cards))
            user_score = sum(player_deck)
            computer_score = sum(computer_deck)
            if user_score > 21:
                print(f"Your cards: {player_deck}, current score {user_score}")
                print(f"Computer first card: {computer_deck[0] }")
                print(f"Your final hand: {player_deck}, final score: {user_score}")
                print(
                    f"Computer final hand: {computer_deck}, final score: {computer_score}"
                )
                print("You went over, you lose :( ")
                blackJack()

        elif another == "n":
            if user_score > computer_score:
                print(f"Your final hand: {player_deck}, final score: {user_score}")
                print(
                    f"Computer final hand: {computer_deck}, final score: {computer_score}"
                )
                print("You win! 😎")
            elif user_score == computer_score:
                print(f"Your final hand: {player_deck}, final score: {user_score}")
                print(
                    f"Computer final hand: {computer_deck}, final score: {computer_score}"
                )
                print("You Draw 🙃")

            elif computer_score > 21:
                print(f"Your final hand: {player_deck}, final score: {user_score}")
                print(
                    f"Computer final hand: {computer_deck}, final score: {computer_score}"
                )
                print("Computer went over, you win :)")

            else:
                print(f"Your final hand: {player_deck}, final score: {user_score}")
                print(
                    f"Computer final hand: {computer_deck}, final score: {computer_score}"
                )
                print("You lose :(")
            blackJack()


blackJack()
