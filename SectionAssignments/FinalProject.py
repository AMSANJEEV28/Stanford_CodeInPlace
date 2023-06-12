import random

LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Max number of guesses per game

def play_game(secret_word):
    guessed_letters = []
    incorrect_guesses = 0
    word_length = len(secret_word)
    current_word = ['_'] * word_length

    while '_' in current_word and incorrect_guesses < INITIAL_GUESSES:
        print("Current word:", ' '.join(current_word))
        print("Guessed letters:", ' '.join(guessed_letters))
        guess = input("Guess a letter: ").strip().upper()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            for i in range(word_length):
                if secret_word[i] == guess:
                    current_word[i] = guess
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")
            print("You have", INITIAL_GUESSES - incorrect_guesses, "guesses left.")

    if '_' not in current_word:
        print("Congratulations! You guessed the word:", secret_word)
    else:
        print("You ran out of guesses. The word was:", secret_word)

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game. The word is randomly chosen from a file
    specified by the constant LEXICON_FILE.
    """
    with open(LEXICON_FILE, 'r') as file:
        words = file.readlines()
        words = [word.strip().upper() for word in words]
        return random.choice(words)

def main():
    secret_word = get_word()
    play_game(secret_word)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
