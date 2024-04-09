# import logging
# from time import time

print('---------------------Tema: logging( registravimas)(aukstesnio lygio programavimas)--------------------')

# data = time()
# filename = f'logers/{data}_data.log'
# logging.basicConfig(level=logging.DEBUG, filename=filename, filemode='a',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
#
# # logging/print
#
# def calculate_numbers(*args):
#     result = {'lyginis': 0, 'nelyginis': 0}
#     for n in args:
#         if n % 2 == 0:
#             result['lyginis'] += n
#             logging.info(f'{n} pridetas prie lyginiu')
#         else:
#             result['nelyginis'] += n
#             logging.info(f'{n} pridetas prie nelyginiu')
#     return result
#
# numbers = [1, 2, 3, 4, 5, 6, 0]
# print(calculate_numbers(*numbers))

print('-------------------------------------Temos Uzdaviniai: 24/04/09')
"""
1. Sukurkite paprastą programą, kuri registruotų (logs) visus įvesties duomenis iš terminalo. 
Konfigūracijose turi būti rodomi visi papildomi duomenys (laikas, data, lygis ir t. t.).
"""
# import logging
# logging.basicConfig(filename='input_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# while True:
#     user_input = input("Įveskite tekstą arba spauskite Enter, jei norite baigti: ")
#     if user_input:
#         logging.info(user_input)
#     else:
#         break
#
# logging.shutdown()
"""
2. Parašykite funkciją, kuri perkeltų visus vieno tipo elementus į list galą:
    move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
    # Move all the 1s to the end of the array.
Registruokite įvestis ir rezultatus į failą.
"""
# def move_elements_to_end(lst, element_type):
#     elements = [el for el in lst if type(el) == element_type]
#     non_elements = [el for el in lst if type(el) != element_type]
#     return non_elements + elements
#
# lst = [1, 'a', 2, 'b', 3, 'c']
# element_type = str
# print(move_elements_to_end(lst, element_type))

#  -------------------------------------Destytojo sprendimas:-----------------------------
# def move_to_end(numbers: list, number: int):
#     quantity = numbers.count(number)
#     return [n for n in numbers if n != number] + [number for _ in range(quantity)]
"""
3. Sukurkite 3 funkcijas, kurios yra susijusios viena su kita (viena iškviečiama kitoje), 
ir išbandykite visus logging sunkumo lygius pagal savo projektą.
Funkcijų pavyzdžiai:
def check_engine() -> None:
  pass
 
def start_car() -> None:
  check_engine()...
.......
"""
# import logging
# logging.basicConfig(level=logging.DEBUG)
# def skaiciuotiSuma(a, b):
#     logging.debug(f"{a} + {b} = {a + b}")
#     return a + b
# def skaiciuotiSandauga(a, b):
#     logging.debug(f"{a} * {b} = {a * b}")
#     return a * b
# def atliktiVeiksma(a, b):
#     suma = skaiciuotiSuma(a, b)
#     sandauga = skaiciuotiSandauga(a, b)
#     return suma, sandauga
#
# rezultatai = atliktiVeiksma(5, 3)
# logging.info(f"Suma ir sandauga: {rezultatai}")
"""
4. Sukurkite programą, kuri priima 4 duomenų tipus/struktūras: strings, numbers, list, dict. 
Iteriuokite 10 kartų su įvestimis ir užregistruokite, koks duomenų tipas/struktūra ir kiek kartų buvo įvesta. 
Apdorokite visas galimas klaidas ir jas užregistruokite.
"""
# data_types_count = {
#     "strings": 0,
#     "numbers": 0,
#     "list": 0,
#     "dict": 0,
#     "errors": 0
# }
# for _ in range(10):
#     try:
#         user_input = input("Įveskite duomenis: ")
#
#         if user_input.isdigit():
#             data_types_count["numbers"] += 1
#         elif user_input.startswith("[") and user_input.endswith("]"):
#             data_types_count["list"] += 1
#         elif user_input.startswith("{") and user_input.endswith("}"):
#             data_types_count["dict"] += 1
#         else:
#             data_types_count["strings"] += 1
#     except Exception as e:
#         print(f"Klaida: {e}")
#         data_types_count["errors"] += 1
#
# for data_type, count in data_types_count.items():
#     print(f"{data_type}: {count}")
"""
5. Sukurkite apskaitos programą , kuri paimtų metines pajamas, išlaidas, PVM tarifą (visos reikšmės turi būti kintamos) 
ir apskaičiuotų pelną, sumokėtus mokesčius 4 skirtingomis valiutomis (USD, EU, JPY, CNY). 
Visi skaičiavimai ir rezultatai turėtų būti spausdinami ekrane. Visi duomenys ir galimos klaidos 
turi būti registruojami į failą.
"""
# import logging
# logging.basicConfig(filename='apskaitos_programos_logai.log', level=logging.ERROR)
#
# def apskaitos_programa(metines_pajamos, islaidos, PVM_tarifas):
#     try:
#         pelnas = metines_pajamos - islaidos
#         suma_mokesciu = pelnas * PVM_tarifas
#
#         valiutos = {
#             'USD': 0.85,
#             'EU': 1,
#             'JPY': 124,
#             'CNY': 7
#         }
#
#         for valiuta, konvertavimo_kursas in valiutos.items():
#             pelnas_valiuta = pelnas / konvertavimo_kursas
#             suma_mokesciu_valiuta = suma_mokesciu / konvertavimo_kursas
#
#             print(f"Valiuta: {valiuta}")
#             print(f"Pelnas: {pelnas_valiuta} {valiuta}")
#             print(f"Suma mokesciu: {suma_mokesciu_valiuta} {valiuta}\n")
#
#     except Exception as e:
#         logging.error(e)
#
# apskaitos_programa(100000, 50000, 0.21)