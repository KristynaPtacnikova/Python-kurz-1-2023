"""class Auto:  # definice tridy
    registracni_znacka = ""  # atribut tridy
    typ_vozidla = ""
    najete_km = ""
    dostupnost = ""

auto_1 = Auto()
auto_1.registracni_znacka = "4A2 3020"
auto_1.typ_vozidla = "Peugeot 403 Cabrio"
auto_1.najete_km = "47534 Km"

auto_2 = Auto()
auto_2.registracni_znacka = "1P3 4747"
auto_2.typ_vozidla = "Škoda Octavia"
auto_2.najete_km = "41253 Km"

print(auto_1.registracni_znacka)
"""
class Auto:
    def __init__(self,registracni_znacka,typ_vozidla,najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def get_info(self):
        print(f"SPZ: {self.registracni_znacka}, znacka: {self.typ_vozidla},najeto: {self.najete_km}.")

    def pujc_auto(self):
        self.dostupne = False


    def __str__(self):
        if self.dostupne == True:
            return ("Potvrzuji zapůjčení vozidla.")
        else:
            return ("Vozidlo není k dispozici.")



auto_1 = Auto("4A2 3020","Peugeot 403 Cabrio","47534 Km")
auto_1.pujc_auto()
print(auto_1)
auto_2 = Auto("1P3 4747","Škoda Octavia","41253 Km")
auto_2.get_info()
print(auto_1.najete_km)
print(auto_2.typ_vozidla)

def znacka_vozu(vloz_znacku:str):#Overi spravný výběr
    max_delka = 7
    delka = len(vloz_znacku)
    if delka == max_delka and vloz_znacku(š*[a-zA-Z]):
            return True
    elif delka == 5:
            return True
         
vloz_znacku = input(f"Vyberte si značku vozu?:")
# Overime, jestli je to platne pomoci nasi funkce :
auto_2.get_info()
auto_2.pujc_auto()
print(auto_2)