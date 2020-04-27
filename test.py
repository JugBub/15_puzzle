import importlib

import findPrimeFactors

import random

# moduleName = input('Enter module name:')
# importlib.import_module("findPrimeFactors")

# x = 1.5

# print(( x - 1.5) * ( x + 3.2 ))




# print("t", end= "")
# print("t")

# n = 0
# c = [(n-21)]
# c[0] = 1
# print(c[0])

# x = 1
# n= 10
# c1 = 0
# i = True
# c = [1,0,0,1,1,0,1,1]
# o = [(n-x-1),(n-x),(n-x+1),(n-1),(n+1),(n+x-1),(n+x),(n+x+1)]#operations
# while i == True:
#     try:
#         if c[c1] == 0:
#             c.pop(c1)
#             o.pop(c1)
#         else:
#             c1 = c1 + 1
#     except:
#         i = False
# print(o)  

# a = [1,1,1,2]
# a.remove(1)
# print(a)

# l = [1]
# i = l[0]
# print (i)

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
# l1 = [9,11,12,3,8,6,13,5,4,15,0,14,1,2,7,10]
# i = 1
# x = 3
# y = 3
# l = [1,2,3,4,5,8,7,6,0]


### check if shuffle is possible

# j = l.index(0)
# n = 0
# i = x*y-1
# while i > j:
#     if (j+x) >= i:
#         break
#     else:
#         i = i-x
#         n = n+1
# while i > j:
#     n= n+1
#     i = i-1
# ic = 0
# i = 0
# for i in range(len(l)-1):
#     i = i+1

#     while l[i-1] != i:
#         s = l.index(i)
#         l.pop(s)
#         l.insert(s-1, i) 
#         ic = ic + 1
# if n % 2 == ic % 2:
#     done = True
# else:
#     done = False   


### shuffle board

# l = [1,2,3,4,5,6,7,8,0]

# lf = l
# l = []

# for i in range(3*3):
#     r = random.choices(lf)
#     r = r[0]
#     lf.pop(lf.index(r))
#     l.append(r)
    
#     print(l)





# print(n)
# print(ic)
# print(done)
