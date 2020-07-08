import random
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
cnt = -1
win = False
winner = ''
def checkwin():
    global win
    global winner
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X' or board[3] == 'X' and board[4] == 'X' and board[5] == 'X' or board[6] == 'X' and board[7] == 'X' and board[8] == 'X' or board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or board[2] == 'X' and board[4] == 'X' and board[6] == 'X' or board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        win = True
        winner = 'player'

    
    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O' or board[3] == 'O' and board[4] == 'O' and board[5] == 'O' or board[6] == 'O' and board[7] == 'O' and board[8] == 'O' or board[0] == 'O' and board[4] == 'O' and board[8] == 'O' or board[2] == 'O' and board[4] == 'O' and board[6] == 'O' or board[0] == 'O' and board[3] == 'O' and board[6] == 'O' or board[1] == 'O' and board[4] == 'O' and board[7] == 'O' or board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
        win = True
        winner = 'computer'
    
    else:
        win = False
        winner = ''

def updateboard():
    global board
    shouldcont = True
    newslot = -1 + int(input('What do you want to play?\n'))
    if board[newslot] == 'X' or board[newslot] == 'O':
        suggestion = random.choice(range(0, 8))
        while True:
            if board[suggestion] == 'X' or board[suggestion] == 'O':
                suggestion = random.choice(range(0, 8))

            else:
                break
        suggestion += 1
        newslot = -1 + int(input("Oops! You can't play that slot. Maybe try " + str(suggestion) +"\n"))
    board[newslot] = 'X'
    checkwin()
    if win == True:
        shouldcont = False
    if shouldcont:
        cpuslot = random.choice(range(0, 8))
        while True:
            if board[cpuslot] == 'X' or board[cpuslot] == 'O':
                cpuslot = random.choice(range(0, 8))

            else:
                break
        board[cpuslot] = 'O'
print('1|2|3')
print('-----')
print('4|5|6')
print('-----')
print('7|8|9')
while True:
    updateboard()
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-----')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-----')
    print(board[6]+'|'+board[7]+'|'+board[8])
    checkwin()
    if win == True:
        if winner == 'player':
            print('Congratulations! You win.')
        elif winner == 'computer':
            print('Oh no! The computer won!')
        break