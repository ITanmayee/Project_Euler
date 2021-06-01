# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import math
def isPrime(n):
  for num in range(2,int(math.sqrt(n) + 1)):
    if n % num == 0:
      return False
  return True

count = 0

for num in range(2, 1000000):
  q = False
  num = str(num)
  for i in range(len(num)):
    if isPrime(int(num[i : ] +num[:i])):
      q = True
    else:
      q = False
      break
  if q:
    count+=1

print(count)
