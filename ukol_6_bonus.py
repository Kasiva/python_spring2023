# ukol_6_bonus

import re
# varianta 1 definice funkci:
#overeni uzivatelskeho_jmena
# napr:regularni vyraz ^[a-zA-Z]{6,10}$ https://regex101.com/r/whTA4w/1 
def kontrola_uzivatelske_jmeno(jmeno):
    regularni_vyraz_jmeno = re.compile(r"^[a-zA-Z]{6,10}$")
    jmeno_ok = regularni_vyraz_jmeno.match(jmeno)
    if jmeno_ok:
        return True
    return False
#overeni hesla
# ^[a-zA-Z0-9._\-\+\=]{12,30}$ funguje https://regex101.com/r/CWa7V1/1
def kontrola_hesla(heslo):
    regularni_vyraz_heslo = re.compile(r"^[a-zA-Z0-9._\-\+\=]{12,30}$")
    heslo_ok = regularni_vyraz_heslo.match(heslo)
    if heslo_ok:
        return True
    return False
#overeni emailu
# [a-z0-9._\-\"\+]+@[a-z0-9-\[\]]+(\.[a-z0-9-]+)* funguje vybere vsechny platne, ale i par neplatnych:-(, https://regex101.com/r/40JmDJ/1
def kontrola_email(email):
    regularni_vyraz_email = re.compile(r"[a-z0-9._\-\"\+]+@[a-z0-9-\[\]]+(\.[a-z0-9-]+)*")
    email_ok = regularni_vyraz_email.match(email)
    if email_ok:
        return True
    return False

""" # varianta 2 definice funkci:
#overeni uzivatelskeho_jmena
# napr:regularni vyraz ^[a-zA-Z]{6,10}$ https://regex101.com/r/whTA4w/1 
def kontrola_uzivatelske_jmeno(jmeno):
    if re.match(r"^[a-zA-Z]{6,10}$", jmeno):
        return True
    return False

#overeni hesla
# ^[a-zA-Z0-9._\-\+\=]{12,30}$ funguje https://regex101.com/r/CWa7V1/1
def kontrola_hesla(heslo):
    if re.match(r"^[a-zA-Z0-9._\-\+\=]{12,30}$", heslo):
        return True
    return False

#overeni emailu
# [a-z0-9._\-\"\+]+@[a-z0-9-\[\]]+(\.[a-z0-9-]+)* funguje vybere vsechny platne, ale i par neplatnych:-(, https://regex101.com/r/40JmDJ/1
def kontrola_email(email):
    if re.match(r"[a-z0-9._\-\"\+]+@[a-z0-9-\[\]]+(\.[a-z0-9-]+)*", email):
        return True
    return False """

jmeno = input("Zadejte své uživatelské jméno: ")
while not kontrola_uzivatelske_jmeno(jmeno): #dela se stale dokola pokud return False tak se provede nasledujici
    jmeno = input("Nesprávné uživatelské jméno! Uživatelské jméno musí mít délku 6-10 a obsahovat pouze písmena. Pokud chcete pokračovat zadejte správné uživatelské jméno!: ")

heslo = input("Zadejte své heslo: ")
while not kontrola_hesla(heslo):
    heslo = input("Nesprávné heslo! Heslo musí mít délku 12-30 a obsahovat pouze písmena, číslice a speciální znaky (_-.+=). Pokud chcete pokračovat zadejte správné heslo!: ")

email = input("Zadejte svoji e-mail adresu: ")
while not kontrola_email(email):
    email = input("Nesprávná e-mail adresa! Pokud chcete pokračovat zadejte správnou e-mail adresu!: ") 

print("Všechny údaje jsou správně zadané.")



