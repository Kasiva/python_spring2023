#zadani:
#Krom souboru s body si ulož a načti do druhého slovníku ještě soubor bonusy.json. Obsahuje bonusové body získané během semestru. Pozor, bonusové body získali jen někteří žáci.

#Tvým úkolem je žákům přiřadit známky na základě součtu bodů z písemky a #bonusových bodů. Bodová rozhraní (vztahují se na součet) najdeš zde:

#1: 90 a více
#2: 70-89
#3: 50-69
#4: 30-49
#5: 28 a méně
#nacteni slovniku body a bonusy
import json

with open('body.json', encoding='utf-8') as soubor:
    body = json.load(soubor)
#print(body)
#print(len(body))
print(body["Blanka Kučerová"])
print()
with open('bonusy.json', encoding='utf-8') as soubor:
    bonusy = json.load(soubor)
#print(bonusy)
print(bonusy["Blanka Kučerová"])
print()
#vytvoreni slovniku znamky
#bude to soucet hodnot pro klic ze slovniku body viz povinny ucet a bonusy pro klic, ktery se rovna klici ve slovniku body
pre_znamky = {}
for jmeno, hodnoceni in body.items():
    if jmeno in bonusy:
        pre_znamky[jmeno] = hodnoceni + bonusy[jmeno]
    else:
        pre_znamky[jmeno] = hodnoceni
#print(pre_znamky)
#print(len(pre_znamky))
print(pre_znamky["Blanka Kučerová"])
print()
znamky = {}
for jmeno, pre_znamky in body.items():
    if pre_znamky <= 29:
        znamky[jmeno] = 5
    elif pre_znamky >= 30 and pre_znamky<= 49:
        znamky[jmeno] = 4
    elif pre_znamky >= 50 and pre_znamky<= 69:
        znamky[jmeno] = 3
    elif pre_znamky >= 70 and pre_znamky<= 89:
        znamky[jmeno] = 2
    else:
        znamky[jmeno] = 1
#print(len(znamky))
#print(znamky)
print(znamky["Blanka Kučerová"])


#Výsledný slovník ulož jako JSON do souboru znamky.json.
#ulozeni vysledneho slovniku do souboru 
#with open("znamky.json", mode="w", encoding="utf-8") as vystupni_soubor:
#    json.dump(znamky, vystupni_soubor, ensure_ascii=False, indent=4)
