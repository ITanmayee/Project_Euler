# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def get_binary_number(decimal) :
    remainder = []
    while decimal != 0 :
        remainder.append(decimal % 2)
        decimal = decimal // 2 
    return ''.join(map(str, remainder[::-1])) 

def is_palindrome(word) :
    if word == word[::-1] :
        return True

print(sum([i for i in range(1000000) if is_palindrome(str(i)) and is_palindrome(get_binary_number(i))]))



