# Library -> whole bunch of code someone else wrote
import random

globalVariable = True

def guessing_game():
  secret_number = random.randint(1, 100)
  num_guesses = 0
  
  while globalVariable:
    # ask the user to guess
    guess = int(input("Guess a secret number between 1 and 100: "))
    num_guesses += 1
  
    # check the guess
    if guess == secret_number:
      print(f"Congradulations, you guessed the correct number in {num_guesses} guesses!")
    elif guess < secret_number:
      print("Too low, try again!")
    else:
      print("Too high, try again!")
  
    if num_guesses >= 6:
      print("You have not guessed the number in the alloted tries.")
      break

guessing_game();