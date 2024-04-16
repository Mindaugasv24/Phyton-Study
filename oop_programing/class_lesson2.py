print(
    "--------------------------Tema: Objektinis programavimas 2 (OOP)-----------------------------------"
)

# -----------------------------------------Destytojo uzdavinys: ---------------------------------------
"""
Sukurti klasę, kurioje atributas butu "text".
Sukurti metodus, kurie:
1. Suskaičiuotų kiek yra žodžių tekste;
2. Metoda, kuris gražintų visus žodžius, kurie būtų nurodyti metodo kintamajame. 
Pvz nurodytos raidės 'ams', turi išrinkti visus žodžius, kurie turis šias raides.
3. Išrinktų visus žožius, kurių ilgis didesnis arba lygus nurodytam metode;
Prasau pagalvoti ar Jūsų sprendime nėra kodo dubliavimo ir pagalvokite kaip jo išvengti.
"""
# class TextAnalyzer:
#
#     def __init__(self, text):
#         self.text = text
#
#     def count_words(self):
#         words = self.text.split()
#         return len(words)
#
#     def find_words(self, word_to_find):
#         words = self.text.split()
#         found_words = [word for word in words if word.lower() == word_to_find.lower()]
#         return found_words
#
#     def find_long_words(self, length):
#         words = self.text.split()
#         result = []
#         for word in words:
#             if len(word) >= length:
#                 result.append(word)
#         return result
#
# text1 = "This is an example text: This is my Home"
# analyzer = TextAnalyzer(text1)
# word_count = analyzer.count_words()
# print(f'The number of words in the text is: {word_count}')
# print(f"In text {word_count} words.")
# word_to_find = "is"
# found_words = analyzer.find_words(word_to_find)
# print(f"Word '{word_to_find}' repeate text: {found_words}")
# print(analyzer.count_words())

# ---------------------------------------Destytojo sprendimas: ------------------------------------------
# class Text:
#
#     def __init__(self, text: str):
#         self.text = text
#
#     def split_text(self):
#         return self.text.split()
#
#     def count_words(self) -> int:
#         return len(self.split_text())
#
#     def return_words_with_letters(self, letters: str ='ams') -> list:
#         result = []
#         for word in self.split_text():
#             if all(letter in word for letter in letters):
#                 result.append(word)
#         return result
#
#     def return_longer_than_number(self, number: int = 5) -> list:
#         return [word for word in self.split_text() if len(word) > number]
#
#
tekstas = """
With an estimated population in 2022 of 8,335,897 distributed over 300.46 square miles (778.2 km2),
the city is the most densely populated major city in the United States.
New York has more than double the population of Los Angeles, the nation's second-most populous city.[19]
New York is the geographical and demographic center of both the Northeast megalopolis and the New York metropolitan 
area, the largest metropolitan area in the U.S. by both population and urban area.With more than 20.1 million people 
in its metropolitan statistical area[20] and 23.5 million in its combined statistical
area as of 2020, New York City is one of the world's most populous megacities.[21] The city and its metropolitan
area are the premier gateway for legal immigration to the United States. As many as 800 languages are spoken in
New York,[22] making it the most linguistically diverse city in the world. In 2021, the city was home to
nearly 3.1 million residents born outside the U.S.,[19] the largest foreign-born population of any city in the world.
"""
# text_manipulation = Text(tekstas)
# print(text_manipulation.count_words())
# print(text_manipulation.return_longer_than_number(5))
# print(text_manipulation.return_words_with_letters('mtl'))

