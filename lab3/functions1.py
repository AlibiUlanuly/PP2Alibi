from itertools import permutations
import math
from random import randint
#TASK 1
"""
def con(grams):
    ounces = 28.3495231 * grams
    print(ounces)
con(193)
"""

#TASK 2
"""
def convert(F):
    C = (5 / 9) * (F - 32)
    return C
print(convert(51))
"""

#TASK 3
"""
def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = 2 * num_chickens + 4 * num_rabbits

        if total_legs == numlegs:
            return num_chickens, num_rabbits

    return None
"""

#TASK 4
"""
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5 + 1)):
        if num%i==0:
            return False
    return True

def filter_prime(numbers):
    return[num for num in numbers if isPrime(num)]
"""

#TASK 5
"""
def printpermutations(string):
    permuted_strings = permutations(string)
    for permuted_string in permuted_strings:
        print(''.join(permuted_string))
"""

#TASK 6
"""
def reversing(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ''.join(reversed_words)

    return reversed_sentence
"""

#TASK 7
"""
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
"""

#TASK 8
"""
def spy_game(nums):
    zero_count = 0
    seven_found = False
    for num in nums:
        if num == 0:
            zero_count+=1
        elif num == 7 and zero_count >= 2:
            seven_found = True
            break
    return seven_found
"""

#TASK 9
"""
def find_volume(radius):
    volume = 4/3 * math.pi * radius**3
    
    return volume
"""

#TASK 10
"""
def uniq(listofelem):
    found = []
    unilist = []
    for elem in listofelem:
        if elem not in found:
            found.append(elem)
            unilist.append(elem)
    return unilist
"""

#TASK 11
"""
def isPalindrome(word):
    for i, j in zip(range(len(word)), reversed(range(len(word)))):
        if word[i] != word[j]:
            return False
    return True
"""

#TASK 12
"""
def histogram(nums):
    for num in nums:
        for i in range(num):
            print('*', end = ' ')
        print()
histogram([4,9,7])
"""

#TASK 13
"""
print("Hello! What is your name?")
name = input("")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
random_int = randint(1, 20)
guess = 0
guess_count = 0
while guess != random_int:
    print("Take a guess.")
    guess = int(input())
    if guess < random_int:
        print("Your guess is too low.")
        guess_count+=1
    elif guess > random_int:
        guess_count+=1
        print("Your guess is too high.")
    else:
        guess_count+=1
        print(f"Good job, {name}! You guessed my number in {guess_count} guesses!")
        break
"""