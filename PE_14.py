# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#  Which starting number, under one million, produces the longest chain?

def generate_collatz_sequence(num) :
    collatz = []
    while num != 1 :
        if num % 2 == 0:
            collatz.append(num)
            num = (num // 2)
        else :
            collatz.append(num)
            num = (3 * num) + 1
    return collatz

def get_length_of_collatz_sequence(num) :
    collatz_sequence = generate_collatz_sequence(num)
    return len(collatz_sequence) + 1    # 1 is added to the length because 1 is excluded from the sequence

lengths_of_collatz_sequence  = [(get_length_of_collatz_sequence(i) , i) for i in range(2, 1000000) ]

print(max(lengths_of_collatz_sequence))


