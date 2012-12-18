'''
Created on 2012-12-06

@author: Marty
'''
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation 
of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''
import time
from math import factorial

startTime = time.time()
size = 10
availableDigits = [True] * size
target = 1000000
total = ""
start = 0

for digit in reversed(range(1,size+1)):
  
  variance = factorial(digit-1)
    
  i=1
  while start + (variance * i) < target: 
    i += 1
    
  count = 0  
  for key, value in enumerate(availableDigits):
    if value == True:    
      if count == i-1:
        total += str(key)
        availableDigits[key] = False
        break               
      count += 1
      
  start += variance*(i-1)

print total
print "Time Elapsed: " + str(time.time() - startTime)
