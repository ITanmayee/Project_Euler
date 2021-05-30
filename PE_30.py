# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def get_digit_power_sum(n , power) :
    number = str(n)
    digits = [int(i) for i in number]
    return  sum([i ** power for i in digits])
def get_sum_nth_powers(n) :
    nth_powers = [i for i in range(2 , 10 ** (n + 1)) if i == get_digit_power_sum(i , n) ]
    return sum(nth_powers)

print(get_sum_nth_powers(5))
