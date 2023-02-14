#  []  {}
#Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

#1.Vytvoř seznam průměrných teplot pro každý den. done
#2.Vytvoř seznam ranních teplot. done
#3.Vytvoř seznam nočních teplot. done
#4.Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu. done
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#1.Vytvoř seznam průměrných teplot pro každý den.

prumerna_denni_teplota = [round(sum(den)/len(den), 2) for den in teploty]

print(f'Průměrná denní teplota je: {prumerna_denni_teplota}')

#2.Vytvoř seznam ranních teplot.

ranni_teploty = [den[0] for den in teploty]
print(f'Ranní teploty jsou: {ranni_teploty}')

#3.Vytvoř seznam nočních teplot.

nocni_teploty = [den[-1] for den in teploty]
print(f'Noční teploty jsou: {nocni_teploty}')

#4.Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

poledni_nocni_teploty = [[den[1],den[-1]]for den in teploty]
print(f'Polední a noční teploty jsou: {poledni_nocni_teploty}')