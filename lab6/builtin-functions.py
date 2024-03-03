import time

#TASK 1

"""
def mult(lst):
    ans = 1
    for i in range(len(lst)):
        ans *= lst[i]
    return ans
lst = [1,4,46,2,5]
print(mult(lst))
"""

#TASK 2

"""
def count(string):
    upcount = lowcount = 0
    for char in string:
        if char.islower()s:
            lowcount += 1
        else:
            upcount += 1
    return upcount, lowcount
print(count("AliBi"))
"""

#TASK 3

"""
def palin(string):
    for i, j in zip(range(len(string)), reversed(range(len(string)))):
        if string[i] != string[j]:
            return False
    return True
"""

#TASK 4

"""
from time import sleep
def func(num, ms):
    sqrt = pow(num, 0.5)
    sec = ms/1000
    sleep(sec)
    print(f'Square root of {num} after {ms} miliseconds is {sqrt}')
func(25100, 2123)
"""

#TASK 5

"""
def func(tuple):
    return all(tuple)
tuple = (0, 1, 1)
print(func(tuple))
"""