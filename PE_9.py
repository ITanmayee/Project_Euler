# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,a^2 + b^2 = c^2 . 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc .

def pythagorean_triplet(SUM):
 for a in xrange(1, SUM):
  for b in xrange(1, SUM):
   c = 1000-a-b
   if (a**2+b**2) == c**2 :
    return a*b*c

print(pythagorean_triplet(1000))

