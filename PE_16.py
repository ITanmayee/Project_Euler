# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def get_power(n) :
    return 2 ** n

def get_digits(n) :
    number = str(n)
    return [int(i) for i in number]

def get_sum_of_digits(n) :
    power = get_power(n)
    return sum(get_digits(power))

print(get_sum_of_digits(1000))
