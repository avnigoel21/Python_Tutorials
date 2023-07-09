# The game() function in a program lets a user play a game and returns the score as an integer.
# you need to read a file 'HighScore.txt' which is either blank or contains the previous high-score.
# You need to write a program to update the high-score whenever game() breaks the high-score

def game():
    return 778

score = game()

with open('HighScore.txt') as f:
    highScoreStr = f.read()

if highScoreStr == '' :
    with open('HighScore.txt' , 'w') as f:
        f.write(str(score))

elif int(highScoreStr) < score :
    with open('HighScore.txt' , 'w') as f:
        f.write(str(score))

