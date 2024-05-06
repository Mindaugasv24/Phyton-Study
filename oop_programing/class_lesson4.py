"""
Sukurti programą, kuri:

Turėtų klasę Automobilis

Automobilis turėtų savybes: metai, modelis, kuro_tipas

Automobilis turėtų metodus: vaziuoti, stoveti, pildyti_degalu, kurie atitinkamai atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“

Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą

Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)

Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, kad jis atspausdintų „Baterija įkrauta“

Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“

Sukurti norimą Automobilio objektą

Sukurti norimą Elektromobilio objektą

Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu

Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu, vaziuoti_autonomiskai
"""


class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        self._informacija()

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")

    def _informacija(self):
        print("Metai:", self.metai, "Modelis:", self.modelis, "Tipas:", self.kuro_tipas)


class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija įkrauta")

    def vaziuoti_automonomiškai(self):
        print("Važiuoja autonomiškai")


toyota = Automobilis(2015, "Toyota Avensis", "Dyzelinas")
tesla = Elektromobilis(2018, "Telsla Model S", "Elektra")

toyota.vaziuoti()
toyota.stoveti()
toyota.pildyti_degalu()
tesla.pildyti_degalu()
tesla.vaziuoti_automonomiškai()


"""
Sukurti programą, kuri:

Turėtų klasę Darbuotojas

Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo

Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)

Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)

Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą turint omeny, kad darbuotojas dirba 5 dienas per savaitę (o ne 7, kaip įprastas darbuotojas).

Sukurti norimą Darbuotojo objektą

Sukurti norimą NormalusDarbuotojas objektą

Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima
"""

import datetime


class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo
        self.dirba_nuo_datetime = datetime.datetime.strptime(dirba_nuo, "%Y-%m-%d")

    def _kiek_nudirbo_dienu(self):
        skirtumas = datetime.datetime.today() - self.dirba_nuo_datetime
        return skirtumas.days

    def paskaiciuoti_atlyginima(self):
        return self._kiek_nudirbo_dienu() * 8 * self.valandos_ikainis


class NormalusDarbuotojas(Darbuotojas):
    def _kiek_nudirbo_dienu(self):
        return round(super()._kiek_nudirbo_dienu() / 7 * 5)


darbuotojas1 = Darbuotojas("Tomas", 20, "2000-12-12")
darbuotojas2 = NormalusDarbuotojas("Domas", 20, "2000-12-12")
print(darbuotojas1.paskaiciuoti_atlyginima())
print(darbuotojas2.paskaiciuoti_atlyginima())