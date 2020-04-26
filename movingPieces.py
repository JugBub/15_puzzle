# l =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
# i = True
# # a = 0
# # n = the number to switch with n

def wheresNumber(x,y,l,p):
    if p != True:
        i = True
        while i == True:
            c = [0,0,0,0] #t,l,r,b
            if l.index(0) == 0 and l.index(0) != x:  # tl
                c = [0,0,1,1]
                break
            if l.index(0) == x-1:  #tr
                c = [0,1,0,1]
                break
            if l.index(0) == (x*y-x): #bl
                c = [1,0,1,0]
                break
            if l.index(0) == (x*y-1): # br
                c = [1,1,0,0]
                break
            if l.index(0) % x == 0: # l
                c = [1,0,1,1]
                break
            if (l.index(0)+1) % x == 0: # r
                c = [1,1,0,1]
                break
            if l.index(0) < (x-1): # t
                c = [0,1,1,1]
                break
            if l.index(0) > x*y-1-x: # b
                c = [1,1,1,0]
                break
            c = [1,1,1,1] # c
            i = False
    else:
        c = [0,1,1,0]
    return c

def askForInput(x,y):  
    done = True
    while done == True:
        wAstr = input("what a?  ")
        try:
            wA = int(wAstr)
            a = wA
            if a <= x*y-1:
                done = False
            else:
                print("Try again")
        except:
            print("Try again")

    return a

def gettingOperations(x,y,c,n):
    o = [(n-x),(n-1),(n+1),(n+x)]#operations
    for i in range(len(c)):
        if c[i] == 0:
            o[i] = x*y
    i = True
    while i == True:
        if o.count(x*y) == 0:
            i = False
        else:
            for i in range(o.count(x*y)):
                o.remove(x*y)
    return o
def askForNumbers(x,y,l,c,a):
    n = l.index(0)
    TA = False
    done = True
    while done == True:
        if TA == True:
            a = askForInput(x,y)
        o = gettingOperations(x,y,c,n)
        if o.count(l.index(a)) >= 1:
            done = False
        else:
            print("Try again")
            TA = True
    return a
            

def switchPlaceInList(l,a):
    n = l.index(a) # gets index of a
    l.pop(n) # pops out a from list
    i = l.index(0) # takes index of 0
    l.pop(i) #pops out zero from list
    l.insert(i, a)
    l.insert(n, 0)
    return l


# switchPlaceInList(l,0)
# while i == True:
#     c = wheresNumber(4,4,l,isPrime)
#     a = askForNumbers(4,4,l,c)
#     switchPlaceInList(l,a)
#     print(l)
