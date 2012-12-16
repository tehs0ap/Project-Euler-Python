'''
Created on 2012-12-06

@author: Marty
'''
'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''
import time

startTime = time.time()

def doubleNumber(n):
  carry = 0;
  for i in range(0,len(n)):
    n[i] <<= 1
    n[i] += carry
    if (n[i] >= 1000000000):
      carry = 1
      n[i] -= 1000000000
    else:
      carry = 0;
      


limit = 1000
ints = limit / 29
number = [0]*(ints+1)
number[0] = 2
for i in range(2,limit+1):
  doubleNumber(number) 

stringNum = ""
for i in range(0, len(number)):
  stringNum += str(number[i])

sum = 0
for i in range(0, len(stringNum)):
  sum += int(stringNum[i])

'''
Also do-able but less cool
print str(2**1000)
test = 0
for i in range(0, len(str(2**1000))):
  test += int(str(2**1000)[i])
print test
'''
          
print number
print stringNum
print sum
print "Time Elapsed: " + str(time.time() - startTime)
