#!/usr/bin/python3
count=1
total=0
while count <1000:
  if (count%3 == 0) or (count%5 == 0):
      total += count
  count += 1
print (total)

