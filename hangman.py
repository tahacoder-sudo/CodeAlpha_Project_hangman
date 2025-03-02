import random

def choose_word():
    """Chooses a random word from a predefined list."""
    word_list = ["python", "java", "swift", "javascript", "ruby", "go", "kotlin", "csharp", "cplusplus", "php"]  # You can expand this list
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Displays the word with correctly guessed letters and underscores for others."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word

def play_hangman():
    """Runs the Hangman game."""
    word_to_guess = choose_word()
    word_length = len(word_to_guess)
    guessed_letters = set()
    incorrect_guesses_left = 6  # You can adjust the number of allowed incorrect guesses

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while incorrect_guesses_left > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            incorrect_guesses_left -= 1
            print(f"Incorrect. You have {incorrect_guesses_left} incorrect guesses left.")
        else:
            print("Correct guess!")

        print(display_word(word_to_guess, guessed_letters))

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations, you've guessed the word:", word_to_guess)
            return

    print("Game over! You ran out of guesses. The word was:", word_to_guess)

if __name__ == "__main__":
    play_hangman()