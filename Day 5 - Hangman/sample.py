import random
import hangman.hamgman_words as hamgman_words, hangman.hangman_art as hangman_art


chosen_word = random.choice(hamgman_words.word_list)
print(f"Chosen word: {chosen_word}")  # For debugging

# Display with blanks
empty_display = ["_" for _ in chosen_word]

# Keep track of correct guesses
print(hangman_art.logo)
print("Guessing letter game!")
lives = 6
while "_" in empty_display and lives > 0:
    guess = input("Guess a letter: \n").lower()
    found = False
    if guess in empty_display:
        print(f"You have guessed letter {guess}")
        continue
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            empty_display[index] = guess
            found = True

    print("Current word: ", "".join(empty_display))
    if not found:
        print(f"{guess}, Incorrect guess. Try again!\n")
        lives -= 1
    print(hangman_art.stages[lives])

if "_" in empty_display:
    print("Game Over!, you have run out life")
else:
    print("You have won the Game!")
