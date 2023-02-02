#zadani:
#Krom souboru s body si ulož a načti do druhého slovníku ještě soubor bonusy.json. Obsahuje bonusové body získané během semestru. Pozor, bonusové body získali jen někteří žáci.

#Tvým úkolem je žákům přiřadit známky na základě součtu bodů z písemky a #bonusových bodů. Bodová rozhraní (vztahují se na součet) najdeš zde:

#1: 90 a více
#2: 70-89
#3: 50-69
#4: 30-49
#5: 29 a méně
import json
with open('body.json', encoding='utf-8') as soubor:
    body = json.load(soubor)
with open('bonusy.json', encoding='utf-8') as soubor:
    bonusy = json.load(soubor)
pre_znamky = {}
for jmeno, hodnoceni in body.items():
    pre_znamky[jmeno] = hodnoceni
    if jmeno in bonusy:

       pre_znamky[jmeno] += bonusy[jmeno] 
znamky = {}
for jmeno, pre_znamky in pre_znamky.items():
#    print(jmeno, pre_znamky) #kontrola
    if pre_znamky <= 29:
        znamky[jmeno] = 5
    elif pre_znamky <= 49:
        znamky[jmeno] = 4
    elif pre_znamky <= 69:
        znamky[jmeno] = 3
    elif pre_znamky <= 89:
        znamky[jmeno] = 2
    else:
        znamky[jmeno] = 1
#    print(znamky[jmeno])#kontrola
with open("znamky.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(znamky, vystupni_soubor, ensure_ascii=False, indent=4)
