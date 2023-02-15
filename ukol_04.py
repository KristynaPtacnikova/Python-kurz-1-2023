import math

def telefonni_cislo(vloz_cislo:int):#Overi spravnou delku cisla
    max_delka = 13
    text = input(str("Zadejte text:"))
    delka = len(vloz_cislo)
    if delka == max_delka and (vloz_cislo[slice(+420)]):
            return True
    elif delka == 9:
            return True
    elif telefonni_cislo(vloz_cislo) == True:
            print(input("Zadejte text:"))
    else:
            return False

#print(telefonni_cislo(vloz_cislo))

def cena_sms(text:str):# Vykalkuluje nam cenu za pocet(180) znaku
    text = input(str("Zadejte text:"))
    text_delka = len(text)
    zaokrouhleni = (math.ceil(text_delka/180))
    cena = int(zaokrouhleni)*3
    return(cena)

vloz_cislo = input(f"Zadejte tel.číslo:")
# Overime, jestli je platne pomoci nasi funkce telefonni_cislo:
platne_cislo = telefonni_cislo(vloz_cislo)

# Pokud ano, zeptame se na text zpravy a spocitame cenu 
if platne_cislo:
    text_sms = input("Zadejte text:")
    print(f"Vaše sms stojí {cena_sms(text)} Kč.")


