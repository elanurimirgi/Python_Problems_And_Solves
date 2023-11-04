#Homework1
import random

# Create a Word List
words = ["python", "programming", "game", "entertainment", "learning"]

# Randomly Select a Word
def choose_word(words):
    return random.choice(words)

# Define Game Variables
selected_word = choose_word(words)
guessed_letters = []
guesses_left = 6  # For example, 6 guesses allowed
win_condition = False

# Create the Game Loop
while not win_condition and guesses_left > 0:
    print("\nGuessed word: " + "".join([letter if letter in guessed_letters else "_" for letter in selected_word]))
    print("Guesses left: " + str(guesses_left))

    # Get a guess from the user
    guess = input("Guess a letter: ").lower()  # Convert the user's input to lowercase

    # Ensure it's a valid guess by performing checks
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid letter.")
        continue

    # Check the correctness of the guess
    if guess in guessed_letters:
        print("You've already guessed this letter.")
    elif guess in selected_word:
        guessed_letters.append(guess)
        if set(selected_word).issubset(set(guessed_letters)):
            win_condition = True
    else:
        guessed_letters.append(guess)
        guesses_left -= 1

# Display the Results
if win_condition:
    print("\nCongratulations! You correctly guessed the word. The word is: " + selected_word)
else:
    print("\nSorry, you've run out of guesses. The correct word was: " + selected_word)
