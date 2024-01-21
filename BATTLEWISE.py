import random
import time
def clear2():
    for x in range(24):
        print("")
def secretbord(board):
    print("     A     B    C    D     E  ")
    print(" ━━━━━━━━━━━━━━━━━━━━━")
    row_number = 1
    for row in board:
        print(row_number, end=' ┃ ')
        for cell in row:
            if cell == 'X':
                print(' ' + ' ' + ' ┃', end=' ')
            else:
                print(' ' + str(cell) + ' ┃', end=' ')
        print()
        print(" ━━━━━━━━━━━━━━━━━━━━")
        row_number += 1

def showbord(board):
    print("     A     B    C    D     E  ")
    print(" ━━━━━━━━━━━━━━━━━━━━━")
    row_number = 1
    for row in board:
        print(row_number, end=' ┃ ')
        for cell in row:
            print(' ' + str(cell) + ' ┃', end=' ')
        print()
        print(" ━━━━━━━━━━━━━━━━━━━━")
        row_number += 1

def clear():
    time.sleep(1)
    for _ in range(40):
        print("")

def userattack(board):
    column = input("Column (A to E): ").upper()
    while column not in "ABCDE":
        print("That column is wrong! It should be A, B, C, D, or E")
        column = input("Column (A to E): ").upper()
    row = input("Enter the row number (1 to 5): ")
    while row not in "12345":
        print("That row is wrong! It should be 1, 2, 3, 4, or 5")
        row = input("Row (1 to 5): ")
    
    rowno = int(row) - 1
    colno = letternumgrid[column]

    while board[rowno][colno] == 'X':
        print("You can't attack your own battleship location!")
        column = input("Column (A to E): ").upper()
        while column not in "ABCDE":
            print("That column is wrong! It should be A, B, C, D, or E")
            column = input("Column (A to E): ").upper()
        row = input("Enter the row number (1 to 5): ")
        while row not in "12345":
            print("That row is wrong! It should be 1, 2, 3, 4, or 5")
            row = input("Row (1 to 5): ")
        
        rowno = int(row) - 1
        colno = letternumgrid[column]

    return rowno,colno

def game():
    print("Place your battleships:")
    showbord(board)
    for _ in range(2):
        print("Place ship ", _ + 1)
        rowno, colno = userattack(board)
        while board[rowno][colno] == 'X':
            print("You already placed a battleship there!")
            rowno, colno = userattack(board)
        board[rowno][colno] = 'X'
        clear()
        showbord(board)

    print("Computer placing battleships:")
    placeship(csbord)
    placeship(csbord)
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
    chances=3

    while playerchance < 2 and cschance < 2 and chances > 0:
        print("Your turn to guess:")
        rowno,colno=userattack(board)

        if bordguess[rowno][colno] != ' ':
            print("You have already guessed that place ")
            continue

        if csbord[rowno][colno] == 'X':
            print("HIT!")
            bordguess[rowno][colno] = 'X'
            playerchance += 1
        else:
            bordguess[rowno][colno] = '.'
            print("MISSED")

        clear()
        print("THE ENEMY HAS FIRED THIER CANNON:")
        csrow = random.randint(0, bordsiz - 1)
        cscolumn = random.randint(0, bordsiz - 1)

        while bordguess[csrow][cscolumn] != ' ':
             csrow = random.randint(0, bordsiz - 1)
             cscolumn = random.randint(0, bordsiz - 1)

        if board[csrow][cscolumn] == 'X':
            print("The computer HIT one  your battleships!")
            bordguess[csrow][cscolumn] = 'X'
            cschance += 1
        else:
            bordguess[csrow][cscolumn] = '.'
            print("The Enemy MISSED!")

        showbord(bordguess)
        chances -= 1
        print('Chances left :', chances)

    if playerchance == 2:
        print("Congratulations! You sank all enemy  battleships!")
    elif cschance == 2:
        print("Sorry, Enemy defeated you Better luck next Life!")
    else:
        print("You both ran out of Ammo. RETREAT!")
