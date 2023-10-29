import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game = [Rock, Paper, Scissors]
player_choice = int(input("Choose : 0 for Rock/ 1 for Paper/ 2 for Scissors :"))
bot_choice = random.randint(0,2)

print("Your choice is : ....")
if player_choice >=3 or player_choice < 0:
    print("Invalid Game,Sir:........................")
else:
    print(game[player_choice])
    print("Computer choice is : ....")
    print(game[bot_choice])

    if player_choice == 0 and bot_choice == 0:
        print("No Winner.............")
    elif player_choice == 1 and bot_choice == 0:
        print("You Won the game.........")
    elif player_choice == 0 and bot_choice == 1:
        print("Computer Won the Game, Sir..........")
    elif player_choice == 1 and bot_choice == 1:
        print("No Winner.............")
    elif player_choice == 2 and bot_choice == 2:
        print("No Winner.............")
    elif player_choice == 1 and bot_choice == 2:
        print("Computer Won the Game, Sir..........")
    elif player_choice == 2 and bot_choice == 1:
        print("You Won the game.........")
    elif player_choice == 2 and bot_choice == 0:
        print("Computer Won the Game, Sir..........")
    elif player_choice == 0 and bot_choice == 2:
        print("You Won the game.........")
    else:
        print("Invalid")
