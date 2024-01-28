from resources import *

#Show Boards:
def showBoard(board):
    print("     A    B    C    D    E    F    G")
    print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    rowNum = 1
    for row in board:
        print(rowNum,end=" ┃ ")
        for cell in row:
            print(' ' + str(cell) + ' ┃', end=' ')
        print()
        print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        rowNum += 1

#Player Placing Ships:
def placePlayerShip(board):
    print("Place your Battle ships!")
    showBoard(playerBoard)
    for ships in range(4):
        print("Place Battle Ship",ships+1)
        column = input("Enter column (A to G): ").upper()
        while column not in 'ABCDEFG':
            column = input("Column out of bounds! Enter again: ").upper()
        row = input("Enter Row number (1 to 7): ")
        while row not in '1234567':
            row = input("Row out of bounds! Enter again: ")
        
        rowNo = int(row)-1
        colNo = grid[column]
    
        while board[rowNo][colNo] == 'X':
            print("You have already placed a ship there! Try again.")
            column = input("Enter column (A to G): ").upper()
            while column not in 'ABCDEFG':
                column = input("Column out of bounds! Enter again: ").upper()
            row = input("Enter Row number (1 to 7): ")
            while row not in '1234567':
                row = input("Row out of bounds! Enter again: ")
        
            rowNo = int(row)-1
            colNo = grid[column]
    
        board[rowNo][colNo] = 'X'
        clear(25,1)
        showBoard(board)
        
#Computer Placing Ships:
def csPlaceShip(board):
    print("The undefeated Rajat is placing his Battle ships...")
    t.sleep(1)
    for ships in range(4):
        csRow = r.randint(0,boardSize-1)
        csCol = r.randint(0,boardSize-1)
        while board[csRow][csCol]=='X':
            csRow = r.randint(0,boardSize-1)
            csCol = r.randint(0,boardSize-1)
        
        board[csRow][csCol] = 'X'
    clear(25,2)

#Player Attacks:
def playerAttack(board):
    column=input("Enter Column (A to G): ").upper()
    while column not in "ABCDEFG":
        column = input("Column out of bounds! Enter again: ").upper()
    row=input("Enter row number (1 to 7): ")
    while row not in "1234567":
        row = input("Row out of bounds! Enter again: ")
    
    rowNo = int(row)-1
    colNo = grid[column]

    while board[rowNo][colNo] == '-':
        print("You already guessed that area! Try again.")
        column = input("Enter Column (A to G)  : ").upper()
        while column not in "ABCDEFG":
            column = input("Column out of bounds! Enter again: ").upper()
        row = input("Enter row number (1 to 7)  : ")
        while row not in "1234567":
            row = input("Row out of bounds! Enter again: ")
        
        rowNo = int(row)-1
        colNo = grid[column]
    return rowNo,colNo

#Dialogue:
def dialogue():
    print(END,nightmareRajat,sep="\n")
    scroll([boldred],"I have become ")
    scroll([boldred],"D E A T H . . . ",0.10)
    scroll([boldred],"the destroyer of worlds!")
    clear()
    scroll([boldred],"Fear me and my eternal power.")
    clear(50,2)
    print(nightmareRajat,"\n")
    scroll([boldred],"I AM RAJAT! ",0.05)
    scroll([boldred],"AND YOU SHALL FALL BEFORE ME!")
    clear()
    scroll([boldred],"FEE FII FOO FUM!!!",0.05)
    clear(50,4)
    print(END)

#Main Game:
def game():
    #Creating Player's Board
    global boardSize
    boardSize = 7
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
    grid = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}

    #Dialogue:
    dialogue()
    
    #Player Placing Ships
    placePlayerShip(playerBoard)
    clear(25,1)
    
    #Computer Placing Ships:
    csPlaceShip(csBoard)

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
    
    #Guessing Time:
    playerHits = 0
    csHits = 0
    
    while True:
        showBoard(playerGuess)
        print("It's time to fire your cannon!")
        rowNo,colNo = playerAttack(playerGuess)
        
        while playerGuess[rowNo][colNo]!=' ':
            print("Those coordinates have already been destroyed!")
            t.sleep(1)
            rowNo,colNo = playerAttack(playerGuess)
        
        if csBoard[rowNo][colNo]=='X':
            playerGuess[rowNo][colNo] = 'X'
            print("Your cannon has hit one of the enemy's battleships")
            playerHits+=1
            t.sleep(1)
            if playerHits==4:
                print(END,nightmareRajat,sep="\n")
                clear()
                scroll([boldgreen],"I have seen many warriors rise and fall")
                clear()
                scroll([boldgreen],"but not one of this power.")
                clear()
                scroll([boldgreen],"You have ")
                scroll([boldyellow],"*cough cough* ",0.05)
                scroll([boldgreen],"beaten me...")
                clear(50,2)
                scroll([boldcyan],"You have beaten the mighty Rajat and now rule the galaxy.")
                print(END)
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
            if csHits==4:
                print(nightmareRajat)
                scroll([boldred],"Did your puny mind really think that you could beat me?")
                clear()
                scroll([boldred],"If you wish to defeat me, TRAIN FOR ANOTHER 1000 YEARS. ")
                scroll([boldred],"M O R T A L .",0.1)
                clear(50,2)
                scroll([boldcyan],"You have lost against the universally undefeated ")
                scroll([boldred],"nightmare... Rajat.")
                clear()
                scroll([boldcyan],"And he has to say this to you again...")
                clear(50)
                print(END,nightmareRajat,sep="\n")
                scroll([boldred],"L + Ratio + *every single insult in existence*")
                break
        
        else:
            csGuess[csRow][csCol] = '-'
            print("The enemy missed their shot!")
            clear(1,1)
