#guess the number exercise like input a number and check if the number you have entered is matching witht the computer input or not
#no of guesses =9
#print no of guesses left
# print game over if the nof of gueess are over
#and if he /she wins then print the in how many no of gueeses he / she guesed it correctly

print("Welcome to Game,This is the number guessing game by Subhasree")
num = 20
no_of_guess =0
run = "Y, N"

while(no_of_guess!=9):
    print("Guess a number between 1 to 100 and you can only guess it 9 times")
    guessno=int(input())
    no_of_guess = no_of_guess+1
    if guessno==num:
        print("Congrats! You have guessed it right in ", no_of_guess, "no of guesses")
        print("For you the no of guesses left is : ", 9-no_of_guess)
        break

    elif guessno>num:
        print("You guessed too high")
        print("Guess again!")
    else:
        print("You guessed too low")
        print("Guess again!")

if guessno!=num:
    print("Game Over! You couldn't guess the number")
    print("You want to play again", run)
    # if run=="Y":


