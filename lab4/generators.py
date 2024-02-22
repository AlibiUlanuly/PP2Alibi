#TASK 1
"""
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2
"""

#TASK 2
"""
def evennum_generator(N):
    for i in range(1, N+1):
        if i%2==0:
            yield i
n = int(input())
even_nums = evennum_generator(n)
for num in even_nums:
    print(num, end=", ")
"""

#TASK 3
"""
def divisible(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num
"""

#TASK 4
"""
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2
a = 3
b = 7

for square in squares(a, b):
    print(square)
"""

#TASK 5
"""
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
"""