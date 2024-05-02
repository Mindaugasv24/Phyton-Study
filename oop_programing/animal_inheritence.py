"""3. Paveldėjimas (Inheritance) – galimybė apjungti panašių objektų funkcionalumą, naudojant tėvines klases.
Tai leidžia nekartoti panašaus ar to paties kodo. Taip pat nekeičiant paties objekto kodo,
papildyti arba keisti jo funkcionalumą."""

class Gyvunas():
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print("Bėgu")


class Kate(Gyvunas):
    def miaukseti(self):
        print("Miau")


class Suo(Gyvunas):
    def loti(self):
        print("Au")


vezlys = Gyvunas("Tadas", "Rudas")
vezlys.begti()

# vezlys.miaukseti()

# AttributeError: 'Gyvunas' object has no attribute 'miaukseti'


kate1 = Kate("Mūza", "Pilka")
suo1 = Suo("Čakas", "Baltas")

kate1.begti()

# Bėgu

kate1.miaukseti()

# Miau

kate1.loti()

# AttributeError: 'Kate' object has no attribute 'loti'

suo1.loti()

# Au