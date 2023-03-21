import random

def jadahre():
    # generate a random number between 1 and 100
    number = random.randint(1, 100)
    # keep track of the number of guesses
    num_guesses = 0
    
    while True:
        # get user input
        guess = input("Guess a number between 1 and 100: ")
        # convert the user input to an integer (if possible)
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        
        # increment the number of guesses
        num_guesses += 1
        
        # check if the guess is correct
        if guess == number:
            print("Congratulations, you guessed the number in", num_guesses, "guesses!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
            
if __name__ == '__main__':
    jadahre()
