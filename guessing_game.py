#import random
import random 

# Generate a random number between 1 and 99
number = random.randint(1, 99)

# Ask the user to guess the number
guess = int(input("Guess a number between 1 and 99: "))

# Keep looping until the user guesses the number correctly
while guess != number:
    if guess < number:
        # The user's guess is too low
        print("Your guess is too low.")
    else:
        # The user's guess is too high
        print("Your guess is too high.")
    
    # Ask the user to guess the number again
    guess = int(input("Guess again: "))

# The user has guessed the number correctly
print("Congratulations! You guessed the number correctly.")


