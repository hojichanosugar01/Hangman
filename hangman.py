import random

def get_random_word():
  """Gets a random word from a list of words."""
  with open("words.txt", "r") as f:
    words = f.readlines()
  return random.choice(words).strip()

def display_hangman(guesses_left):
  """Displays the hangman image, given the number of guesses left."""
  hangman = [
    "  +---+",
    "  |   ",
    "  |   ",
    "  |   ",
    "  +---+"
  ]

  for i in range(guesses_left):
    hangman[i + 1] = "  |X  "

  return hangman

def get_user_guess():
  """Gets a guess from the user."""
  while True:
    guess = input("Guess a letter: ").lower()
    if len(guess) == 1:
      return guess
    else:
      print("Please enter a single letter.")

def check_guess(guess, word, guesses_left):
  """Checks if the guess is correct and updates the hangman image."""
  if guess in word:
    for i, letter in enumerate(word):
      if letter == guess:
        word[i] = "_"

  if guess not in word:
    guesses_left -= 1

  return guesses_left

def play_hangman():
  """Plays a game of Hangman."""
  word = get_random_word()
  guesses_left = 6
  hangman_image = display_hangman(guesses_left)

  while guesses_left > 0:
    print("The word to guess is:", "".join(word))
    print("`", "".join(hangman_image), "`")

    guess = get_user_guess()
    guesses_left = check_guess(guess, word, guesses_left)

    if guesses_left == 0:
      print("You lost!")
      print("The word was:", word)
      break

    if "".join(word).count("_") == 0:
      print("You won!")
      break

if __name__ == "__main__":
  play_hangman()
