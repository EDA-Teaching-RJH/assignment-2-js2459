### Part Two -- your code goes here. 
import random

target_number = random.randint(1, 100)  
guess = 0

print("Guess a number between 1 and 100")

while guess != target_number:
    guess = int(input("Enter your guess: "))  
    if guess < target_number:
        print("Guess is too low, try again!")
    elif guess > target_number:
        print("Guess is too high, try again!")
    else:
        print("Congratulations! You've guessed the correct number.")
