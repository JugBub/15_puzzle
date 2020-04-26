### imports
import importlib

import math

import findPrimeFactors as fpf

import createAndPrintList as cpl

import movingPieces as mP

import shuffle as sh
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
done = False
while done == False:
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
    if isPrime != True:   
        break
    print("No primes")

### make and shuffle the board

listOfNumbers = cpl.createList(x,y)
correctList = listOfNumbers.copy()
done = False
while done == False:
    listOfNumbers = sh.shuffle(x,y,listOfNumbers)
    fakeList = listOfNumbers.copy()
    done = sh.checkShuffle(x,y,listOfNumbers)
    listOfNumbers = fakeList.copy()

### print the board

cpl.printList(x,y,listOfNumbers)

### Game
game = True
while game == True:
    if listOfNumbers == correctList:
        break    
    composition = mP.wheresNumber(x,y,listOfNumbers,isPrime)
    askedNumber = mP.askForInput(x,y)
    askedNumber = mP.askForNumbers(x,y,listOfNumbers,composition,askedNumber)
    listOfNumbers = mP.switchPlaceInList(listOfNumbers,askedNumber)

    #prints board again
    cpl.printList(x,y,listOfNumbers)
print("Congratulations")
### trash
