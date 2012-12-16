'''
Created on 2012-12-06

@author: Marty
'''
'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import time

def isPalindrome(number):
  numberString = str(number)
  if numberString == numberString[::-1]:
    return True
  else:
    return False
  
startTime = time.time()
largestPalindrome = 0
for a in reversed(range(100, 1000)):
  for b in reversed(range(100, 1000)):
    if isPalindrome(a * b) and (a * b) > largestPalindrome:
      largestPalindrome = a * b
  
print largestPalindrome
print "Time Elapsed: " + str(time.time() - startTime)