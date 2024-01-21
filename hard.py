import time
import random
def clear2():
    for hu in range(24):
        print("")
def secretbord(board):
    print("     A     B    C    D     E  ")
    print(" ━━━━━━━━━━━━━━━━━━━━━")
    row_number=1
    for row in board:
        print(row_number,end=' ┃ ')
        for cell in row:
            if cell=='X':
                print(' ' + ' ' + ' ┃', end=' ')
            else:
                print(' ' +str(cell) + ' ┃', end=' ')
        print()
        print(" ━━━━━━━━━━━━━━━━━━━━")
        row_number+= 1

def showbord(board):
    print("     A     B    C    D     E  ")
    print(" ━━━━━━━━━━━━━━━━━━━━━")
    row_number=1
    for row in board:
        print(row_number, end=' ┃ ')
        for cell in row:
            print(' ' + str(cell) + ' ┃', end=' ')
        print()
        print(" ━━━━━━━━━━━━━━━━━━━━")
        row_number+=1

def clear():
    time.sleep(1)
    for _ in range(40):
        print("")

def userattack(board):
    column=input("Column (A to E): ").upper()
    while column not in "ABCDE":
        print("That column is wrong  It should be either A, B, C, D, or E")
        column = input("Column (From A to E): ").upper()
    row = input("Enter the row number (1 to 5): ")
    while row not in "12345":
        print("That row is wrong! It should be 1, 2, 3, 4, or 5")
        row = input("Enter a Row (1 to 5): ")    
    rowno=int(row) - 1
    
    colno =letternumgrid[column]
    
    while board[rowno][colno]=='X':
        print("ARIGH! You may not fire on to your own battle ship?")
        column = input("Column (A to E): ").upper()
        while column not in "ABCDE":
            print("That column is wrong! It should be A, B, C, D, or E")
            column=input("Column (A to E): ").upper()
        row=input("Enter the row number (1 to 5): ")
        while row not in "12345":
            print("That row is wrong! It should be 1, 2, 3, 4, or 5")
            row =input("Enter row Row (1 to 5): ")
        
        rowno=int(row) - 1
        colno=letternumgrid[column]
    return rowno,colno

def placeship(board):
    for n in range(2):
        rowno=random.randint(0,bordsiz-1)
        colno=random.randint(0,bordsiz-1)
        while board[rowno][colno] == 'X':
            rowno=random.randint(0,bordsiz-1)
            colno=random.randint(0,bordsiz-1)
        board[rowno][colno]='X'

