#!/usr/bin/env python

from math import sqrt
primes=[]
def is_prime ( p ):
  
  if p == 2: 
    primes.append(p)
    return True # Lucas-Lehmer test only works on odd primes
  elif p <= 1 or p % 2 == 0: 
      return False
  else:
    for i in range(3, int(sqrt(p))+1, 2 ):
      if p % i == 0: 
          return False
    primes.append(p)
    return True
  
  if is_prime(p):
    primes.append(p)
    
def is_mersenne_prime ( p ):
  for i in primes:
    print(i)
  for i in primes:
    x=2**i-1
    if x in primes:
      print(x,'true')

  

if __name__ == '__main__':

    high_val=int(input("Enter a number for upper bound (starting at 1)"))
  
    for x in range(1,high_val+1):
        p=x
        
        is_prime(p)
    is_mersenne_prime(p)

