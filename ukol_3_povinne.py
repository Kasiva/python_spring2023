#zadani:
#Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.
#bod1:Soubor si ulož a načti do slovníku.
#bod2:Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/#neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a #hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. #Pokud má méně než 60, hodnota bude "Fail".
#bod3:Výsledný slovník ulož jako JSON do souboru prospech.json.
#reseni:
import json
with open('body.json', encoding='utf-8') as soubor:
    body = json.load(soubor)
#print(body) #kontrola obsahu
#print(type(body)) #kontrola typu
#vytvoreni slovniku:
prospech = {}
for jmeno, hodnoceni in body.items():
    print(jmeno, hodnoceni) #kontrola vysledku prvni cast
    if hodnoceni < 60:
        prospech[jmeno] = "Fail"
    else:
        prospech[jmeno] = "Pass"
    print(prospech[jmeno]) #kontrola vysledku druha cast
#ulozeni slovniku jako soubor prospech.json
with open("prospech.json", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(prospech, vystupni_soubor, ensure_ascii=False, indent=4)