def game():
    print("General You may place 2 Battle Ships in Strategic positions now :")
    showbord(board)
    for _ in range(2):
        print("PLACE BATTLE SHIP", _ + 1)
        rowno, colno = userattack(board)
        while board[rowno][colno]=='X':
            print("Argh ! One of our battalion Ships is already there!")
            rowno, colno = userattack(board)
        board[rowno][colno]='X'
        clear()
        showbord(board)

    print("The Great Napolean Is Sending his Fleet! Prepare for bloodshed:")
    placeship(csbord)
    placeship(csbord)
    clear()
    secretbord(csbord)

    bordguess=[]
    for e in range(bordsiz):
        row=[]
        for e in range(bordsiz):
            row.append(' ')
        bordguess.append(row)
    playerchance=0
    cschance=0
    chances=7
    while playerchance <2 and cschance <2 and chances > 0:
        print("Its Time General FIRE THE CANNON ")
        rowno,colno=userattack(board)

        if bordguess[rowno][colno] != ' ':
            print("Those coordinates have aldready been Destroyed")
            time.sleep(1)
            continue

        if csbord[rowno][colno]=='X':
            print("THE CANNON HAS HIT NAPOLEANS BATTALION!")
            time.sleep(1)
            bordguess[rowno][colno]='X'
            playerchance += 1
        else:
            bordguess[rowno][colno]='.'
            print("Argh It was a Flobber the cannon missed")
            time.sleep(1)

        clear()
        print("ENEMY CANNON FIRED TAKE COVER!!!!:")
        csrow = random.randint(0,bordsiz-1)
        cscolumn = random.randint(0,bordsiz-1)

        while bordguess[csrow][cscolumn]!=' ':
            csrow = random.randint(0,bordsiz-1)
            cscolumn = random.randint(0,bordsiz-1)

        if board[csrow][cscolumn]=='X':
            print("ABANDON SHIP ONE OF OUR WAR FLEETS HAVE BEEN HIT!!")
            bordguess[csrow][cscolumn] = 'X'
            cschance+=1
        else:
            bordguess[csrow][cscolumn] = '.'
            print("Yearhhh! The Enemy cannon has missed thier shot")
        showbord(bordguess)
        chances-=1
        print('Cannons Left:', chances)

    if playerchance==2:
        clear()
        print("""           %%%%%%###%%%%%%%%%%             
         %%%#####%%%#####%%%%%%%%%%%%        
      %%#######################%%%%%%%%      
    %%##%###################**###%%%%%%%%    
   %%#%####################**==+##%%%%%%%%   
  %%#%#######################**###%%%%%%%%%  
 %%#############################%%%%%%%%%%%% 
 %#############################%%%%%%%%%%%%% 
 %#%#########################%%%%%%%%%%%%%%%%
%%%%#######################%%%%%%%%%%%%%%%%%%
%%%%%%%%%################%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%******+#%%%%%%%*+++++++#%%%%      			"Argh You have Defeated me...For now mortal"
     %**%%*+*+#%**++*#%+***+*##++++#%++*%    
    %++*#%+++++=+**+*===++**++++++=#%*+=*    
    %++**%+=++++++++*===++=++++++==*#+++#    
    %#+++*========+*++++++*+=======+*++*%    
      ##**=======++++++++*+++======+##%      
      %###======+====+**+====+=====+%%       
     %####*=======**********======+###%      
    %########*======++++++=====+#%#####%     
   %%#######%%#++==+**+*++==***#%%######%    
   %#####*#***###+=====+++*+###***######%%   
   %#############+=======+*+*###########%%   
   %%############+======++*+*###########%%   
    %%########+*#*===++*+*++##**########%    
       %%%%%##%%%%%%**#%%##%%%%%#%%%%%%%   """)
        time.sleep(1)
    elif cschance==2:
        clear()
        print("""           %%%%%%###%%%%%%%%%%             
         %%%#####%%%#####%%%%%%%%%%%%        
      %%#######################%%%%%%%%      
    %%##%###################**###%%%%%%%%    
   %%#%####################**==+##%%%%%%%%   
  %%#%#######################**###%%%%%%%%%  
 %%#############################%%%%%%%%%%%% 
 %#############################%%%%%%%%%%%%% 
 %#%#########################%%%%%%%%%%%%%%%%
%%%%#######################%%%%%%%%%%%%%%%%%%
%%%%%%%%%################%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%******+#%%%%%%%*+++++++#%%%%      
     %**%%*+*+#%**++*#%+***+*##++++#%++*%    
    %++*#%+++++=+**+*===++**++++++=#%*+=*    
    %++**%+=++++++++*===++=++++++==*#+++#    
    %#+++*========+*++++++*+=======+*++*%    "NO ONE SHALLL DEFEAT THE GREAT NAPOLEAN YEARGHHHH"
      ##**=======++++++++*+++======+##%      
      %###======+====+**+====+=====+%%       
     %####*=======**********======+###%      
    %########*======++++++=====+#%#####%     
   %%#######%%#++==+**+*++==***#%%######%    
   %#####*#***###+=====+++*+###***######%%   
   %#############+=======+*+*###########%%   
   %%############+======++*+*###########%%   
    %%########+*#*===++*+*++##**########%    
       %%%%%##%%%%%%**#%%##%%%%%#%%%%%%%   """)
        time.sleep(1)
    else:
        print("You both ran out of Ammo. RETREAT!")
    ch=input("Shall you challenege Napolean Again??").upper()
    if ch=="YES":
        game()
    else:
        clear()
bordsiz=5
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
letternumgrid={'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,}
game()