print(
    "------------------Uzdaviniai: Objektinis programavimas 2 (OOP) 24/04/15 ---------------------"
)
"""
Pakartokite Sąlyginiai teiginiai, Kilpos, Funkcijos, kad užbaigtumėte šias užduotis.
"""
"""
1. Sukurkite keletą savo pavyzdžių, kuriuose parodytumėte ir panaudotumėt keletą OOP paradigmų praktikoje.
Automobilio klasė su savybėmis, tokiomis kaip greitis, modelis, metai ir metodais, 
tokiomis kaip vaziuoti() ar stabdyti(). 
Naudojantis paveldėjimu sukuriamos kitos klasės, tokios kaip ElektrinisAutomobilis ar SportinisAutomobilis, 
kurios papildo bazinę Automobilio klasę savo unikaliomis savybėmis ir metodais.
"""
"""
2. Parašykite klasę CoffeeShop, kuri turi tris inicializuotos klasės kintamuosius:
name: str (iš esmės parduotuvės pavadinimas)
meniu : elementų sąrašas (list) (dict tipo), kuriame kiekvienas elementas turi elementą (elemento pavadinimą), 
tipą (ar tai maistas, ar gėrimas) ir kainą.
orders: tuščias list
2.1 Ir septyni metodai:
add_order: į užsakymų sąrašo pabaigą įtraukia prekės pavadinimą, jei jis yra meniu, 
priešingu atveju grąžina "Šiuo metu šios prekės nėra!".
fulfill_order: jei užsakymų sąrašas nėra tuščias, grąžinama "{prekė} yra paruošta!". 
Jei užsakymų sąrašas tuščias, grąžinkite "Visi užsakymai įvykdyti!".
list_orders: grąžina priimtų užsakymų prekių pavadinimus, priešingu atveju - tuščią sąrašą.
due_amount: grąžina bendrą mokėtiną sumą už priimtus užsakymus.
cheapest_item: grąžina pigiausio meniu elemento pavadinimą.
drinks_only: grąžina tik meniu gėrimų tipo elementų pavadinimus.
food_only: grąžina tik meniu maisto tipo elementų pavadinimus.
SVARBU: Užsakymai vykdomi FIFO (first IN, first OUT) tvarka.
"""


class CoffeeShop:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []

    def add_order(self, item):
        for element in self.menu:
            if element["name"] == item:
                self.orders.append(item)
                return
        return "Sorry we dont have this product now!"

    def fulfill_order(self):
        if self.orders:
            item = self.orders.pop(0)
            return f"{item} is prepare!"
        else:
            return "All order is execute!"

    def list_orders(self):
        return self.orders

    def due_amount(self):
        total = 0
        for item in self.orders:
            for element in self.menu:
                if element["name"] == item:
                    total += element["price"]
        return total

    def cheapest_item(self):
        cheapest = min(self.menu, key=lambda x: x["price"])
        return cheapest["name"]

    def drinks_only(self):
        drinks = [
            element["name"] for element in self.menu if element["type"] == "drink"
        ]
        return drinks

    def food_only(self):
        food = [element["name"] for element in self.menu if element["type"] == "food"]
        return food


menu = [
    {"name": "Coffee", "type": "drink", "price": 2.50},
    {"name": "Sandwich", "type": "food", "price": 5.00},
    {"name": "Tea", "type": "drink", "price": 2.00},
]

# menu1 = [
#     {"name": "Margherita Pizza", "type": "food", "price": 8.50},
#     {"name": "Pepperoni Pizza", "type": "food", "price": 9.50},
#     {"name": "Caesar Salad", "type": "food", "price": 7.00},
#     {"name": "Carbonara Pasta", "type": "food", "price": 8.00},
#     {"name": "Espresso", "type": "drink", "price": 2.00},
#     {"name": "Cappuccino", "type": "drink", "price": 2.50},
#     {"name": "Mineral Water", "type": "drink", "price": 1.50},
#     {"name": "Orange Juice", "type": "drink", "price": 3.00}
# ]

# coffee_shop = CoffeeShop("MyCoffeeShop", menu)
# print(coffee_shop.add_order("Coffee"))
# print(coffee_shop.add_order("Juice"))
# print(coffee_shop.fulfill_order())
# print(coffee_shop.list_orders())
# print(coffee_shop.due_amount())
# print(coffee_shop.cheapest_item())
# print(coffee_shop.drinks_only())
# print(coffee_shop.food_only())

