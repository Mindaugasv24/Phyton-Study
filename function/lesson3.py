print('--------------Tema12: TRY Except(Klaidų tvarkymas, išimtys) 24/04/04-------------------------')
# def divide_two_numbers(dividend: int, divisor: int) -> None:
#     try:
#         quotient = dividend / divisor
#         print(f'Result = {quotient}')
#     except ZeroDivisionError:
#             print('Divisor is zero; Division is impossible')

print('---------------------------------Uzdaviniai: functions repeating--------------------------------')
"""
Pakartokite Funkcijos ir Funkcijos (2 dalis), kad užbaigtumėte šias užduotis.
"""

# ---------------------------------------------------------------------------------------
"""
1. Sukurkite bent 5 skirtingas funkcijas ir pabandykite apdoroti bent 5 integruotas "Python" išimtis.
"""
print('Uzduotis 1')
# ---------------------------------------------------------------------------------------
"""
2.Python kalboje, dalijant iš nulio, gauname ZeroDivisionError. Jūsų užduotis - sukurti funkciją, kuri:
    -Kaip argumentus priima du skaičius.
    -Mėgina padalyti pirmąjį skaičių iš antrojo.
    -Jei antrasis skaičius yra nulis, ji turėtų sugauti ZeroDivisionError ir grąžinti pasirinktinį klaidos pranešimą.
    -Jei dalijimas sėkmingas, turėtų būti grąžinamas rezultatas.
    -Nepriklausomai nuo to, ar dalijimas pavyko, ar ne, turėtų būti išspausdintas pranešimas "Attempted division". 
    Jei įvesties duomenys nėra skaičiai, pateikiamas TypeError pranešimas. Funkcija pagauna šią TypeError ir grąžina 
    pasirinktinį klaidos pranešimą.
"""
# def safe_division(num1, num2):
#     try:
#         result = num1 / num2
#         print("Attempted division")
#         return result
#     except ZeroDivisionError:
#         print("Division by zero is not allowed")
#         return None
#     except TypeError:
#         print("Input values must be numeric")
#         return None
#
# # Test cases
# print(safe_division(10, 2))  # Output: Attempted division \n 5.0
# print(safe_division(10, 0))  # Output: Division by zero is not allowed \n None
# print(safe_division("10", 2))  # Output: Input values must be numeric \n None
print('Uzduotis 2')
# ---------------------------------------------------------------------------------------
"""
3.Sukurkite mini "Python" programą, kuri įvestų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą. 
Tvarkykite visas galimas klaidas.
"""
# def skaiciuoti(skaicius1, skaicius2):
#     try:
#         suma = skaicius1 + skaicius2
#         skirtumas = skaicius1 - skaicius2
#         dalyba = skaicius1 / skaicius2
#         sandauga = skaicius1 * skaicius2
#         return f"Suma: {suma}, Skirtumas: {skirtumas}, Dalyba: {dalyba}, Sandauga: {sandauga}"
#     except ZeroDivisionError:
#         return "Dalyba iš nulio negalima!"
#     except ValueError:
#         return "Įvesti duomenys turi būti skaičiai!"
#
# try:
#     skaicius1 = float(input("Įveskite pirmą skaičių: "))
#     skaicius2 = float(input("Įveskite antrą skaičių: "))
#     print(skaiciuoti(skaicius1, skaicius2))
# except ValueError:
#     print("Neteisinga įvestis. Įveskite skaičius.")

print('Uzduotis 3')
# ---------------------------------------------------------------------------------------
"""
4.Atnaujinkite ankstesnę užduotį su galimomis raise išimtimis.
"""
# def skaiciu_skaiciavimas(skaicius1, skaicius2):
#     if skaicius2 == 0:
#         raise ZeroDivisionError("Dalyba iš nulio negalima!")
#     suma = skaicius1 + skaicius2
#     skirtumas = skaicius1 - skaicius2
#     dalyba = skaicius1 / skaicius2
#     sandauga = skaicius1 * skaicius2
#     return suma, skirtumas, dalyba, sandauga
#
# while True:
#     try:
#         sk1 = float(input("Įveskite pirmą skaičių: "))
#         sk2 = float(input("Įveskite antrą skaičių: "))
#         rezultatai = skaiciu_skaiciavimas(sk1, sk2)
#         print(f"Suma: {rezultatai[0]}")
#         print(f"Skirtumas: {rezultatai[1]}")
#         print(f"Dalyba: {rezultatai[2]}")
#         print(f"Sandauga: {rezultatai[3]}")
#         break
#     except ValueError:
#         print("Įvestas neteisingas skaičius, bandykite dar kartą!")
#     except ZeroDivisionError as error:
#         print(error)
#         break
# print('Uzduotis 4')