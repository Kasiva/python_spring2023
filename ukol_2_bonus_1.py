#Zadání:
#Ve slovníku zde najdeš Morseovu abecedu, kde jako klíč slouží znak v klasické abecedě a jako hodnota zápis znaku v Morseově abecedě.
#bod1:done
# Napiš program, který se uživatele zeptá na text, který chce zapsat v Morseově abecedě. Uvažuj disciplinovaného uživatele, který zadává pouze znaky bez diakritiky, malá písmena atd. Na začátku uvažuj i to, že uživatel nezadává mezery.
#bod2:done
#Projdi řetězec zadaný uživatelem. Najdi každý znak ve slovníku a vypiš ho na obrazovku v Morseově abecedě.
#bod3:done
#Abychom měli celý kód vypsaný na jedné řádce, požádáme funkci print(), aby na konci výpisu nevkládala znak pro konec řádku, ale mezeru. To uděláme tak, že jako druhý arugument funkce dáme argument end=" ".
#bod4:
#Nyní přidáme mezery. Uvažuj, že uživatel může zadat mezeru. Před tím, než budeš hledat znak ve slovníku, zkontroluj, zda znak není mezera. Pokud ano, vypiš znak lomítka /.
#Slovnik:
morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

#reseni_var1
print(f'Řešení varianta 1.')
text = input("Napište text, který chcete přepsat v Morseově abecedě. ") 
print(f'Zadaný text je: {text}.') #pro kontrolu
delka_textu = len(text)
#print(f'delka zadaného textu je: {delka_textu}.') #pro kontrolu
#print(f'první znak zadaného textu je: {text[0]}.') #pro kontrolu
#potrebuji jednotlive znaky v textu najit ve slovniku tzn. potrebuji znaky na indexech text[0] az text[-1] a k nim priradit odpovidajici hodnoty
#for counter in range(0,delka_textu): #varianta zapisu
for counter in range(delka_textu): #varianta zapisu
    if text[counter] == " ":#bod 4
        print("/",end=" ")
#        print(f'/',end=" ") #tento zapis by mel dat stejny vystup jako tento print("/",end=" ")
    else:
        if text[counter] in morse_code:
#             print(f'{morse_code[text[counter]]}') #tisk varianta bodu 2
            print(f'{morse_code[text[counter]]}',end=" ") #tisk varianta bodu 3
print(" ")
#reseni_var2
print(" ")
print(f'Řešení varianta 2.')
morse_code[" "] = "/" #upravit slovnik a pak odpada testovani na mezeru 
#print(morse_code)#pro kontrolu
text = input("Napište text, který chcete přepsat v Morseově abecedě. ") 
print(f'Zadaný text je: {text}.')
delka_textu = len(text)
#for counter in range(0,delka_textu): #varianta zapisu
for counter in range(delka_textu): #varianta zapisu
    if text[counter] in morse_code:
#        print(f'{morse_code[text[counter]]}') #tisk varianta bodu 2
            print(f'{morse_code[text[counter]]}',end=" ") #tisk varianta bodu 3
morse_code.pop(" ")
#print(" ")
#print(morse_code)#pro kontrolu


