stringa: str = input("Ciao, sono Python. Dammi una stringa per favore: ");

stringa = stringa.lower();

stringaLista = list(stringa);

stringaListaRovesciata = stringaLista[::-1];

print(stringaLista, stringaListaRovesciata);

if (stringaLista == stringaListaRovesciata):
    print("La stringa è palindroma");
else:
    print("La stringa non è palindroma");
