import movingPieces as mP

import random

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

def askForRandomInput(x,y,c,l):
    i = True
    while i == True:
        n = l.index(0)
        o = mP.gettingOperations(x,c,n)
        o.sort()
        r = random.choices(o)
        r = r[0] + 1
        if r != x*y:
            i = False
    print(r)
    return r
def moveZeroRandom(l):
    mP.switchPlaceInList(l,4)


# i = 0
# while i < 100:
#     c = mP.wheresNumber(4,4,l,False)
#     r = askForRandomInput(4,4,c)
#     a = mP.askForNumbers(4,4,l,c,r)
#     l = mP.switchPlaceInList(l,a)
#     i = i+1
# print(l)