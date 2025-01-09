numeroDaDividere: int = int(input("Ciao, sono Python. Dammi un numero naturale per favore "));

listaPossibiliDivisori = list(range(1,numeroDaDividere +1));

for possibileDivisore in listaPossibiliDivisori:
    if numeroDaDividere % possibileDivisore == 0:
        print(possibileDivisore);
