# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

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
    sum = 0
    for i in range(2 , limit) :
        if is_prime(i) :
            sum += i
    return sum

print(get_prime(2000000))
