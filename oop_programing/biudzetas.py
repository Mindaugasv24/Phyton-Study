"""Padaryti minibiudžeto programą, kuri:
Leistų vartotojui įvesti pajamas
Leistų vartotojui įvesti išlaidas
Leistų vartotojui parodyti pajamų/išlaidų balansą
Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
Leistų vartotojui išeiti iš programos"""

class Irasas:
    """r"""
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        return f"{self.tipas}: {self.suma}"


class Biudzetas:
    """r"""
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        """r"""
        pajamos = Irasas("Pajamos", suma)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma):
        """r"""
        islaidos = Irasas("Išlaidos", suma)
        self.zurnalas.append(islaidos)

    def gauti_balansą(self):
        """r"""
        suma = 0
        for irasas in self.zurnalas:
            if irasas.tipas == "Pajamos":
                suma += irasas.suma
            if irasas.tipas == "Išlaidos":
                suma -= irasas.suma
        print(suma)

    def parodyti_ataskaita(self):
        """r"""
        for irasas in self.zurnalas:
            print(f"{irasas.tipas}: {irasas.suma}")


biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n9 - išeiti iš programos"))
    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        biudzetas.prideti_pajamu_irasa(suma)
    if pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        biudzetas.prideti_islaidu_irasa(suma)
    if pasirinkimas == 3:
        biudzetas.gauti_balansą()
    if pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()
    if pasirinkimas == 9:
        print("Viso gero")
        break
