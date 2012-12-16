'''
Created on 2012-12-06

@author: Marty
'''
'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''
import time
from itertools import izip_longest

startTime = time.time()
number = 0
file = open('problem_13.txt', 'r+')
numbers = [file.readline() for i in range(0,100)]
carry = 0
segmentedNumber = list()
numberString = ""

for i in range(0,100):
  print numbers[i]
  segmentedNumber.append([numbers[i][k:k+1] for k in range(0, len(numbers[i]), 1)])
  
#len-1 to ignore newlines
for j in reversed(range(0, len(segmentedNumber[0])-1)):
  number = 0
  for i in range(0,100):
    number += int(segmentedNumber[i][j])
  number += carry
  carry = number / 10  
  numberString += str(number%10)  

#Last number is a special case
number /= 10
while number > 0:
  numberString += str(number%10)  
  number /= 10
  
print numberString[::-1]
print "Time Elapsed: " + str(time.time() - startTime)
