#exercise = Game = Snake, water and Gun

print("Welcome to the Snake Water and Gun Game by Subhasree")

import random
char = "SWG" # computer will generate the random character from these characters # so now computer can generate

comp_value=0
user_value=0

no_of_Times = 1
while(no_of_Times!=10):
    random_char = random.choice(char)
    print("Choose S for Snake, W for Water and G for Gun")
    value = input()
    if random_char==value:
        print("Match Drawn!")

    elif random_char=="S" and value=="W":
        comp_value = comp_value+1
        print("You loose! Try again")

    elif random_char=="W" and value=="S":
        user_value= user_value+1
        print("You win! Want to play again")

    elif random_char=="S" and value=="G":
        user_value = user_value + 1
        print("You win! Want to play again")

    elif random_char=="G" and value=="S":
        comp_value = comp_value + 1
        print("You loose! Try again")

    elif random_char=="W" and value=="G":
        comp_value = comp_value + 1
        print("You loose! Try again")

    elif random_char=="G" and value=="W":
        user_value = user_value + 1
        print("You win! Want to play again")

    else:
        print("Invalid Input! Want to play again")

    no_of_Times = no_of_Times+1

if comp_value>user_value:
    print("Game Over!")
    print(f"Your score is : {user_value} and computer score is : {comp_value}")
    print("This time you Loose!")

else:
    print("Game Over!")
    print(f"Your score is : {user_value} and computer score is : {comp_value}")
    print("You won Finally!")




