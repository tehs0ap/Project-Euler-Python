'''
Created on 2012-12-26

@author: Marty
'''
'''
In England the currency is made up of pound, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1pound (100p) and 2pound (200p).
It is possible to make 2pound in the following way:

1x 1pound + 1x 50p + 2x 20p + 1x 5p + 1x 2p + 3x 1p
How many different ways can 2pound be made using any number of coins?
'''

import time
startTime = time.time()

upperBound = 200
values = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0]*(upperBound+1)
ways[0] = 1

for i in range(0, len(values)):
  for j in range(values[i], len(ways)):
    ways[j] += ways[j-values[i]]
    
print ways
print ways[upperBound]
print "Time Elapsed: " + str(time.time() - startTime)
