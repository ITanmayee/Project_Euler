# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def get_power(num) :
    return num ** num

def sum_power_series(limit) :
    return sum([get_power(i) for i in range(1, limit + 1)])

sum_of_series = str(sum_power_series(1000))
print(sum_of_series[len(sum_of_series) - 10:])
