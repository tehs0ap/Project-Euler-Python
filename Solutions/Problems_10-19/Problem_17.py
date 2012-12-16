'''
Created on 2012-12-06

@author: Marty
'''
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''
import time

startTime = time.time()

ones = [0,3,3,5,4,4,3,5,5,4]
tens = [0,3,6,6,5,5,5,7,6,6]
teens = [3,6,6,8,8,7,7,9,8,8]
conjunction = 3
hundred = 7 # hundred
thousand = 8 #thousand

letterCount = 0
for i in range(1,1001):
  number = i
  print number
  t = number / 1000
  if t > 0:
    letterCount += ones[t] + thousand
    number -= (1000 * t)
  h = number / 100
  if h > 0:
    letterCount += ones[h] + hundred
    number -= (100 * h)
  d = number / 10
  if d == 1:
    number -= (10 * d)
    letterCount += teens[number]
  else:
    letterCount += tens[d]
    number -= (10 * d)
    letterCount += ones[number]
    
  if (t > 0 or h > 0) and (d > 0 or number > 0):
    letterCount += conjunction

print letterCount
print "Time Elapsed: " + str(time.time() - startTime)
