# Guess the Number
# using random module

import random
randomNumber = random.randint(1 , 100)

userGuess = None
guesses = 0
while(userGuess != randomNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess == randomNumber):
        print("you guessed it right!!")
    else:
        if(userGuess > randomNumber):
            print("wrong guess, Enter a smaller number")
        else:
            print("wrong guess, Enter a larger number")
print(f"You guessed the number in {guesses} guesses.")

with open("highScore.txt" , "r") as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("you have just broken the high score!")
    with open("highScore.txt" , "w") as f:
        f.write(str(guesses))

