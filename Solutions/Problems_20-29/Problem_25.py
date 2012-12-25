'''
Created on 2012-12-06

@author: Marty
'''
'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''
import time

startTime = time.time()
previousTerms = [1,1]
currentTerm = 0
found = False
n=2

while not found:
  n+=1
  currentTerm = previousTerms[0]+previousTerms[1]
  previousTerms[0] = previousTerms[1]
  previousTerms[1] = currentTerm
  
  if currentTerm / 10**999 > 0 :
    found = True

print n
print "Time Elapsed: " + str(time.time() - startTime)