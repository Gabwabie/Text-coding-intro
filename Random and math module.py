# import random
# playing = True
# number = (random.randint(1,5))
# print(number)
# print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
# print("The game ends when you get 1 hero!")
# while playing:
#     guess = int(input("Give me your best guess! \n"))
#     if number == guess:
#         print("You win the game")
#         print("Thr number was", number)
#         break
#     else:
#         print("Your guess isn't quite right, try againn \n")

import random
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_acions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_acions)
    print(f"\n You chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break