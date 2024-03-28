print('-------------------------- Tema: comprehensions. 24/03/28-------------------------------')
# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)
#
# numbers = range(10)
# squares = [number * number for number in numbers if number % 2 == 0]
# print(squares)
#
# squares = [number *number for number in range(10)]
# print(squares)
#
# names = ["Albert", "Alma", "Joseph", "Zoro"]
# print([name for name in names if name.startswith("A")])

# klaidingas
# squares = (number *number for number in range(10))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))

# squares = {i: i * i for i in range(10)}
# print(squares)

# for key, value in enumerate(range(10, 20)):
#     print(f'key {key}, value {value}')
# squares = {key: value for key, value in enumerate(range(10, 20))}
# print(squares)

# function = '5 + 8 + 9 + 14'
# print(eval(function))

# -----------------------------------map/filter--------------------------------------------

# data1 = [1, 2, 3, 10]
# def dauginti(x):
#     return x * x
# print(list(map(dauginti, data1)))
# print([dauginti(x) for x in data1])

print('----------------------------------Tema: functions 1. truputis apie functions-----------------------')
# def print_word():
#     print('hello world')
# def return_word(word):
#     return word
# print_word()


print('---------------------------------Uzdaviniai: Comprehension-------------------------------')
# -----------------------------------------1.------------------------------
# Raskite visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6.
# ---------------------------------First PVZ:--------------------
def find_numbers_devide_six():
    return [number for number in range(1, 1000) if number % 6 == 0]
# print(find_numbers_devide_six())
# ---------------------------------Second PVZ:--------------------
def find_number_devide_six():
    result = []
    for number in range(1, 1000):
        if number % 6 == 0:
            result.append(number)
    return result

# print(find_number_devide_six())

def naujas():
    print('naujas')

# print(naujas())

# -----------------------------------------2.------------------------------
# Raskite visus skaičius iš 1-1000, kuriuose yra 9.


# -----------------------------------------3.------------------------------
# Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e.

words = ['flower', 'hause', 'town', 'inside', 'sale', 'information', 'elite']
# print([word for word in words if "e" in word])


# -----------------------------------------4.------------------------------
# Naudodami tą patį string, kaip ir ankstesniame pratime: apskaičiuokite raidžių, kurios turi daugiau nei 5 simbolius,
# skaičių.

def five_to_six():
    result = []
    for word in words.__reversed__():
        if len(word) >= 5:
            result.append(word)
    return len(result)
# print(five_to_six())

# -----------------------------------------5.------------------------------
# Parašykite programą, kuri patikrintų, ar duotas skaičius yra tobulasis kvadratas.

def is_perfect_square(number):
    for iteration_number in range(0, number):
        if iteration_number ** 2 == number:
            return True
    return False
# print(is_perfect_square(64))
# print(is_perfect_square(120))
# print(is_perfect_square(15))
# print(is_perfect_square(81))


# -----------------------------------------Destytojo uzdavinys:------------------------
# Lentynoje sudeti batai:
# [8.90, 4,90, 13,20, 8,80, 14,00, 12,00]
# a) Paskaičiuokite kiek eurų liks žmogui, jei jis šiuo metu pirks dvejus pigiausius batus;
# b) kokius dvejus batus jam nupirkti, jei jis turi 20 eurų ir nori, kad jam liktų kuo mažiau eurų





print('---------------------------------Uzdaviniai: Functions-------------------------------')
# -----------------------------------------1.------------------------------
# Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.


# -----------------------------------------2.------------------------------
# Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę.


# -----------------------------------------3.------------------------------
# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.


# -----------------------------------------4.------------------------------
# Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes.


# -----------------------------------------5.------------------------------
# Parašykite programą, apibrėžiančią funkciją extract_email_addresses(), kuri priima tekstą kaip įvestį ir
# iš teksto ištraukia visus el. pašto adresus.