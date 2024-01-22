import time as t

def clear(lines=0,time=0):
    t.sleep(time)
    print("\n"*lines)

def scroll(str,time=0.025):
    for i in str:
        print(i,end="")
        t.sleep(time)