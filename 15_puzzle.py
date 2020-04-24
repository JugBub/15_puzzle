### imports
import importlib

import math

import findPrimeFactors as fpf

import createAndPrintList as cpl

import movingPieces as mP

import shuffle
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

### shuffle the board
listOfNumbers = cpl.createList(x,y)
i = 0
while i < 100:
    c = mP.wheresNumber(x,y,listOfNumbers,isPrime)
    r = shuffle.askForRandomInput(x,y,c,listOfNumbers)
    a = mP.askForNumbers(x,y,listOfNumbers,c,r)
    l = mP.switchPlaceInList(listOfNumbers,a)
    i = i+1
print(l)

### print the board



cpl.printList(x,y,listOfNumbers)

### Game
game = True
while game == True:
    composition = mP.wheresNumber(x,y,listOfNumbers,isPrime)
    askedNumber = mP.askForInput(x,y)
    askedNumber = mP.askForNumbers(x,y,listOfNumbers,composition,askedNumber)
    listOfNumbers = mP.switchPlaceInList(listOfNumbers,askedNumber)

    #prints board again
    cpl.printList(x,y,listOfNumbers)
### trash
