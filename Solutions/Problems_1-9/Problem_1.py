'''
Created on 2012-12-06

@author: Marty
'''

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
import time

startTime = time.time()
result = 0
for i in range(1000):
  if i % 3 == 0 or i % 5 == 0:
    result += i

print result
print "Time Elapsed: " + str(time.time() - startTime)