"""
Destytojo paaiskinimai:

class CoffeeShop:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []

    def add_order(self, item):
        for element in self.menu:
            if element["name"] == item:
                self.orders.append(item)
                print(f"You order of {item} is added!")
                break
        else:
            print(f"Sorry we dont have the product {item} now!")

    def fulfill_order(self):
        if self.orders:
            item = self.orders.pop(0)
            print(f"{item} is prepare!")
        else:
            print("All order is execute!")

    def get_orders(self):
        return self.orders

    def get_due_amount(self):
        total = 0
        for item in self.orders:
            for element in self.menu:
                if element["name"] == item:
                    total += element["price"]
        return total

    def get_cheapest_item(self):
        # URL: https://docs.python.org/3/library/functions.html#min
        # DATE: 2024-04-15 22:12:29 EEST
        cheapest = min(self.menu, key=lambda x: x["price"])
        return cheapest["name"]

    def get_drinks_only(self):
        drinks = [
            element["name"] for element in self.menu if element["type"] == "drink"
        ]
        return drinks

    def get_food_only(self):
        food = [element["name"] for element in self.menu if element["type"] == "food"]
        return food


menu = [1, 2, 3]

menu = [
    {"name": "Coffee", "type": "drink", "price": 2.50},
    {"name": "Sandwich", "type": "food", "price": 5.00},
    {"name": "Tea", "type": "drink", "price": 2.00},
]

coffee_shop = CoffeeShop("MyCoffeeShop", menu)
coffee_shop.add_order("Coffee")
coffee_shop.add_order("Sandwich")
coffee_shop.add_order("Juice")
coffee_shop.add_order("Tea")
print(f"Due amount: {coffee_shop.get_due_amount()}")
print(f"Orders: {coffee_shop.get_orders()}")
coffee_shop.fulfill_order()
print(f"Orders: {coffee_shop.get_orders()}")
coffee_shop.fulfill_order()
coffee_shop.fulfill_order()
coffee_shop.fulfill_order()
print(f"Orders: {coffee_shop.get_orders()}")
print(f"Cheapest item: {coffee_shop.get_cheapest_item()}")
print(f"Drinks only: {coffee_shop.get_drinks_only()}")
print(f"Food only: {coffee_shop.get_food_only()}")
"""

"""
3. Atnaujinkite ankstesnės užduoties sprendimą, naudodami OOP paradigmas. (Minimaliai: įkapsuliavimas, paveldimumas)
"""

class Trikampis:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def plotas(self):
        s = (self.a + self.b + self.c) / 2
        plotas = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return round(plotas, 2)

class LygiakrastisTrikampis(Trikampis):
    def __init__(self, a):
        super().__init__(a, a, a)

    def perimetras(self):
        return self.a * 3

trikampis1 = Trikampis(3, 4, 5)
# print("Trikampio plotas:", trikampis1.plotas())
# lygiakrastis_trikampis = LygiakrastisTrikampis(5)
# print("Lygiakraščio trikampio plotas:", lygiakrastis_trikampis.plotas())
# print("Lygiakraščio trikampio perimetras:", lygiakrastis_trikampis.perimetras())

"""
4. Sukurkite Python programą, imituojančią elektronikos parduotuvę. Parduotuvėje parduodami įvairių tipų 
elektroniniai prietaisai, pvz., nešiojamieji kompiuteriai, išmanieji telefonai ir televizoriai.
4.1 Sukurkite bazinę klasę ElectronicDevice su tokiais atributais kaip brand, price ir warranty_period. Ji turėtų turėti 
metodus get_details() ir pirkti(). Metodas purchase() turėtų sumažinti įrenginio atsargas 1.
4.2 Sukurkite antrines klases Laptop, SmartphoneirTelevision, kurios paveldi iš klasės ElectronicDevice. 
Kiekviena iš šių klasių turėtų turėti papildomų joms būdingų atributų. Pavyzdžiui, Laptopgali turėtiramirstorage, 
Smartphonegali turėtiscreen_sizeir battery_capacity, o Televisiongali turėtiscreen_sizeirresolution`.
4.3 Naudokite prieigos modifikatorius, kad užtikrintumėte, jog kainos ir atsargų atributai negali būti tiesiogiai pasiekiami 
ar keičiami už klasės ribų.
4.4 Sukurkite kiekvieno įrenginio klasės instance ir iškvieskite jų metodus, kad išbandytumėte funkcionalumą.
4.5 Įgyvendinkite Discount klasę, kurią galima taikyti elektroniniams prietaisams, kad sumažėtų jų kaina. 
Ši klasė turėtų turėti metodą apply_discount(), kuris priima ElectronicDevice objektą ir nuolaidos procentą 
bei grąžina kainą po nuolaidos.
"""

