import random

print('---------------------------Temos Uzdaviniai: 24/04/22------------------------------')

"""1.Write a Python program to create a generator that generates the squares of numbers up to a given number."""


def generate_squares(n):
    """function representing range of numbers"""
    for num in range(1, n + 1):
        yield num**2
    for square in generate_squares(10):
        print(square)

print()

"""2.Write a Python program to create a generator that yields "n" random numbers between a low and 
high number that are inputs."""


def random_numbers(low, high, n):
    """representing random numbers"""
    for _ in range(n):
        yield (random.randint(low, high))
    low = int(input("Enter the low number: "))
    high = int(input("Enter the high number: "))
    n = int(input("Enter the number of random numbers to generate: "))

    random_generator = random_numbers(low, high, n)
    for num in random_generator:
        print(num)