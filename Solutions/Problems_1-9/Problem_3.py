'''
Created on 2012-12-06

@author: Marty
'''
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt
import time

startTime = time.time()

number = 600851475143

primes = set([2])
value = 3

while value < sqrt(number):
  isPrime = True
  for p in primes:
    if value % p == 0:
      isPrime = False
  
  if isPrime:
    primes.add(value)
    if number % value == 0:
      number /= value
  
  value += 2
            
print number
print "Time Elapsed: " + str(time.time() - startTime)