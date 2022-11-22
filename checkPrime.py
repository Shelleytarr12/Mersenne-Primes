#!/usr/bin/env python

from math import sqrt
def is_prime ( p ):
  if p == 2:
    return True # Lucas-Lehmer test only works on odd primes
  elif p <= 1 or p % 2 == 0:
      return False
  else:
    for i in range(3, int(sqrt(p))+1, 2 ):
      if p % i == 0:
          return False

    return True


if __name__ == '__main__':
    primes=[]
    upper_val=int(input("Enter a number for upper bound (starting at 1): "))

    for i in range(1,upper_val+1):
        if is_prime(i):
            primes.append(i)
    print(primes)
