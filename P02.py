# ⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️Date:02-DEC-2025⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️

# Print numbers from 1 to N using recursion.

"""
def print_numbers(n,current=1):

    if current>n:
        return
    
    print(current)

    print_numbers(n,current+1)

print_numbers(10)

"""

# Print numbers from N to 1 using recursion.

"""
def print_num(n):

    if n==0:
        return
    
    print(n)

    print_num(n-1)

print_num(5)

"""

# 3. Find the sum of first N natural numbers.


"""
def find_sum(n):
    if n==0:
        return 0
    
    return n+find_sum(n-1)

print(find_sum(10))
"""


# 4. Find factorial of a number (classic).

"""
def fact(n):
    if n==0:
        return 1

    return n*fact(n-1)

print(fact(4))

"""

# Find power of a number: aⁿ
# Do it without using **
# Concept: Multiply + reduce exponent.


"""
def find_exp(a,n):

    if n==1:
        return a

    return a *find_exp(a,n-1)

print(find_exp(3,4))

"""

# 6. Print the digits of a number one-by-one.

# Example: 253 → 2 5 3
# Concept: Recursion + string/number conversion.

# ⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️Date:09-DEC-2025⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️⚡️








