""" Nepovinný bonus:
Tuto část můžeš řešit, pokud už máš první část úkolu hotovou a chceš si ještě něco procvičit.

Napiš program, který bude obsahovat proměnnou jmeno_a_prijmeni. 
Obsah proměnné načti od uživatele pomocí funkce input. Tvůj program postupně vypíše několik způsobů formátování jména:

1 všechna písmena velká (vypíše např. JANA MALÁ) done
2 všechna písmena malá (vypíše např. jana malá) done
3 standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)done
4 iniciály (vypíše např. J. M.)done
5 křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků.
Jinak vypíše standardní variantu, tj. první písmeno velké, další malá 
(u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)podminka done
6 Zaexperimentuj s různými vstupy od uživatele (co třeba JaNA maLá?). """
#Řešení:
 #varianta 1 funguje
print("řěšení bonusu varianta 1")
jmeno = input("Zadej prosím své křestní jméno: ")
prijmeni = input("Zadej prosím své přijmení: ")
#řešení bod 1
print("řěšení bonusu bod 1 varianta 1")
print(f'{jmeno} {prijmeni}'.upper())
#řešení bod 2
print("řěšení bonusu bod 2 varianta 1")
print(f'{jmeno} {prijmeni}'.lower())
#řešení bod 3 pomocí title
print("řěšení bonusu bod 3 varianta 1")
print(f'{jmeno} {prijmeni}'.title())
#řešení bod 4 pomocí title
print("řěšení bonusu bod 4 varianta 1")
print(f'{jmeno[0]}. {prijmeni[0]}.'.title()) 
#řešení bod 5 podmínka
print("řěšení bonusu bod 5 varianta 1")
if len(jmeno) >5: #pocet znaku funkce len ()
    print(f'{jmeno[0]}. {prijmeni}'.title())
else:
    print(f'{jmeno} {prijmeni}'.title())
print(" ") 
#varianta 2 
print("řěšení bonusu varianta 2") 
a = input("Zadej prosím své křestní jméno: ")#jmeno
b = input("Zadej prosím své přijmení: ")#prijmeni
#jmeno_a_prijmeni = ""#jak udelam promenou ze dvou promenych?
jmeno_a_prijmeni = a + " " + b
#test proměnný
#print("test proměnné")
#print(f"{jmeno_a_prijmeni}") #funguje
#řešení bod 1
print("řěšení bonusu bod 1 varianta 2")
print(f'{jmeno_a_prijmeni}'.upper()) #funguje
#řešení bod 2
print("řěšení bonusu bod 2 varianta 2")
print(f'{jmeno_a_prijmeni}'.lower()) #funguje
#řešení bod 3 pomocí title
print("řěšení bonusu bod 3 varianta 2")
print(f'{jmeno_a_prijmeni}'.title()) #funguje title změní první písmeno každého slova - mezery apostrof a pod
#řešení bod 4 pomocí title
print("řěšení bonusu bod 4 varianta 2")
x_prijmeni = jmeno_a_prijmeni.find(" ") 
print(f'{jmeno_a_prijmeni[0]}. {jmeno_a_prijmeni[x_prijmeni + 1]}.'.title())
#řešení bod 5 podmínka
print("řěšení bonusu bod 5 varianta 2")
if len(a) >5: #pocet znaku funkce len ()
    print(f'{a[0]}. {b}'.title())
else:
    print(f'{jmeno_a_prijmeni}'.title()) 