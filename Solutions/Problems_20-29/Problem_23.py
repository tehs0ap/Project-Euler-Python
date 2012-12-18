'''
Created on 2012-12-06

@author: Marty
'''
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called 
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be 
written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that 
all integers greater than 28123 can be written as the sum of two abundant numbers. However, this 
upper limit cannot be reduced any further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import time
from math import sqrt
startTime = time.time()
limit = 28124
total = 0
array = list()
sumAbundant = [False] * limit

#sum of positive divisors function
def sumOfDivisors(number):
  n = number
  sum = 1
  for k in range(2,int(sqrt(n)+1)):
    p = 1
    while n % k == 0:
      p = (p*k)+1
      n/=k
    sum *= p
  if n>1:
    sum *= n+1
  #aliquot sum
  return sum #- number 

def d(n):
  sum = 0
  for i in range(1,(n/2)+2):
    if n % i == 0:
      sum += i
  return sum

for i in range(2,limit):
  if sumOfDivisors(i) > (2 * i) and i!=0:
    array.append(i)

for x in array:
  for y in array:
    if x+y >= limit:
      continue
    sumAbundant[x+y]=True

for key,value in enumerate(sumAbundant):
  if(not value):
    total += key

print total
print "Time Elapsed: " + str(time.time() - startTime)
