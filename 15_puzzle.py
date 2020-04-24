### imports
import importlib

import math

import findPrimeFactors as fpf

import createAndPrintList as cpl

### variables

### functions

def defineBoardSize():
    done = True
    while done == True:
        wSstr = input("what s?  ")
        try:
            wS = int(wSstr)
            s = wS
            done = False
        except:
            print("Try again")
    return s    

def isSWhole(s):
    if s == int(s):
        return True


### setup

s = defineBoardSize()
primeNumbers = fpf.generatePrimes(s)
isPrime = fpf.isNumberPrime(s,primeNumbers)
if isPrime == True:    
    x = s
    y = 1
else :
    squared = fpf.isNumberSquared(s)
    if squared == True:
        x = int(math.sqrt(s))
        y = int(math.sqrt(s))
if isPrime == None and squared == None:
    x, y = fpf.numberFactors(s,primeNumbers)
print(x, y)

### trash
