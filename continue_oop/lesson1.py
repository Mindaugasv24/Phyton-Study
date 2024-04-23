# import random

from random import randint

print(
    "---------------------------Temos Uzdaviniai: 24/04/22------------------------------"
)

"""1.Write a Python program to create a generator that generates the squares of numbers up to a given number."""


def generate_squares(n):
    """function representing range of numbers"""
    for num in range(1, n + 1):
        yield num**2
    for square in generate_squares(10):
        print(square)


"""2.Write a Python program to create a generator that yields "n" random numbers between a low and 
high number that are inputs."""


# def random_numbers(low, high, n):
#     """representing random numbers"""
#     for _ in range(n):
#         yield (random.randint(low, high))
# low = int(input("Enter the low number: "))
# high = int(input("Enter the high number: "))
# n = int(input("Enter the number of random numbers to generate: "))

# random_generator = random_numbers(low, high, n)
# for num in random_generator:
#     print(num)


# ------------Destytojo sprendimas:
# def generate_values(low, high, n):
#     for _ in range(n):
#         print(randint(low, high))
#
#
# low, high, n = [int(x) for x in input("ivesk 3 skaivius: ").split()]
#
# generate_values(low, high, n)

"""3.Write a Python program to create a generator that iterates over a string."""

# def string_iterator(s):
#     for i in s:
#         yield i
#     for i in my_generator:
#         print(i)
#
# my_string = "Hello, World!"
# my_generator = string_iterator(my_string)
#
# print(my_generator)

"""4.Write a Python program to create a Fibonacci series generator."""

# def fibonacci_generator(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# n = int(input("Enter the number of terms in the Fibonacci series: "))
# fib_sequence = list(fibonacci_generator(n))
#
# print("Fibonacci series:")
# for num in fib_sequence:
#     print(num)

"""5.Write a Python program to create a generator from a list that yields item from the list if it is a number."""

# def number_generator(items):
#     for item in items:
#         if isinstance(item, (int, float)):
#             yield item

# # Test the generator
# my_list = [1, 'apple', 2.5, 'orange', 5, 'banana']
# gen = number_generator(my_list)

# for num in gen:
#     print(num)

"""6.Create a list of tuples, each representing a person's information.
Each tuple contains the following information: (name: str, age: int, city: str, salary: float). 
Your task is to create Python generators to perform the following tasks:
Filtering Generator: Create a generator function that filters the people who are below a certain age threshold.
Mapping Generator: Create a generator function that maps the names of people to uppercase.
Aggregation Generator: Create a generator function that calculates the average salary of the selected group.
"""

person_info = [
    ("Alice", 30, "New York", 50000.0),
    ("Bob", 25, "Los Angeles", 60000.0),
    ("Charlie", 35, "Chicago", 70000.0),
    ("David", 40, "San Francisco", 80000.0),
    ("Emma", 28, "Houston", 55000.0),
    ("Frank", 33, "Miami", 65000.0),
    ("Grace", 45, "Seattle", 75000.0),
    ("Henry", 32, "Boston", 70000.0),
    ("Ivy", 27, "Atlanta", 60000.0),
    ("Jack", 29, "Denver", 58000.0),
]

def filter_people_by_age(person_info, age_threshold):
    for person in person_info:
        if person[1] < age_threshold:
            yield person


def map_names_to_uppercase(person_info):
    for person in person_info:
        yield (person[0].upper(), person[1], person[2], person[3])


def calculate_average_salary(person_info):
    total_salary = 0
    count = 0
    for person in person_info:
        total_salary += person[3]
        count += 1
        if count > 0:
            yield total_salary / count


filtered_people_gen = filter_people_by_age(person_info, 40)
for person in filtered_people_gen:
    print(person)

upper_cased_names_gen = map_names_to_uppercase(person_info)
for person in upper_cased_names_gen:
    print(person)

average_salary_gen = calculate_average_salary(person_info)
for avg_salary in average_salary_gen:
    print(avg_salary)
