# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(n) :
  if n in [2,3,5,7]:
    return True
  if n% 2 == 0 :
    return False
  r = 3
  while r * r <= n:
    if n % r == 0:
      return False
    r += 2
  return True

def get_prime(limit) :
    primes = []
    num = 2
    while len(primes) < limit :
        if is_prime(num) :
            primes.append(num)
        num += 1
    return primes[-1]

print(get_prime(10001))

