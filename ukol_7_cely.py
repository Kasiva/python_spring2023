""" ukol-07: Evidence aut - povinná část
Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
4A2 3020	        Peugeot 403 Cabrio	    47534
1P3 4747	        Škoda Octavia	        41253
Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy: done

registrační značka automobilu     registracni_znacka,
značka a typ vozidla              typ_vozidla,
počet najetých kilometrů          najete_km,
informaci o tom, jestli je vozidlo aktuálně volné dostupne (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).

Vytvoř metodu __init__() pro třídu Auto. 
Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu. 
Poslední atribut rovnou nastav jako True, tj. na začátku je vozidlo vždy volné. done

Vytvoř objekty, které reprezentují oba automobily půjčovny. done

Třídě Auto přidej metodu 
pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu dostupne, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".

Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto().

Otestuj, že program nedovolí půjčit stejné auto dvakrát.

Bonus:
Přidej třídě Auto metodu vrat_auto(), která bude mít (krom obligátního self) 2 parametry, a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return.
 """

class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
# atribut dostupnost_vypujceni zapis prirazene hodnoty "natvrdo"        
        self.dostupnost_vypujceni = True

    def pujc_auto(self):
        if self.dostupnost_vypujceni:
            self.dostupnost_vypujceni = False
            return f"Potvrzuji zapůjčení vozidla: {self.typ_vozidla} SPZ: {self.registracni_znacka}."
        else:
            return f"Vozidlo: {self.typ_vozidla} SPZ: {self.registracni_znacka} není k dispozici."

    def get_info(self):   
        return f"Vozidlo: {self.typ_vozidla} SPZ: {self.registracni_znacka} stav tachometru: {self.najete_km} km."
    
    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.dostupnost_vypujceni = True
        vypujcka_ujete_km = stav_tachometru - self.najete_km
        self.najete_km = stav_tachometru
        cena = 0
        if pocet_dni < 7:
            cena = pocet_dni * 400
        else:
            cena = pocet_dni * 300
        return f"Cena za půjčení vozidla {self.typ_vozidla} je {cena} Kč."

def muj_tisk(auto):
    print("\nNásleduje výpis požadavků ze zadání povinné části ůkolu.\n")
    print(auto.get_info())
    print(auto.pujc_auto(), "\n")
    print("Následuje kontrola, že zvolené vozidlo nemůže být znovu zapůjčeno.")
    print(auto.pujc_auto(), "\n") 
    print("Následuje kontrola bonusové části ůkolu.\n")
    print(auto.vrat_auto(50000, 3), "\n")
    print("Následuje kontrola, že vrácené vozidlo má nový stav tachometru.")
    print(auto.get_info())
    print("\nNásleduje kontrola, že vrácené vozidlo může být znovu zapůjčeno.")
    print(auto.pujc_auto(), "\n")

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534) 
skoda = Auto("1P3 4747", "Škoda Octavia", 41253) 

zadani = input("Vítejte na stránkách naší půjčovny aut.\nK dispozici máte dva typy vozidel: Peugeot a Škoda.\nZadejte vybrané vozidlo.\nPro Peugeot zadejte 1 pro Škoda zadejte 2: ")
# Andy dekuji za typ na slovnik, puvodne jsem mela "proste if/elif/else" a pak jsem zkousela seznam (a tam jsem se motala:-)), ale slovnik je nejkratsi:-)
# pro vstup jsem zvolila hodnoty 1/2 misto slov. Pokud by se zadavala slova tak jen vsude v kodu bude "1" nahrazena "Peugeot" a "2" "Škoda".
vypujcka = {
    "1": peugeot,
    "2": skoda
}

if zadani not in vypujcka:
    print("Tento typ vozidla není k dispozici.")
else:
    auto = vypujcka[zadani]
    muj_tisk(auto)