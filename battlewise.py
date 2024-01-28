from resources import *
import easy,medium,hard,nightmare

scroll([boldyellow],"""Before starting, set IO font to Consolas and font size to '11'
Ready?
""")
ready=input("").lower()
if "n" in ready:
    scroll([boldred],"Too bad.")
    print(END)
clear(50,1)
scroll([boldyellow],"For peak gaming experience, please maximize Shell.")
print(END)
clear(50,5)
ByteWiseLogo()
clear(50,3)
scroll([boldyellow],"In collaboration with Johan, Gleon and Nithin presents....")
print(END)
clear(50,3)
BattleWiseLogo()
clear(1,3)
scroll([boldcyan],"Do you dare to play?\n")
scroll([boldgreen]," 1. Yes\n")
scroll([boldred]," 2. No")
print(END)
if int(input(""))==1:
    clear(50)
    scroll([boldcyan],"Choose your difficulty level (with caution):\n")
    scroll([boldgreen]," 1. Easy       < Rajat :/ >\n")
    scroll([boldyellow]," 2. Medium     < GENGHIS KHAN >\n")
    scroll([boldred],""" 3. Hard       < NAPOLEON BONAPARTE >
               ^^^^^^^^^^^^^^^^^^^^ WARNING!\n""")
    scroll([boldred]," 4. NIGHTMARE  ")
    scroll([boldpurple],"[L O C K E D]")
    print(END)
    while True:
        diff=input("")
        while diff not in "1234":
            scroll([boldyellow],"That's not... a choice? Try again: ")
            diff=input("")
        if diff=="1":
            while True:
                scroll([boldyellow],"Looks like you're in for a pretty easy fight. Are you sure you wanna continue? (yes/yes): ")
                yes=input("").lower()
                if yes=="yes":
                    easy.game()
                    break
                elif yes=="nightmare69":
                    scroll([boldyellow],"Cheating moment.")
                    clear(time=1)
                    nightmare.game()
                    break
                else:
                    scroll([boldyellow],"That ain't a valid input!\n")
            break
        elif diff=="2":
            medium.game()
            break
        elif diff=="3":
            hard.game()
            break
        elif diff=="4":
            scroll([boldyellow],"What part of ")
            scroll([boldpurple],"'L O C K E D'")
            scroll([boldyellow]," did you not understand?\n")
            scroll([boldyellow],"Choose something valid this time: ")

else:
    clear(25)
    scroll([boldyellow],"B r u h . ",0.1)
    scroll([boldcyan],"Coward ahh move but alright!")
