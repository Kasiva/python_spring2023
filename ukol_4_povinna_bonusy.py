""" Zadání
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:
První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.
Tipy:
Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420". """
def kontrola_tel_cisla() -> bool:
# Funkce provadi kontrolu pozadovane delky zadaneho tel.cisla (9 ci 13 cislic/pozic) a zaroven kontroly volacky statu CR +420 - je-li delka tel.cisla 13 pozic. Vrati hodnotu True/False.    
    if (len(upravene_cislo) == 13 and (upravene_cislo[:4]) == "+420") or len(upravene_cislo) == 9: 
        return True
    else:
        return False

def cena_zpravy(text: str, cena_180_znaku: int = 3) -> int:
# Funkce vypocte celkovou cenu zpravy na zaklade zadanych informaci (zadany_text a cena za 180 znaku). Vrati cenu.
    cena = (int(len(text)/180) + 1) * cena_180_znaku 
    return cena

zadane_cislo = input("Zadej tel.číslo příjemce: ")
upravene_cislo = zadane_cislo.replace(" ", "")

if kontrola_tel_cisla():
    zadany_text = input("Zadej zprávu, kterou chceš poslat: ")
    pocet_znaku = len(zadany_text)
#    print(pocet_znaku) # informace pro kontrolu vypoctu
    print(f"Zpráva stojí {cena_zpravy(zadany_text)} Kč.")
#    print(f"Zpráva stojí {cena_zpravy(zadany_text, 4)} Kč.") # varianta pri zmene default parametru
else:
    print("Zadané číslo není v požadovaném formátu. Zadejte znovu.")

""" Nepovinný bonus 1 obsazeno v reseni viz vyse
Zkus svoji první funkci upravit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš například tak, že použiješ metodu .replace(). První parametr metody replace je znak, který chceš nahradit, a druhý parametr nový znak. Pokud se chceš nějakého znaku zbavit, "nahraď" ho prázdným řetězcem "".

Odkaz na dokumentaci metody replace: https://docs.python.org/3/library/stdtypes.html#str.replace

Nepovinný bonus 2 obsazeno v reseni viz vyse
Přidej svým funkcím typování, aby bylo jasné, jaký typy mají parametry tvých funkcí a jaká je návratová hodnota tvých funkcí.

K typování se dostaneme až v 5. lekci. Pokud chceš, můžeš úlohu řešit předem pomocí Čtení na doma """
