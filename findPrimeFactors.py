
import math


s = 16

def isNumberWhole(s):
    if s == int(s):
        return True

def isNumberSquared(s):
    if math.sqrt(s) == int(math.sqrt(s)):
        return True

def isNumberPrime(s,primeNumbers):
    if primeNumbers.count(s) >= 1:
        return True

def numberFactors(s,primeNumbers):
    clear = True    
    f = []
    i = 0  
    while clear == True:
        try:
            if s % primeNumbers[i] == 0:
                s = s/primeNumbers[i]
                f.append(primeNumbers[i])
            else:
                i= i + 1
        except:
                clear = False
    clear = True
    if len(f) > 2:
        while clear == True:
            f.sort()
            f[0] = f[0] * f[1]
            f.pop(1)
            if len(f) <= 2:
                clear = False
    x = f[0]
    y = f[1]
    return x, y

def generatePrimes(s):
    p = []
    for num in range(1, s + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                    
            else:
                p.append(num)        
    return p
# primeNumbers = generatePrimes(s)
# isPrime = isNumberPrime(s,primeNumbers)
# if isPrime == True:    
#     x = s
#     y = 1
#     print("p")
# else :
#     squared = isNumberSquared(s)
#     if squared == True:
#         x = int(math.sqrt(s))
#         y = int(math.sqrt(s))
#         print("s")
# if isPrime == None and squared == None:
#     x, y = numberFactors(s,primeNumbers)
#     print("b")
# print(x, y)
