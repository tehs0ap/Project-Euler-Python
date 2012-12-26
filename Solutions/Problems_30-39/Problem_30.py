'''
Created on 2012-12-26

@author: Marty
'''
'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

import time
startTime = time.time()

sum = 0
digitPowers = [0**5, 1**5, 2**5, 3**5, 4**5, 5**5, 6**5, 7**5, 8**5, 9**5]

#Single digits don't count
for i in range(10,355001):
  number = i
  sumDigitPowers = 0
  
  while number > 0:
    digit = number % 10
    number /= 10
    sumDigitPowers += digitPowers[digit]
  
  if sumDigitPowers == i:
    sum += i
    
print sum
print "Time Elapsed: " + str(time.time() - startTime)
