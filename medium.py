import time
import random

playerchance = 0
cschance = 0
chances = 8

def clear2():
    for hu in range(24):
        print("")

def secretbord(board):
    print("     A     B    C     D ")
    print("━━━━━━━━━━━━━━━━━")
    rowno = 1
    for row in board:
        print(rowno, end=' ┃ ')
        for cell in row:
            if cell == 'X':
                print(' ' + ' ' + ' ┃', end=' ')
            else:
                print(' ' + str(cell) + ' ┃', end=' ')
        print()
        print("━━━━━━━━━━━━━━━━━━━")
        rowno += 1

def showbord(board):
    print("     A     B    C     D  ")
    print(" ━━━━━━━━━━━━━━━━")
    rowno = 1
    for row in board:
        print(rowno, end=' ┃ ')
        for cell in row:
            print(' ' + str(cell) + ' ┃', end=' ')
        print()
        print(" ━━━━━━━━━━━━━━━━")
        rowno += 1

def clear():
    time.sleep(1)
    for pop in range(40):
        print("")

def userattack(board):
    while True:
        column = input("Column (A to D): ").upper()
        while column not in "ABCD":
            print("That column is wrong. It should be A, B, C, or D.")
            column = input("Enter a Column (A to D): ").upper()

        row = input("Enter the row number (1 to 4): ")
        while row not in "1234":
            print("That row is wrong! It should be 1, 2, 3, or 4.")
            row = input("Enter Row (1 to 4): ")

        rowno = int(row) - 1
        colno = letternumgrid[column]

        if board[rowno][colno] == 'X':
            print("You can't attack your own battleship location!")
        else:
            break

    return rowno, colno
def end():
    clear()
    print("GAME OVER!!")

def placeship(board, bordguess):
    for x in range(2):
        csrow = random.randint(0, bordsiz - 1)
        cscolumn = random.randint(0, bordsiz - 1)
        while board[csrow][cscolumn] == 'X' or bordguess[csrow][cscolumn] != ' ':
            csrow = random.randint(0, bordsiz - 1)
            cscolumn = random.randint(0, bordsiz - 1)

        board[csrow][cscolumn] = 'X'

def check():
    global playerchance, go
    if playerchance == 2:
        print("Congratulations! You sank the enemy battleship!")
        go = 1
        end()

    elif cschance == 2:
        print("Sorry, Enemy defeated you. Better luck next time!")
        go = 1
        end()

    elif chances == 0:
        print("You both ran out of Cannons. RETREAT!")
        go = 1
        end()

def game():
    global go, playerchance, cschance, chances
    while go == 0:
        print("Place your battleships:")
        showbord(board)
        for a in range(2):
            print("Place ship ", a + 1)
            rowno, colno = userattack(board)
            while board[rowno][colno] == 'X':
                print("You already placed a battleship there!")
                rowno, colno = userattack(board)
            board[rowno][colno] = 'X'
            clear()
            showbord(board)

        print("Computer placing battleships:")
        bordguess = [[' ' for _ in range(bordsiz)] for _ in range(bordsiz)]
        placeship(csbord, bordguess)
        clear()
        secretbord(csbord)

        bordguess = [[' ' for _ in range(bordsiz)] for _ in range(bordsiz)]

        playerchance = 0
        cschance = 0
        chances = 8

        while playerchance < 2 and cschance < 2 and chances > 0:
            print("Your turn to guess:")
            rowno, colno = userattack(board)
            if bordguess[rowno][colno] != ' ':
                print("You have already guessed that place ")
                continue

            if csbord[rowno][colno] == 'X':
                print("You Have Sunk A BattleShip!")
                bordguess[rowno][colno] = 'X'
                playerchance += 1
                check()

            else:
                bordguess[rowno][colno] = '.'
                print("Your cannon has shot ....IT MISSED!")

            clear()
            print("THE ENEMY HAS FIRED THEIR CANNON:")
            time.sleep(1)
            csrow = random.randint(0, bordsiz - 1)
            cscolumn = random.randint(0, bordsiz - 1)
            while bordguess[csrow][cscolumn] != ' ':
                csrow = random.randint(0, bordsiz - 1)
                cscolumn = random.randint(0, bordsiz - 1)

            if csbord[csrow][cscolumn] != 'X':
                if board[csrow][cscolumn] == 'X':
                    print("The Enemy HIT one of your battleships!")
                    bordguess[csrow][cscolumn] = 'X'
                    cschance += 1
                    check()
                else:
                    bordguess[csrow][cscolumn] = '.'
                    print("The Enemy MISSED!")

                showbord(bordguess)
                chances -= 1
                print('Chances left:', chances)

        if go == 0:  # Check if the game is not over before asking for replay
            check()
            replay = input("Do you want to play Genghis Khan Again? (yes/no): ").upper()
            if replay != 'YES':
                go = 1
                break  # Exit the outer loop

go = 0
bordsiz = 4
board = []
for pp in range(bordsiz):
    row = []
    for x in range(bordsiz):
        row.append(' ')
    board.append(row)

csbord = []
for x in range(bordsiz):
    row = []
    for y in range(bordsiz):
        row.append(' ')
    csbord.append(row)

letternumgrid = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

# Call the game function to start the game
game()
