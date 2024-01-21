import time
import random
def clear2():
    for hu in range(24):
        print("")
def secretbord(board):
    print("     A     B    C   ")
    print("━━━━━━━━━━━━━")
    row_number = 1
    for row in board:
        print(row_number, end=' ┃ ')
        for cell in row:
            if cell == 'X':
                print(' ' + ' ' + ' ┃', end=' ')
            else:
                print(' ' + str(cell) + ' ┃', end=' ')
        print()
        print("━━━━━━━━━━━━━")
        row_number += 1

def showbord(board):
    print("     A     B    C   ")
    print(" ━━━━━━━━━━━━━")
    row_number = 1
    for row in board:
        print(row_number, end=' ┃ ')
        for cell in row:
            print(' ' + str(cell) + ' ┃', end=' ')
        print()
        print(" ━━━━━━━━━━━━━")
        row_number += 1

def clear():
    time.sleep(1)
    for _ in range(40):
        print("")

def userattack(board):
    column=input("Column (A to C): ").upper()
    while column not in "ABC":
        print("That column is wrong! It should be A, B or C")
        column = input("Column (A to C): ").upper()
    row=input("Enter the row number (1 to 3): ")
    while row not in "123":
        print("That row is wrong! It should be 1, 2 or 3")
        row = input("Row (1 to 3): ")
    
    rowno=int(row) - 1
    colno=letternumgrid[column]

    while board[rowno][colno] == 'X':
        print("You can't attack your own battleship location!")
        column = input("Enter Column (A to c)  : ").upper()
        while column not in "ABCDE":
            print("That column is wrong! It should be A, B or C")
            column = input("Column (A to C): ").upper()
        row = input("Enter the row number (1 to 3)  : ")
        while row not in "12345":
            print("That row is wrong! It should be 1, 2 or 3")
            row = input("Enter row (1 to 3) : ")
        
        rowno=int(row)-1
        colno=letternumgrid[column]
    return rowno,colno


def placeship(board, bordguess):
    for x in range(2):
        csrow = random.randint(0, bordsiz - 1)
        cscolumn = random.randint(0, bordsiz - 1)
        while board[csrow][cscolumn] == 'X' or bordguess[csrow][cscolumn] != ' ':
            csrow = random.randint(0, bordsiz - 1)
            cscolumn = random.randint(0, bordsiz - 1)

        board[csrow][cscolumn] = 'X'

def game():
    print("Place your battleships:")
    showbord(board)
    for a in range(1):
        print("Place ship ", a+1)
        rowno,colno = userattack(board)
        while board[rowno][colno]== 'X':
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

    bordguess = []
    for _ in range(bordsiz):
        row = []
        for _ in range(bordsiz):
            row.append(' ')
        bordguess.append(row)

    playerchance=0
    cschance=0
    chances=8

    while playerchance<2 and cschance<2 and chances>0:
        print("Your turn to guess:")
        rowno,colno=userattack(board)
        if bordguess[rowno][colno] != ' ':
            print("You have already guessed that place ")
            continue

        if csbord[rowno][colno]=='X':
            clear()
            print("YOU HIT THE WARSHIP!!!")
            time.sleep(2)
            print("Congratulations General you have sunk the Warship ")
            print("Thank you for playing!!")
            break
            
        else:
            bordguess[rowno][colno] = '.'
            print("Your cannon has shot ....IT MISSED!")

        clear()
        print("THE ENEMY HAS FIRED THIER CANNON:")
        time.sleep(1)
        csrow=random.randint(0,bordsiz-1)
        cscolumn=random.randint(0,bordsiz-1)
        while bordguess[csrow][cscolumn] != ' ':
            csrow = random.randint(0, bordsiz - 1)
            cscolumn = random.randint(0, bordsiz - 1)

        if board[csrow][cscolumn] == 'X':
            clear()
            print("GENERAL WE HAVE BEEN HIT ABANDON  SHIP!!!")
            print("Your warship was destroyed in war try again!")
            break
        else:
            bordguess[csrow][cscolumn] = '.'
            print("The Enemy MISSED!")

        showbord(bordguess)
        chances-=1
        print('Chances left :', chances)


            
bordsiz=3
board=[]
for pp in range(bordsiz):
    row=[]
    for x in range(bordsiz):
        row.append(' ')
    board.append(row)
csbord=[]
for x in range(bordsiz):
    row=[]
    for y in range(bordsiz):
        row.append(' ')
    csbord.append(row)
letternumgrid= {'A': 0,'B': 1,'C': 2}


