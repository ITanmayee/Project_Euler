# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum .
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_square_difference(limit ) :
    sum_of_digit = sum(i for i in range(1,limit + 1))
    sum_of_square_of_digits = sum(i**2 for i in range(1, limit + 1))
    return str(sum_of_digit ** 2 - sum_of_square_of_digits)

print(sum_square_difference(100))
