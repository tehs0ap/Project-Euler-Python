'''
Created on 2012-12-06

@author: Marty
'''
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
import time

startTime = time.time()
total = 0

def getDayOfWeek(y,m,d):
  t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
  y -= 1 if(m < 3) else 0
  return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7  

for year in range(1901, 2001):    
  for month in range(1,13):
    if (getDayOfWeek(year, month, 1) == 0):
      total += 1

print total
print "Time Elapsed: " + str(time.time() - startTime)
