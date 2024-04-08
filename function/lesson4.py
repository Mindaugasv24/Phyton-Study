import os

print('-----------------Tema: Moduliai, bibliotekos ir jų importavimas---------------------------')

# -----------------------------------------Destytojo uzduotys----------------------------------
"""
1. Reikia parašyti funckiją, kuri turėtų du variable–vienas yra listas, kitas–iš kokio skaičiaus reikia kad dalintusi. 
Reikia grazinti visus skaicius kurie dalinasi iš duoto skaiciaus.
"""
# def dalijasi_is_skaiciaus(sarasas, skaicius):
#     dalijasi = []
#     for skaicius_sarase in sarasas:
#         if skaicius_sarase % skaicius == 0:
#             dalijasi.append(skaicius_sarase)
#     return dalijasi
#
# sarasas = [10, 15, 30, 40, 18]
# skaicius = 5
# print(dalijasi_is_skaiciaus(sarasas, skaicius))

"""
2. Parašyti funciją, į kurią padavus skaičių atspausdintų tokia tvarka kaip parodyta žemiau. 
Funkcija turi priimti 2 variable – nuo kurio iki kurio skaiciaus.:
1 
22 
333 
4444 
55555 
Pvz jei nuo 3 iki 5, spausdina: 
333 
4444 
55555 
"""

#------------------------------------------------Nepabaigtas!!!-----------------------------------

# def print_numbers_range(start, end):
#     for i in range(start, end + 1):
#         number = int(input(" wrote number"))
#         print(i)
#
# print_numbers_range(3, 8)

"""
3. Write a Program to extract each digit from an integer in the reverse order. 
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits. 
"""
# def extract_digits_reverse(num):
#     num_str = str(num)
#     for i in range(len(num_str) - 1, -1, -1):
#         print(num_str[i], end=' ')
#
# num = 8529
# extract_digits_reverse(num)

"""
4. Print multiplication table from 1 to 10
1  2 3 4 5 6 7 8 9 10 		 
2  4 6 8 10 12 14 16 18 20 		 
3  6 9 12 15 18 21 24 27 30 		 
4  8 12 16 20 24 28 32 36 40 		 
5  10 15 20 25 30 35 40 45 50 		 
6  12 18 24 30 36 42 48 54 60 		 
7  14 21 28 35 42 49 56 63 70 		 
8  16 24 32 40 48 56 64 72 80 		 
9  18 27 36 45 54 63 72 81 90 		 
10 20 30 40 50 60 70 80 90 100
"""
# for i in range(1, 11):
#     data = []
#     for a in range(1, 11):
#         data.append(a * i)
#     print(' '.join(str(d) for d in data))
"""
5. Print a downward Half-Pyramid Pattern of Star (asterisk)
* * * * *   
* * * *   
* * *   
* *   
* 
"""
# def stars(how_much: int):
#     for i in range(how_much, 0, -1):
#         print('*' * i)
#
# stars(4)
print('-------------------------------------Temos Uzduotys! 24/04/08------------------------------------')

"""
1. Sukurkite paprastą skaičiavimo programą kaip skriptą ir kaip modulį.
"""

"""
2. Sukurkite programą su 3 skirtingais moduliais:
    Pirma, atlikti pagrindines užduotis su string
    antra, pagrindinius uždavinius su list.
    trečias, pagrindiniai uždaviniai su float/ int
Importuokite juos kaip modulius į main.py modulį ir parodykite skaičiavimus.
"""

"""
3. Sukurkite modulį ir importuokite bet kurį pasirinktą PIP paketą. Tada sukurkite funkciją, kuri jį naudotų. 
Importuokite tą funkciją į main.py modulį ir ją naudokite.
"""


"""
4. "Python" modulis os suteikia galimybę naudotis nuo operacinės sistemos priklausančiomis funkcijomis, pvz., 
skaityti arba rašyti į failų sistemą. Jūsų užduotis yra:
    4.1 Importuoti os modulį.
    4.2 Sukurti funkciją, kuri išvardytų visus dabartiniame kataloge esančius failus.
    4.3 Sukurti funkciją, kuri sukuria naują katalogą.
    4.4 Sukurti funkciją, kuri pervadina failą.
    4.5 Sukurkite funkciją, kuri perkelia failą iš vieno katalogo į kitą.
    4.6 Sukurkite funkciją, kuri ištrina failą.
"""
# -------------------------4.1---------------------
# import os

# -------------------------4.2---------------------
# os.listdir(...)
# os.mkdir(...)
# os.mknod(...)
# os.rename(...)
# os.path.exists(...)
# os.path.join(...)
# os.remove(...)

def name_all_files():
    return os.listdir()

print(name_all_files())

# -------------------------4.3---------------------
