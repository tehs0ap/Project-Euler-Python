'''
Created on 2012-12-06

@author: Marty
'''
'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import time
 
startTime = time.time()
result = 0
a,b,c = 0,0,0
m,n = 2,1
found = False

for m in range(2,1001):
  for n in range(1,m):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    
    if a+b+c == 1000:
      found = True
      break  
  if found:
    break

print a*b*c
print "Time Elapsed: " + str(time.time() - startTime)
