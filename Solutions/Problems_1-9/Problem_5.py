'''
Created on 2012-12-06

@author: Marty
'''
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import time
  
startTime = time.time()
number = 0

'''
Brute Force
************
divisible = False
while not divisible:
  divisible = True
  number += 1
  for i in range(1, 21):
    if number % i != 0:
      divisible = False
      break  
'''

primes = [2, 3, 5, 7, 11, 13, 17, 19]
factors = dict()
largestPrimeFactor = dict()

def findFactors(number, primes):
  factors = dict()
  for i in range(0, len(primes)):
    power = 0
    while number % primes[i]**(power+1) == 0:
      power += 1
    factors[primes[i]] = power
  return factors

for i in range(1, 21):
  factors[i] = findFactors(i, primes)
  
for p in primes:
  largestPrimeFactor[p] = 0
  for i in range(1, 21):
    largestPrimeFactor[p] = max(largestPrimeFactor[p], factors[i][p])

number = 1
for prime, factor in largestPrimeFactor.iteritems():
  number *= prime**factor
  
print number
print "Time Elapsed: " + str(time.time() - startTime)