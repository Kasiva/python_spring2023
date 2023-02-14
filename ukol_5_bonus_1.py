#  []  {}
#Nepovinný bonus 1
#Krom teplot máme k dispozici i informaci o dnu v týdnu:
#Pomocí dict comprehension vytvoř slovník, který bude mít následující formát, kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den.
#{den: průměrná teplota}

teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

slovnik_prumerna_teplota = {den[0]: round(sum(den[1:])/len(den[1:]), 2) for den in teploty}

print(slovnik_prumerna_teplota)