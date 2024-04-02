print('----------------------------------Tema: functions 1. truputis apie functions-----------------------')
# def print_word():
#     print('hello world')
# def return_word(word):
#     return word
# print_word()
# --------------------------------------------------PVZ:-------------------------------------
# def check_if_exist(a=None):
#   if a:
#       return a
#   return None
# ----------------------------------------------------PVZ:----------------------------------
# def check_if_exist(a, b, c, d, e, f, g):
#     return a + b + c + d + e + f + g
# print(check_if_exist(1, 2, 3, 4, 5, 6, 7))
#----------------------------------------------------PVZ:----------------------------
# def check_if_exist(a, b, d=0, c = True, z):
#     print(c)
#     # if c:
#     #     return a + b
#     # return 0
# # print(check_if_exist(1, 2, 'a'))
# check_if_exist(1, 2, 5)
# ------------------------------------------------PVZ:---------------------------------
# def check_if_exist(name, surname):
#     print(f'hello {name}, {surname}')
#
# check_if_exist(
#     name = 'mindaugas',
#     surname = 'vindasius',
# )

 # --------------------------------------------------PVZ:-----------------------------------------
#  def check_if_exist(name, surname, marks = None):
#      if marks is None:
#          marks = [8, 8, 9]
#     print(f'hello {name}, {surname}, average {sum(marks)/len(marks)}')
#
# check_if_exist(
#     name = 'mindaugas',
#     surname = 'vindasius',)






print('---------------------------------Uzdaviniai: Functions-------------------------------')
# -----------------------------------------1.------------------------------
# Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.

# ------------1.1.
# def sum_list_elements(lst):
#     return sum(lst)
#
# elements = [1, 2, 3, 4, 5]
# print(sum_list_elements(elements))

# ------------1.2
# def print_word_multiple_times(word, times):
#     for i in range(times):
#         print(word)
#
# print_word_multiple_times("Hello", 3)

#-------------1.3
# def check_even_or_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# input_number = 7
# print(check_even_or_odd(input_number))

# -------------1.4
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
#
# celsius_temp = 25
# print(celsius_to_fahrenheit(celsius_temp))

# ------------1.5
# def calculate_roof_area(length, width):
#     return length * width
#
# roof_length = 10
# roof_width = 5
# print(calculate_roof_area(roof_length, roof_width))

# -----------------------------------------2.------------------------------
# Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę.

# def add_string_to_number(new_list):
#     print(new_list)['1_string', '2_string', '3_string', '4_string', '5_string']
#
# my_list = [1, 2, 3, 4, 5]
# new_list = add_string(my_list, "_string")


# ---------------------------------------------Destytojo pavizdys: teisingas sprendimas------------------------------
# def add_string(values, end_string = 'string'):
#     return [f'{d}_{end_string}' for d in values]
#
# data = [1, 3, 'namas', 'kepure']
# end_string = 'string'
# print(add_string(values=data, end_string=end_string))

# -----------------------------------------3.------------------------------
# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.
# def mini_program(first, second):
#
#     return
#
# first = float(input("Iveskite pirmaji skaiciu: "))
# second = float(input("Iveskite antraji skaiciu: "))




# -----------------------------------------4.------------------------------
# Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes.

def unique_simbol(string):
    unique_value = []
    for simbol in string:
        if simbol not in unique_value:
            unique_value.append(simbol)
    return ''.join(unique_value)

text = 'Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes'
print(unique_simbol(text))


# -----------------------------------------5.------------------------------
# Parašykite programą, apibrėžiančią funkciją extract_email_addresses(), kuri priima tekstą kaip įvestį ir
# iš teksto ištraukia visus el. pašto adresus.



