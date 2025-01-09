def trovaDivisori(numero):
    listaPossibiliDivisori = list(range(1, numero +1))

    listaDivisori: list[int] = []
    for possibileDivisore in listaPossibiliDivisori:
        if numero % possibileDivisore == 0:
            listaDivisori.append(possibileDivisore)
    
    return listaDivisori

numero: int = int(input("Ciao, sono Python. Dammi un numero naturale maggiore di 0 per favore "))
if numero <=0 :
    print("Il numero non è maggiore di 0")

listaDivisori = trovaDivisori(numero)
print(listaDivisori)

if listaDivisori ==[1, numero]:
    print("Il numero è primo")
else:
    print("Il numero non è primo")