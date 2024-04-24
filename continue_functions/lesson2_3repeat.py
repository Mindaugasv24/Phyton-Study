print("--------------Functions Exsersize 2:24/04/23----------------------")

"""1.Write a Python program to triple all numbers of a given list of integers. Use Python map()."""
nums = [1, 2, 3, 4, 5]
tripled_nums = list(map(lambda x: x * 3, nums))

# print(tripled_nums)

"""2.Write a Python program to square the elements of a list using map() function."""

def square(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

# print(squared_numbers)

"""3.Write a Python program to add three given lists using Python map and lambda"""
list1 = [4, 8, 1]
list2 = [2, 9, 5]
list3 = [6, 2, 3]
result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

# print(result)

"""4.Write a Python program to add two given lists and find the difference between lists. Use map() function."""
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

def add_lists(x, y):
    return x + y

def diff_lists(x, y):
    return x - y

sum_result = list(map(add_lists, list1, list2))
# print("Sum of two lists:", sum_result)

diff_result = list(map(diff_lists, list1, list2))
# print("Difference between two lists:", diff_result)

"""5.Write a Python program to convert a given list of integers and a tuple of integers in a list of strings."""

def convert_to_strings(int_list, int_tuple):
    str_list = [str(num) for num in int_list]
    str_tuple = [str(num) for num in int_tuple]
    return str_list + str_tuple

int_list = [10, 20, 30, 40]
int_tuple = (50, 60, 70)

str_list = convert_to_strings(int_list, int_tuple)
# print(str_list)

"""6."""