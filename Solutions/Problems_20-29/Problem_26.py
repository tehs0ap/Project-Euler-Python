'''
Created on 2012-12-06

@author: Marty
'''
'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2  =   0.5
1/3  =   0.(3)
1/4  =   0.25
1/5  =   0.2
1/6  =   0.1(6)
1/7  =   0.(142857)
1/8  =   0.125
1/9  =   0.(1)
1/10  =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
import time

startTime = time.time()
answer = 0

#Generates list of primes up to limit
def primes_sieve(limit):
  a = [True] * limit  # Initialize the primality list
  a[0] = a[1] = False
    
  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in xrange(2*i, limit, i):  # Mark factors non-prime        
        a[n] = False
        
primes = list(primes_sieve(1000))

for p in reversed(primes):
  if (p - 1) % 2 == 0:
    if (p-1)/2 in primes:
      print p
      break;

print "Time Elapsed: " + str(time.time() - startTime)
