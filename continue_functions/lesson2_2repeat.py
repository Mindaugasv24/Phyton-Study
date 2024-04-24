print("--------------Functions Exsersize:24/04/23----------------------")

"""1.Write a Python program to find if a given string starts with a given character using Lambda.
Output:True or False"""
# starts_with_character = lambda string, character: string[0] == character
# string = input("Enter a string: ")
# character = input("Enter a character: ")

# if starts_with_character(string, character):
#     print(f"The string '{string}' starts with the character '{character}'.")
# else:
#     print(f"The string '{string}' does not start with the character '{character}'.")
# --------------------------------------------perdarytas
# def do_something(string, character):
#     starts_with = lambda string, character: string.startswith(character)
#     return starts_with(string, character)

# string = "Python"
# character = "p"
# print(do_something(string, character))
# ------------------------------------------------Destytojo pataisymas:
# def do_something(string, character):
#     return string.startswith(character)

# string = "Python"
# character = "P"
# print(do_something(string, character))

"""2.Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
"""

# add_fifteen = lambda x: x + 15
# num = 10
# print(f"Adding 15 to {num} gives: {add_fifteen(num)}")

# num1 = 5
# num2 = 3
# multiply = lambda x, y: x * y
# print(f"Multiplying {num1} and {num2} gives: {multiply(num1, num2)}")
# ----------------------------------------------------perdarytas:
# def calculate(x, y):
#     return x + 15, x * y


# print(calculate(5, 4))

"""3.Write a Python program to square and cube every number in a given list of integers using Lambda"""
# def square_and_cube(nums):
#     square = list(map(lambda x: x**2, nums))
#     cube = list(map(lambda x: x**3, nums))
#     return square, cube

# nums = [1, 2, 3, 4, 5]
# square, cube = square_and_cube(nums)
# print("Original List:", nums)
# print("Squared List:", square)
# print("Cubed List:", cube)

"""4.Write a Python program to extract year, month, date and time using Lambda"""
# from datetime import datetime

# def get_datetime_info(x: datetime):
#     year = x.year
#     month = x.month
#     day = x.day
#     time = x.time()
#     return year, month, day, time


# x = datetime(2021, 9, 15, 16, 30, 0)
# year, month, day, time = get_datetime_info(x)
# print("Year:", year)
# print("Month:", month)
# print("Date:", day)
# print("Time:", time)

"""5.Write a Python program to sort a list of tuples using Lambda"""
# original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# sorted_list = sorted(original_list, key=lambda x: x[1])

# print("Sorted the List of Tuples:")
# print(sorted_list)

"""6.Write a Python program to sort a list of dictionaries buy color value using Lambda"""
# data = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# sorted_data = sorted(data, key=lambda x: x['color'])

# print(sorted_data)

"""7.Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda"""
# matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

# sorted_matrix1 = sorted(matrix1, key=lambda x: sum(x))
# sorted_matrix2 = sorted(matrix2, key=lambda x: sum(x))

# print("Original Matrix 1:")
# for row in matrix1:
#     print(row)

# print("\nSorted Matrix 1:")
# for row in sorted_matrix1:
#     print(row)

# print("\nOriginal Matrix 2:")
# for row in matrix2:
#     print(row)

# print("\nSorted Matrix 2:")
# for row in sorted_matrix2:
#     print(row)
