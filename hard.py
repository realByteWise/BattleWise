from resources import *

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
    print("Napoleon Bonaparte is placing his Battle ships...")
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
    print(END)
    clear(50)
    scroll([boldcyan],"You find yourself on the battle field during the midst of ")
    scroll([boldred],"The French Revolution.\n",0.05)
    clear()
    scroll([boldcyan],"You're face to face with the great Napoleon Bonaparte.")
    clear(50,2)
    print(END,Napoleon,sep="\n")
    scroll([boldred],"\"Oh you think you are ready to go against ")
    scroll([boldpurple],"THE GREAT EMPEROR NAPOLEON?\"",0.10)
    clear()
    scroll([boldred],"\"This battle shall be comical!\"")
    clear(50,2)
    scroll([boldpurple],"The Great Napoleon Bonaparte",0.05)
    scroll([boldcyan]," has sent his fleet to destroy you!\n")
    clear()
    scroll([boldcyan],"It's time to defend your nation!")
    clear(50,4)
    print(END)

#Main Game:
def game():
    #Creating Player's Board
    global boardSize
    boardSize = 6
    global playerBoard
    playerBoard = []
    for i in range(boardSize):
        row=[]
        for j in range(boardSize):
            row.append(' ')
        playerBoard.append(row)

    #Creating Computer's Board
    global csBoard
    csBoard = []
    for i in range(boardSize):
        row = []
        for j in range(boardSize):
            row.append(' ')
        csBoard.append(row)

    #Letter Number Grid
    global grid
    grid = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}

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
        
        while playerGuess[rowNo][colNo]!=' ':
            print("Those coordinates have already been destroyed!")
            t.sleep(1)
            rowNo,colNo = playerAttack(csBoard)
        
        if csBoard[rowNo][colNo]=='X':
            playerGuess[rowNo][colNo] = 'X'
            print("Your cannon has hit one of the enemy's battleships")
            playerHits+=1
            t.sleep(1)
            if playerHits==3:
                print(Napoleon)
                scroll([boldgreen],"You have defeated the Great Napoleon Bonaparte!")
                clear()
                scroll([boldgreen],"Are we at... Waterloo? (I hope someone got that reference)")
                clear(50,2)
                scroll([boldcyan],"You have beaten the great ")
                scroll([boldgreen],"Napoleon Bonaparte!")
                clear()
                scroll([boldcyan],"You Win!!!")
                break
            
        else:
            playerGuess[rowNo][colNo] = '-'
            print("Your cannon missed!")
            t.sleep(1)
        
        clear(25,1)
        print("The enemy is firing their cannon!")
        csRow = r.randint(0,boardSize-1)
        csCol = r.randint(0,boardSize-1)
        
        while csGuess[csRow][csCol]!=' ':
            csRow = r.randint(0,boardSize-1)
            csCol = r.randint(0,boardSize-1)
        
        if playerBoard[csRow][csCol] == 'X':
            csGuess[csRow][csCol] = 'X'
            print("One of your ship has been hit!")
            csHits+=1
            clear(1,1)
            if csHits==3:
                print(Napoleon)
                scroll([boldred],"It is impossible to beat the Great Napoleon you imbecile!")
                clear()
                scroll([boldred],"I admire you for trying. But now, perish!")
                clear(50,2)
                scroll([boldcyan],"You have lost against the great ")
                scroll([boldred],"Napoleon Bonaparte!")
                clear()
                scroll([boldcyan],"Adios!")
                break
        
        else:
            csGuess[csRow][csCol] = '-'
            print("The enemy missed their shot!")
            clear(1,1)
