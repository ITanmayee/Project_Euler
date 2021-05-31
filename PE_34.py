# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

def get_digits(num) :
    return [int(i) for i in str(num)]

def get_factorial(n) :
    if n == 1 or n == 0:
        return 1
    else :
        return n * get_factorial(n - 1)

def is_curious_number(num) :
    digits = get_digits(num)
    factorial_of_digit = [get_factorial(i) for i in digits]
    if num == sum(factorial_of_digit) :
        return True

num = 3
Sum = 0
while num >= 2 :
    if is_curious_number(num) :
        Sum = Sum + num
    print(Sum)
    num += 1
