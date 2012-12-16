'''
Created on 2012-12-06

@author: Marty
'''
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import time
 
startTime = time.time()
limit = 2000000L
primeSum = 0

def primes_sieve2(limit):
  a = [True] * limit  # Initialize the primality list
  a[0] = a[1] = False
  
  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in xrange(2*i, limit, i):  # Mark factors non-prime        
        a[n] = False
  
for p in primes_sieve2(limit):
  primeSum += p
     
print primeSum
print "Time Elapsed: " + str(time.time() - startTime)
