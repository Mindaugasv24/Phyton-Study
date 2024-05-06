from functools import reduce

print("--------------Functions Exsersize 2:24/04/23----------------------")

"""1.Write a Python program to triple all numbers of a given list of integers.
Use Python map()"""


def check_triple_numbers(num_list):
    return list(map(lambda x: x*3, num_list))


numbers = [5, 4, 8, 3, 6]
tripled_numbers = check_triple_numbers(numbers)

# print(tripled_numbers)

"""2.Write a Python program to square the elements of a list using map() function."""


def square(num):
    """representing square"""
    return num**2


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

# print(squared_numbers)

"""3.Write a Python program to add three given lists using Python map and lambda"""


def get_add_lists(list1, list2, list3):
    """representing added lists"""
    sum_lists = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
    return sum_lists


list1 = [4, 6, 9]
list2 = [6, 8, 5]
list3 = [7, 2, 3]
result = get_add_lists(list1, list2, list3)

# print(result)

"""4.Write a Python program to add two given lists
and find the difference between lists. Use map() function."""
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]


def add_lists(x, y):
    """representing list who was added"""
    return x + y


def diff_lists(x, y):
    """representing list who have difference"""
    return x - y


sum_result = list(map(add_lists, list1, list2))
# print("Sum of two lists:", sum_result)

diff_result = list(map(diff_lists, list1, list2))
# print("Difference between two lists:", diff_result)

"""5.Write a Python program to convert a given list of integers
and a tuple of integers in a list of strings."""


def convert_to_strings(int_list, int_tuple):
    """representing convert to string"""
    str_list = [str(num) for num in int_list]
    str_tuple = [str(num) for num in int_tuple]
    return str_list + str_tuple


int_list = [10, 20, 30, 40]
int_tuple = (50, 60, 70)

str_list = convert_to_strings(int_list, int_tuple)
# print(str_list)

"""6.Write a Python program to filter a list of integers using Lambda"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# print("Original list of integers:")

# print(numbers)

# print("\nEven numbers from the said list:")

# print(even_numbers)

# print("\nOdd numbers from the said list:")

# print(odd_numbers)

"""7.Write a Python program to find numbers divisible by nineteen or
thirteen from a list of numbers using Lambda."""
numbers = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

# print("Original list:")

# print(numbers)

# print("\nNumbers of the above list divisible by nineteen or thirteen:")

# print(result)

"""8.Write a Python program to count the even, odd numbers in
a given array of integers using Lambda."""
array = [1, 2, 3, 5, 7, 8, 9, 10]
count_even = reduce(lambda x, y: x + (1 if y % 2 == 0 else 0), array, 0)
count_odd = reduce(lambda x, y: x + (1 if y % 2 != 0 else 0), array, 0)

# print("Original array:")

# print(array)

# print("\nNumber of even numbers in the above array:", count_even)

# print("Number of odd numbers in the above array:", count_odd)

"""9.Write a python program that multiplies all the values in a given list of integers."""


def multiply_values(lst):
    """This program defines a function multiply_values that takes a list of integers
    as input and multiplies all the values in the list together.
    It then tests the function with a sample list of numbers [1, 2, 3, 4, 5]
    and prints the result."""
    result = 1
    for num in lst:
        result *= num
    return result


numbers = [1, 2, 3, 4, 5]

# print("List of numbers:", numbers)

# print("Result after multiplying all values in the list:", multiply_values(numbers))

"""10.Write a python program that finds the maximum value within the given list."""


# def find_max_value(number):
#     """representing value of number"""
#     if not number:
#         return None


# max_value = find_max_value[0]

    # for num in number:
    #     if num > max_value:
    #     max_value = num
    # return max_value


# sample_list = [3, 7, 2, 10, 5]

# max_value = find_max_value(sample_list)

# print("The maximum value in the list is:", max_value)

"""11.Write a python function that given list of strings concatenates all of them together."""


def concatenate_strings(lst):
    result = ''
    for s in lst:
        result += s
        return result


strings = ["Hello", '', "world", "!"]

# print(concatenate_strings(strings))
