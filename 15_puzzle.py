### imports

import math

### variables



### functions

def defineBoardSize():
    done = True
    while done == True:
        wSstr = input("what x?  ")
        try:
            wS = int(wSstr)
            s = wS
            done = False
        except:
            print("Try again")
    return s    

def isSWhole(s):
    s

def isBoardSizeCorrect(s):
    s = math.sqrt(s)    
    try:
        s = s
    except:
        print("try again")
    return s


### main

s = defineBoardSize()
s = isBoardSizeCorrect(s)
print(s)

### trash