def createList(x,y):
    l = []
    n = 0
    for i in range(x*y):
        l.append(n)
        n = n + 1
        i++ 1
    return l

def printList(x,y,l):
    n = 1
    
    for i in range(y):
        for j in range(x):
            if n == x*y:
                n = 0 
            print("[%d]" % l[n], end= "")
            n = n + 1
        print("")

l = createList(4,4)
print(l)
printList(4,4,l)