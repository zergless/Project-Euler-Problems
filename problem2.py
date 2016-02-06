#!/usr/bin/python3
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""
fibbonacci0=1
fibbonacci1=2
total=2

while (fibbonacci1 or fibbonacci0) < 4000000:
  fibbonacci0 += fibbonacci1
  if (fibbonacci0%2 == 0) and (fibbonacci0 < 4000000):
    total += fibbonacci0
  fibbonacci1 += fibbonacci0
  if (fibbonacci1%2 ==0) and (fibbonacci1 < 4000000):
    total += fibbonacci1
print (fibbonacci0)
print (fibbonacci1)
print (total)