print("Please maximize shell window for best experience.....")
time.sleep(4)
print("""                                
                                    @@@@@@                                 
                                    @@@@@@                                 
                                    @@@@@@                                 
                  @@@@@     @@@ @@@ @@@@@@ @@@@@@@     @@@@@@              
                  @@@@@      @@@@   @@@@@@    @@       @@@@@               
                  @@@@@@      @@    @@@@@@    @@       @@@@@               
                  @@@@@       @@    @@@@@@    @@       @@@@@@              
                                    @@@@@@                                 
                                    @@@@@@                                 
                                    @@@@@@@@@@@@@@@@@@@@@@@@@              
                                    @@@@@@@@@@@@@@@@@@@@@@@@@              
                                     @@@@@@@@@@@@@@@@@@@@@@@               
                                                                           
               @@@@@@@@@@@@@@@@@@@@@@                                      
             @@@@@@@@@@@@@@@@@@@@@@@@@                                     
              @@@@@@@@@@@@@@@@@@@@@@@@                                     
                                 @@@@@                                     
                                 @@@@@                                     
                                 @@@@@                                     
               @@ @@@ @@     @@  @@@@@   @@@@@    @@@@@@                   
                @@@@@@@@     @@  @@@@@  @@@       @@@                
                @@@ @@@      @@  @@@@@  @@@@@@    @@@@@@                   
                 @@  @       @@  @@@@@   @@@@     @@@@@@                    
                                 @@@@@                                     
                                 @@@@@                                     
                                 @@@@@                                     
                                 @@@@@""")
time.sleep(2)
clear()
print("Presents........")
clear2()
time.sleep(2)
clear()
print("""                          
  @@@@@@@     @@    @@@@@@@@@@@@@@@@@@@@    @@@@@@@        
  @@@@@@@@   @@@@      @@@     @@@   @@@    @@@@@@         
  @@@@@@@@   @@@@@     @@@     @@@   @@@@   @@@@@@@        
  @@@@@@@@  @@@ @@@    @@@     @@@@  @@@@   @@@@           
  @@@@@@@@@ @@@@@@@@   @@@     @@@@  @@@@@@@ @@@@@@        
  @@@@@@@@ @@@@  @@@@  @@@     @@@    @@@@@@  @      ==    
              :--=+==========++++=+++++++++++++++++++++    
  +++++++++++++++++++++++++++++++++++++++++++++++++++++    
  +++++++++++++++++++++++++++++++++++++++++++++++++++++    
  +++++++++++++++++++++++++++++++++++++++++++++++++++++=   
  ++++++++++++++++++++++++++++++++++++++++++++++++++=+++   
  +++++++++++++++++++++++++++++++++++++=     
  +++++++++++++++++++++=+++++++         
  +++++++++==++=  =+=   =+++++++=      
  +++++++++   +++==+= +++=  =++++       
  ++++++++=     =++++++=    +++++=                      
  ++++++++++++++++++++++++++++++++                         
  ++++++++      +++++++=     +++++                         
  ++==++++=    ++=+++=++=   =++++=                         
  ==  +++++  ++=  =+=  =++= +++++                          
       +++++++=   =+=    =++++++                           
        =+++++=   =+=  ==++++++                            
         =+++++++++++++++++++=                             
            =+++++++++++++=         """)
time.sleep(2)
clear()
bordsiz = 5
board = []
for _ in range(bordsiz):
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

letternumgrid= {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,}
def placeship(board):
    for n in range(2):
        rowno = random.randint(0, bordsiz - 1)
        colno = random.randint(0, bordsiz - 1)
        while board[rowno][colno] == 'X':
            rowno = random.randint(0, bordsiz - 1)
            colno = random.randint(0, bordsiz - 1)
        board[rowno][colno] = 'X'
game()
