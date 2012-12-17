'''
Created on 2012-12-06

@author: Marty
'''
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called 
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import time
from math import  sqrt

def d(n):
  sum = 0
  for i in range(1,(n/2)+2):
    if n % i == 0:
      sum += i
  return sum

startTime = time.time()
total = 0
limit = 10000

array = [False] * limit  # Initialize the primality list

for a in range(0,limit):
  if array[a] == True:
    continue
  b = d(a)
  if b >= 10000:
    continue
  if array[b] == True:
    continue
  if d(b) == a and a != b:
    array[a], array[b] = True,True
    total += a + b
  else:
    array[a] = True
    
print total
print "Time Elapsed: " + str(time.time() - startTime)
