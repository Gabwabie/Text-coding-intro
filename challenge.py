# Guessing game

import random

list = ["a", "b", "c", "d", "e"]
ch = random.choice(list)
num = random.randint(1,10)

score = 0
for i in range(5):
    guess = int(input("Guess a number between 1 and 10:"))

    if num == guess:
        print("You won!")
        score += 1
        num = random.randint
        break
    else:
        if guess<num:
            print("Your guess is too low, guess higher:")
        elif guess>num:
            print("Your guess is too high, guess lower:")

print("Your guesses are done!!")
print("You scored",score,"points.")