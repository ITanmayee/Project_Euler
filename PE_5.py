# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def ifDividesAll(limit) :
  for i in range(11, 21):
    if limit % i != 0:
      return False
  return True

def get_smallest_number(num) :
    num = 2520
    while True:
        if ifDividesAll(num):
            break
        else:
            num = num + 1
    return num

print(get_smallest_number(20))

