"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


import random

def not_number_rejector(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_valid_input(message, low=None, high=None):
    while True:
        num = not_number_rejector(message)
        if low is not None and num < low:
            print(f"Input must be at least {low}.")
        elif high is not None and num > high:
            print(f"Input must be at most {high}.")
        else:
            return num

def advancedGuessingGame():
    """
    Play a guessing game with the user.
    
    This exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
    """
    print("\nWelcome to the advanced guessing game!")
    print("Please enter the range for the guessing game.")
    
    lowerBound = get_valid_input("Enter a lower bound: ")
    upperBound = get_valid_input("Enter an upper bound: ", low=lowerBound + 1)

    print(f"OK then, a number between {lowerBound} and {upperBound}?")
    
    actualNumber = random.randint(lowerBound, upperBound)
    guessed = False

    while not guessed:
        guessedNumber = get_valid_input("Guess a number: ", low=lowerBound, high=upperBound)
        print(f"You guessed {guessedNumber},")
        if guessedNumber == actualNumber:
            print(f"You got it!! It was {actualNumber}")
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :(")
        else:
            print("Too big, try again :(")

    return "You got it!"

if __name__ == "__main__":
    print(advancedGuessingGame())


