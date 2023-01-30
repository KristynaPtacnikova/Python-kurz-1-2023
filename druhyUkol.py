sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
nazevKodu = input("Zadejte kod soucastky: ")
dotaz_pocet = input("Zadejte počet: ")

# Vypis hodnoty
#kodSoucastky = "1N4148"
#print(f'klic: {kodSoucastky}, hodnota: {sklad[kodSoucastky]}') 

#if nazevKodu in sklad:
#    sklad[nazevKodu] = int(sklad[nazevKodu]) - int(dotaz_pocet)
#   print(f'{nazevKodu} na skladě zbývá {sklad[nazevKodu]} ks.')
#else:
#    print(f'{nazevKodu} není skladem')

#if int(dotaz_pocet)>= int(sklad[nazevKodu]):
#    print(f'{nazevKodu} Nelze koupit celý počet, máme jen omezené množství ks.')

if int(dotaz_pocet)< int(sklad[nazevKodu]):
    sklad[nazevKodu] = (f'(nazevKodu) - (dotaz_pocet)')
    print("Vaši poptávku vyřídíme v plné výši.")