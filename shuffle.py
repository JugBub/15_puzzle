# import movingPieces as mP

import random

theList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

def shuffle(x,y,l):
    lf = l
    l = []

    for i in range(x*y):
        r = random.choices(lf)
        r = r[0]
        lf.pop(lf.index(r))
        l.append(r)   
    return l

def checkShuffle(x,y,l):
    j = l.index(0)
    n = 0
    i = x*y-1
    while i > j:
        if (j+x) >= i:
            break
        else:
            i = i-x
            n = n+1
    while i > j:
        n= n+1
        i = i-1
    ic = 0
    i = 0
    for i in range(len(l)-1):
        i = i+1

        while l[i-1] != i:
            s = l.index(i)
            l.pop(s)
            l.insert(s-1, i) 
            ic = ic + 1
    if n % 2 == ic % 2:
        done = True
    else:
        done = False
    return done    


done = False
while done == False:
    theList = shuffle(4,4,theList)
    fakeList = theList.copy()
    done = checkShuffle(4,4,theList)
    theList = fakeList.copy()
### TRASH
# def askForRandomInput(x,y,c,l):
#     i = True
#     while i == True:
#         n = l.index(0)
#         o = mP.gettingOperations(x,c,n)
#         o.sort()
#         r = random.choices(o)
#         r = r[0] + 1
#         if r != x*y:
#             i = False
#     print(r)
#     return r
# def moveZeroRandom(l):
#     mP.switchPlaceInList(l,4)


# i = 0
# while i < 100:
#     c = mP.wheresNumber(4,4,l,False)
#     r = askForRandomInput(4,4,c)
#     a = mP.askForNumbers(4,4,l,c,r)
#     l = mP.switchPlaceInList(l,a)
#     i = i+1
# print(l)