from resources import *

#Show Boards:
def showBoard(board):
    print("     A    B    C    D    E")
    print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━")
    rowNum = 1
    for row in board:
        print(rowNum,end=" ┃ ")
        for cell in row:
            print(' ' + str(cell) + ' ┃', end=' ')
        print()
        print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━")
        rowNum += 1

#Player Placing Ships:
def placePlayerShip(board):
    print("Place your Battle ships!")
    showBoard(playerBoard)
    for ships in range(3):
        print("Place Battle Ship",ships+1)
        column = input("Enter column (A to E): ").upper()
        while column not in 'ABCDE':
            column = input("Column out of bounds! Enter again: ").upper()
        row = input("Enter Row number (1 to 5): ")
        while row not in '12345':
            row = input("Row out of bounds! Enter again: ")
        
        rowNo = int(row)-1
        colNo = grid[column]
    
        while board[rowNo][colNo] == 'X':
            print("You have already placed a ship there! Try again.")
            column = input("Enter column (A to E): ").upper()
            while column not in 'ABCDE':
                column = input("Column out of bounds! Enter again: ").upper()
            row = input("Enter Row number (1 to 5): ")
            while row not in '12345':
                row = input("Row out of bounds! Enter again: ")
        
            rowNo = int(row)-1
            colNo = grid[column]
    
        board[rowNo][colNo] = 'X'
        clear(25,1)
        showBoard(board)
        
#Computer Placing Ships:
def csPlaceShip(board):
    print("Genghis Khan is placing his Battle ships...")
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
    column=input("Enter Column (A to E): ").upper()
    while column not in "ABCDE":
        column = input("Column out of bounds! Enter again: ").upper()
    row=input("Enter row number (1 to 5): ")
    while row not in "12345":
        row = input("Row out of bounds! Enter again: ")
    
    rowNo = int(row)-1
    colNo = grid[column]

    while board[rowNo][colNo] == '-':
        print("You already guessed that area! Try again.")
        column = input("Enter Column (A to E)  : ").upper()
        while column not in "ABCDE":
            column = input("Column out of bounds! Enter again: ").upper()
        row = input("Enter row number (1 to 5)  : ")
        while row not in "12345":
            row = input("Row out of bounds! Enter again: ")
        
        rowNo = int(row)-1
        colNo = grid[column]
    return rowNo,colNo

#Dialogue:
def dialogue():
    print(END)
    clear(50)
    scroll([boldcyan],"You're face to face with Genghis Khan's battle horde which has conquered a surplus of nations.")
    clear(50,2)
    print(END,Genghis,sep="\n")
    scroll([boldred],"\"Looks like you like yourself a bit of a challenge eh!?\"")
    clear()
    scroll([boldred],". . . . .")
    clear()
    scroll([boldred],"\"I hope you're ready for what's coming!\"")
    clear(50,3)
    scroll([boldcyan],"This battle won't be an easy one, General!")
    clear(50,1)
    scroll([boldcyan],"The fight will begin soon!")
    clear()
    scroll([boldcyan],"Place your battle ships in strategic positions and fight for your glory!")
    clear(50,2)
    print(END,Genghis,sep="\n")
    scroll([boldred],"or perish.....",0.100)
    clear(50,4)
    print(END)

#Main Game:
def game():
    #Creating Player's Board
    global boardSize
    boardSize = 5
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
    grid = {'A':0,'B':1,'C':2,'D':3,'E':4}
    
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
                print(Genghis)
                scroll([boldgreen],"You... beat me...")
                clear()
                scroll([boldgreen],"how...?")
                scroll([boldgreen],"I surrender my kingdom to you!")
                clear(50,2)
                scroll([boldcyan],"Congratulations General! You have successfuly beaten the mighty ")
                scroll([boldgreen],"Genghis Khan!")
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
                print(Genghis)
                scroll([boldred],"You really thought you could beat me!")
                clear()
                scroll([boldred],"THE MIGHTY GENGHIS KHAN STILL REIGNS MIGHTY! MUAHAHAHA!")
                clear(50,2)
                scroll([boldcyan],"You have lost against the mighty ")
                scroll([boldred],"Genghis Khan!")
                clear()
                scroll([boldcyan],"GGs!")
                break
        
        else:
            csGuess[csRow][csCol] = '-'
            print("The enemy missed their shot!")
            clear(1,1)
