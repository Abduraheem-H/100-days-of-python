from art import logo
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


print(logo)
print("Welcome to the secret auction program")
auction_dict = {}
flag = True

while flag:
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    auction_dict[name] = bid
    char = input("Are there any other bidders? Type any key except N: ").lower()

    if char == "n":
        flag = False
    else:
        clear()


# Determine the winner
highest = 0
winner = ""
for key in auction_dict:
    bid = int(auction_dict[key])
    if bid > highest:
        highest = bid
        winner = key

print(f"The winner is {winner} with a bid of ${highest}")
