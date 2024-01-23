from resources import *
import time as t
import random as r

#Show Boards:
def showBoard(board):
    print("     A    B    C    D    E    F")
    print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    rowNum = 1
    for row in board:
        print(rowNum,end=" ┃ ")
        for cell in row:
            print(' ' + str(cell) + ' ┃', end=' ')
        print()
        print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        rowNum += 1

#Player Placing Ships:
def placePlayerShip(board):
    print("Place your Battle ships!")
    showBoard(playerBoard)
    for ships in range(3):
        print("Place Battle Ship",ships+1)
        column = input("Enter column (A to F): ").upper()
        while column not in 'ABCDEF':
            column = input("Column out of bounds! Enter again: ").upper()
        row = input("Enter Row number (1 to 6): ")
        while row not in '123456':
            row = input("Row out of bounds! Enter again: ")
        
        rowNo = int(row)-1
        colNo = grid[column]
    
        while board[rowNo][colNo] == 'X':
            print("You have already placed a ship there! Try again.")
            column = input("Enter column (A to F): ").upper()
            while column not in 'ABCDEF':
                column = input("Column out of bounds! Enter again: ").upper()
            row = input("Enter Row number (1 to 6): ")
            while row not in '123456':
                row = input("Row out of bounds! Enter again: ")
        
            rowNo = int(row)-1
            colNo = grid[column]
    
        board[rowNo][colNo] = 'X'
        clear(25,1)
        showBoard(board)
        
#Computer Placing Ships:
def csPlaceShip(board):
    print("Computer placing Battle ships...")
    t.sleep(1)
    for ships in range(3):
        csRow = r.randint(0,boardSize-1)
        csCol = r.randint(0,boardSize-1)
        while board[csRow][csCol]=='X':
            csRow = r.randint(0,boardSize-1)
            csCol = r.randint(0,boardSize-1)
        
        board[csRow][csCol] = 'X'
    clear(25,2)

#Player Attacks:
def playerAttack(board):
    column=input("Enter Column (A to F): ").upper()
    while column not in "ABCDEF":
        column = input("Column out of bounds! Enter again: ").upper()
    row=input("Enter row number (1 to 6): ")
    while row not in "123456":
        row = input("Row out of bounds! Enter again: ")
    
    rowNo = int(row)-1
    colNo = grid[column]

    while board[rowNo][colNo] == '-':
        print("You already guessed that area! Try again.")
        column = input("Enter Column (A to F)  : ").upper()
        while column not in "ABCDEF":
            column = input("Column out of bounds! Enter again: ").upper()
        row = input("Enter row number (1 to 6)  : ")
        while row not in "123456":
            row = input("Row out of bounds! Enter again: ")
        
        rowNo = int(row)-1
        colNo = grid[column]
    return rowNo,colNo

#Dialogue:
def dialogue():
    scroll([boldred],"*replacement dialogue*")
    clear(24,4)
    print(END)

#Main Game:
def game():
    #Dialogue:
    dialogue()
    
    #Player Placing Ships
    placePlayerShip(playerBoard)
    clear(25,1)

    #Player Guess Board:
    playerGuess = []
    for i in range(boardSize):
        row=[]
        for j in range(boardSize):
            row.append(' ')
        playerGuess.append(row)
    
    #Computer Guess Board:
    csGuess = []
    for i in range(boardSize):
        row=[]
        for j in range(boardSize):
            row.append(' ')
        csGuess.append(row)
    
    #Computer Placing Ships:
    csPlaceShip(csBoard)
    
    #Guessing Time:
    playerHits = 0
    csHits = 0
    
    while True:
        showBoard(playerGuess)
        print("It's time to fire your cannon!")
        rowNo,colNo = playerAttack(csBoard)
        
        if playerGuess[rowNo][colNo]!=' ':
            print("Those coordinates have already been destroyed!")
            t.sleep(1)
            continue
        
        if csBoard[rowNo][colNo]=='X':
            playerGuess[rowNo][colNo] = 'X'
            print("Your cannon has hit one of the enemy's battleships")
            playerHits+=1
            t.sleep(1)
            
        else:
            playerGuess[rowNo][colNo] = '-'
            print("Your cannon missed!")
            t.sleep(1)
        
        clear(25,1)
        print("The enemy is firing their cannon!")
        csRow = r.randint(0,boardSize-1)
        csCol = r.randint(0,boardSize-1)
        
        if playerBoard[csRow][csCol]!=' ':
            csRow = r.randint(0,boardSize-1)
            csCol = r.randint(0,boardSize-1)
        
        if playerBoard[csRow][csCol] == 'X':
            csGuess[csRow][csCol] = 'X'
            print("One of your ship has been hit!")
            csHits+=1
            clear(1,1)
        
        else:
            csGuess[csRow][csCol] = '-'
            print("The enemy missed their shot!")
            clear(1,1)
        
        if playerHits==3:
            print("You destroyed all of the enemy's ships! You Win!!!")
            break
        
        elif csHits==3:
            print("The enemy has hit all your battle ships! You Lost. L + Ratio + *every single insult in existence*")
            break
        
#Creating Player's Board
boardSize = 6
playerBoard = []
for i in range(boardSize):
    row=[]
    for j in range(boardSize):
        row.append(' ')
    playerBoard.append(row)

#Creating Computer's Board
csBoard = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(' ')
    csBoard.append(row)

#Letter Number Grid
grid = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}

game()
