# The Fibonacci sequence is defined by the recurrence relation:
# F(n) = F(n-1) + F(n-2), where F1 = 1 and F2 = 1.
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def get_fibonacci(term) :
    fib =[]
    f1 = 0
    f2 = 1
    f3 = f1 + f2
    fib.append(f1)
    fib.append(f2)
    while len(str(f3)) < term :
        fib.append(f3)
        f1 , f2 = f2 , f3
        f3 = f1 + f2
    return len(fib)

print(get_fibonacci(1000))

