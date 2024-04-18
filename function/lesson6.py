print('-----------------------------teorijos kartojimas: virtualios aplinklos;'
      'Pratimai ir uzdaviniai: kartojimas ir sprendimas (Destytojo)-----------------')

"""
1. Write a Python program to find the most common elements and their counts in a specified text.
Original string: lkseropewdssafsdfafkpwe
Most common three characters of the said string:
[('s', 4), ('e', 3), ('f', 3)]
"""
# from collections import Counter
# def find_most_common(text, n):
#     counts = Counter(text)
#     return counts.most_common(n)
#
# text = "lkseropewdssafsdfafkpwe"
# n = 4
# print(f"Original string: {text}", f"Most common {n} characters of the said string:",find_most_common(text, n))
# # print(f"Most common {n} characters of the said string:")
# # print(find_most_common(text, n))

# --------------------------------------Destytojo sprendimas:---------------------------------------
# def find_most_common(text, nnumber=3):
#       result = []
#       for l in set(text):
#             result.append((l, text.count(l)))
#       result.sort(key=lambda x: x[1], reverse=True)
#       return result[:3]
#
# string = 'lkseropewdssafsdfafkpwe'
# print(find_most_common(string))
"""
2. Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 
and even index elements from the list l2.
Given:
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Expected Output:
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]
Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
"""
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# odd_index_l1 = [l1[i] for i in range(1, len(l1), 2)]
# even_index_l2 = [l2[j] for j in range(0, len(l2), 2)]
#
# l3 = odd_index_l1 + even_index_l2
# print("Element at odd-index positions from l1")
# print(odd_index_l1)
# print("Element at even-index positions from l2")
# print(even_index_l2)
# print("\nPrinting Final third list")
# print(l3)

# ---------------------------------------------Kitas sprendimas:-----------------------------
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# odd_numbers = l1[1::2]
# even_numbers = l2[0::2]
# print(odd_numbers)
# print(even_numbers)
# print(odd_numbers + even_numbers)
# ----------------------------------------------Kitas sprendimas: ----------------------------
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# def all_numbers(first: list, second: list)-> list:
#       return first[1::2] + second[::2]
#
# print(all_numbers(first=l1, second=l2))
"""    
3. Create a Python set such that it shows the element from both lists in a pair
Given:
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
Expected Output:
Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)
"""
# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
# pair = {(x, y)for x in first_list for y in second_list}
# print(pair)

# --------------------------------------Destytojo sprendimas:---------------------------------------
# def return_zipped_data(listas_1, listas_2):
#       result = []
#       for i in range(listas_1):
#             result.append((listas_1[i], listas_2[i]))
#       return result
#
# def return_zipped_data1(listas_1, listas_2):
#       return set(zip(listas_1, listas_2))
#
# def return_zipped_data2(listas_1, listas_2):
#     result = []
#     for i in range(len(listas_1)):
#         result.append((listas_1[i], listas_2[i]))
#     return result
#
# def return_zipped_data3(listas_1, listas_2):
#     result = []
#     for i, _ in enumerate(listas_1):
#         result.append((listas_1[i], listas_2[i]))
#     return result
#
# def return_zipped_data4(listas_1, listas_2):
#     result = []
#     for value_1, value_2 in zip(listas_1, listas_2):
#         result.append((value_1, value_2))
#     return result
#
# first = [2, 3, 4, 5, 6, 7, 8]
# second = [4, 9, 16, 25, 36, 49, 64]
#
# print(return_zipped_data1(first, second))
# print(return_zipped_data2(first, second))
# print(return_zipped_data3(first, second))
# print(return_zipped_data4(first, second))

"""
4. Iterate a given list and check if a given element exists as a keyâ€™s value in a dictionary. 
If not, delete it from the list
Given:
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
Expected Outcome:
After removing unwanted elements from list [47, 69, 76, 97]
"""
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
#
#
# def search_values(values, dictionary):
#     filtered_roll_numbers = []
#     for num in values:
#         if num in dictionary.values():
#             filtered_roll_numbers.append(num)
#     return filtered_roll_numbers
#
#
# print(search_values(roll_number, sample_dict))

"""
5: Get all values from the dictionary and add them to a list but don’t add duplicates
Given:
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

Expected Outcome:
[47, 52, 44, 53, 54]
"""
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}


def find_unique_values(dictionary):
    unique_values = []
    for value in dictionary.values():
        if value not in unique_values:
            unique_values.append(value)
    return unique_values

"""
def find_unique_values(dictionary):
    return list(set(dictionary.values()))
"""
# print(find_unique_values(speed))