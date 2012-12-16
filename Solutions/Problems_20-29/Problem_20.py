'''
Created on 2012-12-06

@author: Marty
'''
from test.profilee import factorial
'''
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
import time

startTime = time.time()
total = 0

stringNum = str(factorial(100))
for i in range(0, len(stringNum)):
  total += int(stringNum[i])


print total
print "Time Elapsed: " + str(time.time() - startTime)
