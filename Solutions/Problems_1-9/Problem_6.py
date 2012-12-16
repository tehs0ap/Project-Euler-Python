'''
Created on 2012-12-06

@author: Marty
'''
'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural 
numbers and the square of the sum.
'''
import time
  
startTime = time.time()
sumSquares = 0
squareSum = 0
number = 0

for i in range(1,101):
  sumSquares += i**2
  squareSum += i

squareSum = squareSum**2

number =  squareSum - sumSquares 
  
print number
print "Time Elapsed: " + str(time.time() - startTime)