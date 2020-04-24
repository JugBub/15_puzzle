# l =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
# i = True
# # a = 0
# # n = the number to switch with n

isPrime = False

def wheresNumber(x,y,l,p):
    if p != True:
        i = True
        while i == True:
            c = [0,0,0,0] #t,l,r,b
            if l.index(0) == 0:
                c = [0,0,1,1]
                break
            if l.index(0) == x-1:
                c = [0,1,0,1]
                break
            if l.index(0) == (x*y-x):
                c = [1,0,1,0]
                break
            if l.index(0) == (x*y-1):
                c = [1,1,0,0]
                break
            if l.index(0) % x == 0:
                c = [1,0,1,1]
                break
            if (l.index(0)+1) % x == 0:
                c = [1,1,0,1]
                break
            if l.index(0) < (x-1):
                c = [0,1,1,1]
                break
            if l.index(0) > x*y-1-x:
                c = [1,1,1,0]
                break
            c = [1,1,1,1]
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

def gettingOperations(x,c,n):
    o = [(n-x),(n-1),(n+1),(n+x)]#operations
    i = True
    c1 = 0
    while i == True:
        try:
            if c[c1] == 0:
                o[c1] = 0
                c1 = c1 + 1
            else:
                c1 = c1 + 1
        except:
            i = False
    i = True
    while i == True:
        if o.count(0) == 0:
            i = False
        else:
            for i in range(o.count(0)):
                o.remove(0)
    return o
def askForNumbers(x,y,l,c,a):
    n = l.index(0)
    TA = False
    done = True
    while done == True:
        if TA == True:
            a = askForInput(x,y)
        o = gettingOperations(x,c,n)
        

                        
        print(o)
        print(a)
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
