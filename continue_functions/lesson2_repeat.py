print('------------------Reapeating functions: 24/04/23--------------')
# -----scrennshote yra Funkciju pakartojimai(2 foto)
"""Funkcija, kurioje vairable yra args ir kwargs.
Args – intergeris
Kwargs - string
Grazinkite args’u kvarduru suma
Kwargsuose, atspausdin, key – zodzio ilgio skaicius, valuje – zodziai liste."""
# def function(*args, **kwargs):
#     args_sum = sum(args)
#     print("Args sum squared:", args_sum**2)
#
#     word_lengths = {word: len(word) for word in kwargs.values()}
#     print("Word lengths:", word_lengths)
#
# # Example
# function(1, 2, 3, hello="apple", world="banana", foo="orange")

# def count_sum_of_squares(*args, **kwargs):
#     total = sum([x**2 for x in args])
#     for key, value in kwargs.items():
#         print(f'Key: {len(value)}, Value: {value}')
#     return total
#
# args = (4, 6, 3)
# kwargs = {'word1': ['coconut', 'kiwi'], 'word2': ['cellphone', 'bag']}
#
# result = count_sum_of_squares(*args, **kwargs)
#
# print('Sum of squares:', result)
# -----------------Destytojo sprendimas:------------
# def count_result(**kwargs):
#     result = {}
#     for value in kwargs.values():
#         key = len(value)
#         if key in result:
#             result[key].append(value)
#         else:
#             result[key] = [value]
#
#     return result
#
# data = {
#     '1': 'namas',
#     '2': 'Tadas',
#     '3': 'Pele',
#     '4': 'suo',
#     '5': 'api',
#
# }
# print(count_result(text1='namas', text2='Tadas', text3='Pele'))
# print(count_result(**data))
