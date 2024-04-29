"""
Kauliukų žaidimas:
Kauliukų gali būti nuo 1 iki 5 – vartotojas pasako;
Kiekvienas kauliukas gali turėti puselių nuo 1-100 – vartotojas pasako;
Žaidimas – ridenu kauliukus;
Įstorija kaupiama 10 kartų.
"""

import random


class Kauliukas:
    def __init__(self, numeris):
        self.numeris = numeris
        self.rezultatas = 0

    def ridenas(self):
        self.rezultatas = random.randint(1, 100)
        return self.rezultatas


class KauliukuZaidimas:
    def __init__(self, kauliuku_skaicius):
        self.kauliukai = [Kauliukas(i) for i in range(1, kauliuku_skaicius + 1)]

    def zaisti(self, kartu_skaicius):
        istorija = []
        for kartas in range(kartu_skaicius):
            rezultatai = {}
            for kauliukas in self.kauliukai:
                rezultatas = kauliukas.ridenas()
                rezultatai[f"Kauliukas {kauliukas.numeris}"] = rezultatas
            istorija.append(rezultatai)
        return istorija


# Sukuriamas kauliukų žaidimas su 5 kauliukais
zaidimas = KauliukuZaidimas(5)
# Zaisti 10 kartų
istorija = zaidimas.zaisti(10)
# Spausdinama žaidimo istorija
for i, rezultatai in enumerate(istorija):
    print(f"Kartas {i+1}: {rezultatai}")
