'''
Created on 2012-12-06

@author: Marty
'''
'''
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import time

startTime = time.time()
mostTerms = 0
numWithMost = 0
number = 0
def calcNumTerms(n):
  termCount = 1 
  if n == 1:
    return termCount
  elif n % 2 == 0:
    termCount += calcNumTerms(n/2)
  else:
    termCount += calcNumTerms((3*n)+1)
  return termCount

for i in range(2,1000000):
  termCount = calcNumTerms(i)
  if termCount > mostTerms:
    mostTerms = termCount;
    numWithMost = i  
  
print numWithMost
print mostTerms
print "Time Elapsed: " + str(time.time() - startTime)
