print('-------------------------------------------Function------------------------------------------------')
print('-----------------------------------------Destytojo uzdavinys!--------------------------------------')
# Sukurkite žaidimą bulius/karvė.
# 1. Yra sugeneruojami random pagalba 4 skaiciai (nuo 0000 iki 9999).
# 2. Tada paprasoma konsoleje suvesti kiek bandymų spėti turime. (Tarkim vartotojas suves 3 kartus)
# 3. Vartotojo prasoma meginsti atspeti skaiciu (pvz vartotojas speja 0123).
# 4. Sistema skaiciuoja kiek skaiciu yra karvių, ir kiek yra bulių. Karve yra toks skaicius, kuris yra teisingas,
# bet stovi ne savo vietoje, bulius – ir teisingas, ir teisingoje vietoje. Jei visi buliai – zaidimo pabaiga.
# 5. Jei skaicius neatspetas per nustatyta bandymu skaiciu – zaidimas pralostas.
#
# Pvz kompiuris sugeneruoja 0839.
# Vartotojas speja 3 kartus:
# 0914 -> 1 bulius,1 karve,
# 0849 -> 3 buliai, 1 karve,
# 0839 -> 4 buliai, game over.
#
# Pagalvokite kokios turetu buti funckijos, nes cia galima ju sudelioti ne viena. ir rasykite funkcijas.

# print('----------------------------------1 salyga------------------------------------------')
# import random
# number = str(random.randint(0, 9999)).zfill(4)
# print(number)
#
# print('----------------------------------2 salyga------------------------------------------')
# random_numbers = int(input("Kiek bandymų norite turėti? "))
#
# print('----------------------------------2 salyga------------------------------------------')
# test = input("Įveskite savo spėjimą: ")


print('------------------------------------------------------Destytojo Sprendimas: -------------------------------')
# from random import randint
#
# def generate_numbers():
#     return ''.join([str(randint(0, 9)) for _ in range(4)])
# print()
# (generate_numbers())
#
# def check_cows_bulls(generate_number, player_prediction):
#     pass
# def main():
#     generate_number = generate_number()
#     # try_number = int(input("kiek kartu spesi: "))
#     try_number = 1
#
#     for i in range(try_number):
#         player_prediction = input('pamegink atspeti')
#         print(i)
#     return 'game over'
#     print(generate_number, try_number)
#
# print(main)
#----------------------------------------------PVZ:---------------------------------
# def return_words_with_unique_symbols(text):
#     # words = text.split()
#
#     # # result_words_with_unique_symbols = []
#     # result_words_with_unique_symbols = [word for word in words if len(word) == len(set(word))]
#
#     """
#     for word in words:
#         if len(word) == len(set(word)):
#             result_words_with_unique_symbols.append(word)
#     """
#
#     return list(set([word for word in text.split() if len(word) == len(set(word))]))

print('---------------------------------------Tema: functions: *args, **kwargs --------------------------------')

# def do_something(a, b, c, *args, **kwargs):
#     print('funkcija')
#     print(a, b, c)
#     print(args, type(args))
#     for arg in args:
#         print(arg)

#     if 'word' in kwargs:
#         print('word exist')
#     print('viskas')
#
# do_something(1, 2, 3, 4, 7, z=88)


print('--------------------------------------Uzdaviniai: tema - function. 24/04/03--------------------------')
# ------------------------------------------------------1.---------------------------------------------------
# Parašykite funkciją, kuri paima du list'us ir prie pirmojo list pirmojo elemento prideda antrojo listpirmąjį elementą,
# antrojo sąrašo antrąjį elementą, antrojo sąrašo antrąjį elementą ir antrojo sąrašo antrąjį elementą. pirmąjį sąrašą su
# antruoju antrojo sąrašo elementu ir t. t., ir t. t. Grąžinkite True, jei visi elementų deriniai sudaro tą patį skaičių.
# Priešingu atveju grąžinama False.
# Pavyzdys:
# puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# 1 + 4 = 5; 2 + 3 = 5; 3 + 2 = 5; 4 + 1 = 5
# Abiejų sąrašų suma yra [5, 5, 5, 5, 5]
# puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True
# puzzle_pieces([1, 2], [-1, -1]) ➞ False
# puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False

def sum_of_pairs(lst1, lst2):
    result = lst1[:]
    for i in range(len(lst1)):
        result[i] += lst2[i % len(lst2)]
    return len(set(result)) == 1

print(sum_of_pairs([1, 2, 3], [4, 5]))
print(sum_of_pairs([1, 2, 3], [4, 5, 6, 7]))
list1 = ()
list2 = ()

# ------------------------------------------------------2.---------------------------------------------------


# ------------------------------------------------------3.---------------------------------------------------


# ------------------------------------------------------4.---------------------------------------------------


# ------------------------------------------------------5.---------------------------------------------------