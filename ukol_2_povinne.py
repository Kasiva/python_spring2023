#Zadání:
#Vyvíjíš software pro obchod s elektronickými součástkami. 
#Firma eviduje informace o počtu součástek na skladě ve slovníku.
#Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.
#slovnik:
#Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník.
#Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit.
#Obě informace si ulož. Následně naprogramuj následující varianty:
#var1:Pokud zadaný kód není ve slovníku, není součástka skladem.Vypiš tedy zprávu, že součástka není skladem. _ done
#var2:Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
#var3:Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kod_soucastky = input("Zadej kód součástky: ")
#mnozstvi = int(input("Zadej množství: "))
#var1
if kod_soucastky not in sklad:
    print(f'Bohužel, součástka {kod_soucastky} není na skladě.')
else:
#var2
    mnozstvi = int(input("Zadej množství: "))
    if mnozstvi>int(sklad[kod_soucastky]):
        print(f'Bohužel, součástka {kod_soucastky} je na skladě v omezeném množství. Můžeme prodat pouze {sklad[kod_soucastky]} ks.')
        sklad.pop(kod_soucastky)
        print(sklad)# pro kontrolu
        
    else:    
        print(f'Součástka {kod_soucastky} je na skladě v dostatečném počtu ks. Zákazníkovi je možné prodat požadované množství {mnozstvi} ks.')
        sklad[kod_soucastky] = sklad[kod_soucastky] - mnozstvi
        print(sklad)# pro kontrolu
