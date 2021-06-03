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

def get_primeFactors(num) :
    low_factors = [i for i in range(2 , (num // 2) + 1) if num % i == 0 ]
    high_factors = [num // i for i in low_factors]
    factors = set(low_factors + high_factors)
    prime_factors = [i for i in factors if is_prime(i) ]
    return prime_factors

print(get_primeFactors(646))

i = 100000
while i > 0:
    if len(get_primeFactors(i)) == 4:
        if len(get_primeFactors(i + 1)) == 4:
            if len(get_primeFactors(i + 2)) == 4:
                if len(get_primeFactors(i + 3)) == 4:
                    print(i)
                    break
    i += 1





