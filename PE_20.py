# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def get_fact(n) :
    if n == 1 or n == 0:
        return 1
    else :
        return n * get_fact(n - 1)
   
def get_digits(n) :
    number = str(n)
    return [int(i) for i in number]
 
def get_sum_of_digits(n) :
      factorial = get_fact(n)
      return sum(get_digits(factorial))
 
print(get_sum_of_digits(100))

