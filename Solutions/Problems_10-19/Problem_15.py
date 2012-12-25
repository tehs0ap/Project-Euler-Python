'''
Created on 2012-12-06

@author: Marty
'''
'''
Starting in the top left corner of a 2x2 grid, 
there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?
'''
import time

startTime = time.time()

def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

print factorial(40)/(factorial(20)*factorial(20))
print "Time Elapsed: " + str(time.time() - startTime)
