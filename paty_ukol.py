#1.Vytvoř seznam průměrných teplot pro každý den.
#2.Vytvoř seznam ranních teplot.
#3.Vytvoř seznam nočních teplot.
#4.Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
def average(teploty):
    """Spocita prumer teplot pro jeden den, vstupni parametr `teploty` jsou desetinna cisla v seznamu."""
    return sum(teploty) / len(teploty)

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8],
]
prumery = [average(den) for den in teploty]
print(prumery)

#1. seznam průměrných hodnot

prumerne_teploty = [sum(hodnota)/4 for hodnota in teploty]
print(prumerne_teploty)

prumerne_teploty = []
for hodnota in teploty:
    prumerne_teploty.append(sum(hodnota)/4)
print(prumerne_teploty)

#2. seznam rannich teplot
#1.metoda
ranni_teploty = []
for teplota in teploty:
    print(teplota[0])
#2.metoda
ranni_teploty = [print(teplota[0])for teplota in teploty]

#3.seznam nocnich teplot
#1.metoda
nocni_teploty = []
for teplota in teploty:
    print(teplota[-1])
#2.metoda
nocni_teploty = [print(teplota[-1])for teplota in teploty]
#4. seznam dvouprvku
#1.metoda
dve_teploty = []
for teplota in teploty:
    print(teplota[-3:-1])
#2.metoda
dve_teploty = [print(teplota[-3:-1])for teplota in teploty]
