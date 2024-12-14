import random

tentativi: int = 1
numeroDaIndovinare = random.randint(1,9)

while True:

    numeroUtente = int(input("Ciao, sono Python. Prova ad indovinare un numero da 1 a 9: "))
    tentativi +=1
    if numeroUtente > numeroDaIndovinare:
        print("Il numero è troppo alto")
    elif numeroUtente < numeroDaIndovinare:
        print("Il numero è troppo basso")
    else:
        print("Esatto! Hai provato " + str(tentativi) + " volte")
        break

    giocaAncora = input("Vuoi giocare ancora? Y/N ")
    if giocaAncora.upper() == 'N':
        break
