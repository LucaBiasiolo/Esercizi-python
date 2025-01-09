def rovesciaStringa(stringa: str):
    stringaRovesciata = "";

    for carattere in stringa:
        stringaRovesciata = carattere + stringaRovesciata;
    return stringaRovesciata;

parola = input("Ciao, sono Python. Per favore dammi una stringa: ");

print(parola);
parolaRovesciata = rovesciaStringa(parola);
print(parolaRovesciata);

if (parola == parolaRovesciata):
    print("La parola è palindroma");
else:
    print("La parola non è palindroma");
