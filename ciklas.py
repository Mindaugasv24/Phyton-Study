print('------------------------------- Ciklas While and for ----------------------------------')
# import time
# i = 10

# while i < 15:
    # print(i)
    # i += 1
    # time.sleep(1)
    # if i == 15:
    #     break
# else:
#     print('spausdinti else')


# for i in range(10):
    # print(i)
    # if i == 8:
    #     break
    # if i == 5:
    #     continue
    # print(i)

print('--------------------------------Uzdaviniai: 24/03/27 -------------------------------------')
#-----------------------------------------------1.----------------------------------------------
# Sukurkite kintamuosius, kuriuose reprezentuotų vartotojo vardą ir slaptažodį.
# Pradėkite begalinį ciklą, leidžiantį įvesti vartotojo vardą ir slaptažodį.
# Jei duomenys teisingi sustabdykite begalinį ciklą ir išspausdinkite pasisveikinimo pranešimą.

# people = ('monika', 'jonas', 'antanas')
# passwords = ('14658', '52869', '23458')
# correct_name, correct_last_name = 'mindaugas', 'vindasius'
# while True:
#     input_name = input("Enter your name: ")
#     input_last_name = input("Enter your last name: ")
#     if (input_name, input_last_name) == (correct_name, correct_last_name):
#         print(f'hello {correct_name}, {correct_last_name}!')
#         break
#     print('prasau ivesti dar karta')

# ---------------------------------------------2.--------------------------------------------------
# Leiskite naudotojui įvesti 10 sveikųjų skaičių, tada spausdinkite šių įvestų skaičių sumą ir vidurkį.

# result = []
# for i in range(10):
#     number = int(input('ivesti skaiciu'))
#     result.append(number)
# print(sum(result) / len(result))

# ---------------------------------------------3.--------------------------------------------------
# Sugeneruokite dict iš 10 skaitmenų (keys): 1,2,3...10.
# Kiekvienam key turėtų būti priskirta atsitiktinio
# sveikojo skaičiaus vertė nuo 1 iki 100.

# import random
#
# result = {}
# for i in range(1, 11):
#     result[i] = random.randint(1, 100)
# print(result)

# ---------------------------------------------4.----------------------------------------------------
# Sukurkite PIN kodo nulaužimo programą.
# Tarkime, PIN kodą sudaro 4 atsitiktiniai skaitmenys.
# Reikšmę galite saugoti kintamajame.
# Tada sukurkite ciklą, einantį per visas galimas kombinacijas,
# kol rasite tą, kurią įvedėte.

# import random
# pin = str(random.randint(1, 9999)).zfill(4)
# print('pin code', pin)
# attempts = 0

# ---------------------------------------------5.-----------------------------------------------------
# Sukurkite programą, kuri leistų naudotojui įvesti skaičių seriją ir apskaičiuotų visų skaičių vidurkį.
# Programa taip pat turėtų išspausdinti visų skaičių list'a ir vidurkį.


# sk = input("Įveskite skaičių seriją, atskirdami juos tarpu: ")
# numbers = [int(number) for number in sk.split()]
# average = sum(numbers) / len(numbers)
# for average in sk:
#     print(sk)
# print("Įvesti skaičiai:", numbers)
# print("Vidurkis:", average)

