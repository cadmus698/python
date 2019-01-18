import random
guessesLeft = 12
a = [1, 2, 3, 4, 5, 6, 7, 8]
code = ''
for i in random.sample(a, 5):
    code += str(i)

while True:
    correctPos = ''
    correctNumber = ''
    wrongNumber = ''
    codeIndex = 5
    xm = []
    guess = input("Guess a code\n")
    guessesLeft = guessesLeft-1
    if guess == code:
        print('Good job, you won!')
        print('I knew I could never beat you.')
        break
    while codeIndex >= 1:
        codeIndex -= 1
        if guess[codeIndex] in code:
            if guess[codeIndex] == code[codeIndex]:
                correctPos += '='            
            else:
                correctNumber += '+'
        else:
            wrongNumber += '-'
    
    if guessesLeft == 0:
        print('You lost! The code was ' + code + '.')
        break
    else:
        print(correctPos + correctNumber + wrongNumber)
