'''
Created on 2012-12-06

@author: Marty
'''
'''
Euler published the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 
is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n**2  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. 
The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n**2 + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.
'''
import time

startTime = time.time()
nMax = 0
aMax = 0
bMax = 0

#Generates list of primes up to limit
def primes_sieve(limit):
  a = [True] * limit  # Initialize the primality list
  a[0] = a[1] = False
    
  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in xrange(2*i, limit, i):  # Mark factors non-prime        
        a[n] = False
   
primes = list(primes_sieve(100000))   
        
def isPrime(p):
  i = 0
  while primes[i] <= p:
    if primes[i] == p:
      return True
    i += 1
  return False

primeTerms = list(primes_sieve(1000))

print primes;
for b in primeTerms:
    for a in primeTerms:
      for sign in [-1,1]:
        n = 0
        while isPrime(n*n + sign*a*n + b):
          n += 1
          
        if n > nMax:
          nMax = n
          aMax = sign*a
          bMax = b

print nMax
print aMax
print bMax
print aMax * bMax      
print "Time Elapsed: " + str(time.time() - startTime)
