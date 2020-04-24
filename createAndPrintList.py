def createList(x,y):
    l = []
    n = 1
    for i in range(x*y):
        if n == x*y:
            n = 0

        l.append(n)
        n = n + 1
    return l

def printList(x,y,l):
    n = 0
    for i in range(y):
        for j in range(x):
            print("[%d]" % l[n], end= "")
            n = n + 1
        print("")
