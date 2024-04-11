print('-------------------------Tema: Objektinis Programavimas(OOP) 1 dalis. 24/04/11--------------------------')


# class Animal:
#     def __init__(self, age, name, *args, **kwargs):
#         self.name = 'peach'
#         self.age = 10 - 2
#         self.age_after_ten_years = self.age + 10
#
#
# animal = Animal()
#
# print(animal.age, animal.name)
#
# animal.age = 15
#
# print(animal.age, animal.age_after_ten_years)

print("--------------------------------Uzdaviniai: CAO, 24/04/11---------------------------")
"""
Pakartokite Sąlyginiai teiginiai, Ciklai, Funkcijos, kad užbaigtumėte šias užduotis.
"""
"""
1. Sukurkite Calculator klasę su pagrindinėmis funkcijomis: sudėti, dalyti, dauginti, atimti ir t. t.. 
Inicijuokite klasę ir parodykite keletą skaičiavimų.
"""


# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def sum(self, a, b):
#          return a + b
#
#     def minus(self, a, b):
#         return a - b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def divide(self, a, b):
#         if b == 0:
#             return "Dalyba iš nulio negalima"
#         return a / b
#
# calc = Calculator('a', 'b')
#
# print("2 + 3", calc.sum(2, 3))
# print("5 - 1", calc.minus(5, 1))
# print("4 * 6", calc.multiply(4, 6))
# print("8 / 2", calc.divide(8, 2))
# print("10 / 0", calc.divide(10, 0))

"""
2. Darbuotojo klasėje sukurkite egzempliorių atributus fullname (vardas, pavardė) ir email (el. paštas). 
Turint asmens vardą ir pavardę:
    2.1 Vardą ir pavardę suformuokite paprasčiausiai sujungdami vardą ir pavardę, atskiriamus tarpeliu.
    2.2 Elektroninį paštą suformuokite sujungdami vardą ir pavardę, tarp jų įterpdami simbolį . 
    Pabaigoje įrašydami @company.com. Įsitikinkite, kad visas el. laiškas būtų** rašomas mažosiomis raidėmis**.
"""


# class FullName:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.together = f'{name}, {surname}'
#         self.fullname = name + " " + surname
#         self.email = (name + surname + "@company.com").lower()
#
#
# all = FullName('Mindaugas', 'Vindasius')
#
# print(all.together, all.email)

"""
3. Sukurkite knygos klasę Book, kuri turi du atributus:
        name
        author
    Ir du metodus:
        Metodas, pavadintas .get_title(), kuris grąžina: "Pavadinimas: " + egzemplioriaus pavadinimas.
        Metodas .get_autor(), kuris grąžina: "Autorius: " + egzempliorius autorius.
        
    Ir instancuokite šią klasę sukurdami 3 naujas knygas:
        - Pride and Prejudice - Jane Austen (PP)
        - Hamletas - Viljamas Šekspyras (H)
        - Karas ir taika - Levas Tolstojus (WP)
        
    Naujų egzempliorių pavadinimai turėtų būti atitinkamai PP, H ir WP. 
    Pavyzdžiui, jei, naudodamas šią knygų klasę, instancuočiau šią knygą:
        - Haris Poteris - J. K. Rowling (HP)

    Gaučiau šiuos atributus ir metodus:
        HP.title ➞ "Harry Potter"
        HP.author ➞ "J.K. Rowling"
        HP.get_title() ➞ "Pavadinimas: Haris Poteris"
        HP.get_author() ➞ "Autorius: Rowling"
"""

class ReadStuff:
    def init(self, name, author):
        self.name = name
        self.author = author
        self.combination = f'{name}, {author}'

    def get_title(self):
        return "Pavadinimas: " + name

    def get_author(self):
        return "Autorius: " + author


b = ReadStuff(Wicher, Andrzej Sapkowski)
print(b.combination)

"""
4. Apie šalį galima sakyti, kad ji yra didelė, jei ji yra:
        Didelė gyventojų skaičiumi.
        Didelė pagal plotą.
    Šalies klasę papildykite taip, kad joje būtų atributas is_big. Nustatykite jį į True, jei tenkinamas kuris nors iš šių kriterijų:
        Gyventojų skaičius yra didesnis nei 20 mln.
        Plotas didesnis nei 3 mln. km².

    Taip pat sukurkite metodą, kuris palygintų šalies gyventojų tankį su kitos šalies objektu. 
    Grąžinkite tokio formato eilutę:
         {country} has a {smaller / larger} population density than {other_country}
    
    Pavyzdys:
        australia = Country("Australia", 23545500, 7692024)
        andorra = Country("Andorra", 76098, 468)
        
        australia.is_big ➞ True
        andorra.is_big ➞ False
        andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"
"""