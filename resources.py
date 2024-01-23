import time as t
import random as r

def clear(lines=0,time=0):
    t.sleep(time)
    print("\n"*lines)

def scroll(list,str,time=0.025):
    #FORMAT: scroll([color,style,etc.],"str")
    if len(list)==1:
        for i1 in str:
            print(list[0],i1,sep="",end="")
            t.sleep(time)
    elif len(list)==2:
        for i2 in str:
            print(list[0],list[1],i2,sep="",end="")
            t.sleep(time)
    elif len(list)==3:
        for i3 in str:
            print(list[0],list[1],list[2],i3,sep="",end="")
            t.sleep(time)
    elif len(list)==4:
        for i4 in str:
            print(list[0],list[1],list[2],list[3],i4,sep="",end="")
            t.sleep(time)

tips=["There's a secret in the Easy level. Let's see if you can find it ;)",
      "ByteWise will never ask for your password.",
      "Entering a secret letter will grant you the power of the G o d s .",
      "Follow @bytewise11 on instagram.",
      "I hope this is the best game Irfana maam has ever seen."]

#NORMAL
black = "\u001b[0;30m"
red = "\u001b[0;31m"
green = "\u001b[0;32m"
yellow = "\u001b[0;33m"
blue = "\u001b[0;34m"
purple = "\u001b[0;35m"
cyan = "\u001b[0;36m"
white = "\u001b[0;37m"

blackBG = "\u001b[0;40m"
redBG = "\u001b[0;41m"
greenBG = "\u001b[0;42m"
yellowBG = "\u001b[0;43m"
blueBG = "\u001b[0;44m"
purpleBG = "\u001b[0;45m"
cyanBG = "\u001b[0;46m"
whiteBG = "\u001b[0;47m"

#BOLD
boldblack = "\u001b[1;30m"
boldred = "\u001b[1;31m"
boldgreen = "\u001b[1;32m"
boldyellow = "\u001b[1;33m"
boldblue = "\u001b[1;34m"
boldpurple = "\u001b[1;35m"
boldcyan = "\u001b[1;36m"
boldwhite = "\u001b[1;37m"

#ITALIC
italicblack = "\u001b[3;30m"
italicred = "\u001b[3;31m"
italicgreen = "\u001b[3;32m"
italicyellow = "\u001b[3;33m"
italicblue = "\u001b[3;34m"
italicpurple = "\u001b[3;35m"
italiccyan = "\u001b[3;36m"
italicwhite = "\u001b[3;37m"

#UNDERLINE
underlineblack = "\u001b[4;30m"
underlinered = "\u001b[4;31m"
underlinegreen = "\u001b[4;32m"
underlineyellow = "\u001b[4;33m"
underlineblue = "\u001b[4;34m"
underlinepurple = "\u001b[4;35m"
underlinecyan = "\u001b[4;36m"
underlinewhite = "\u001b[4;37m"

#NEGATIVE
negativeblack = "\u001b[7;30m"
negativered = "\u001b[7;31m"
negativegreen = "\u001b[7;32m"
negativeyellow = "\u001b[7;33m"
negativeblue = "\u001b[7;34m"
negativepurple = "\u001b[7;35m"
negativecyan = "\u001b[7;36m"
negativewhite = "\u001b[7;37m"

#CROSSED
crossedblack = "\u001b[9;30m"
crossedred = "\u001b[9;31m"
crossedgreen = "\u001b[9;32m"
crossedyellow = "\u001b[9;33m"
crossedblue = "\u001b[9;34m"
crossedpurple = "\u001b[9;35m"
crossedcyan = "\u001b[9;36m"
crossedwhite = "\u001b[9;37m"

END = "\033[0m"
