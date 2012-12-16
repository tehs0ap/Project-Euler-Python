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
primes = set([2])
primeCount = 1
number = 3

while len(primes) < 10001:
  isPrime = True
  for p in primes:
    #If divisible by prime factor then not a prime
    if number % p == 0:      
      number += 2
      isPrime = False
      break
  
  if isPrime:
    primes.add(number)
    number += 2
  
  
print number
print "Time Elapsed: " + str(time.time() - startTime)