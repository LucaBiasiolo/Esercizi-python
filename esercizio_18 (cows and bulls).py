import random;

print("Ciao, benvenuto nel gioco Cows and Bulls")
numero_da_indovinare = f"{random.randint(0, 9999):04}"
numero_da_indovinare_lista = list(numero_da_indovinare)
numero_tentativi = 0

while True:
    tentativo = input("Inserisci un numero a 4 cifre: ")
    if len(tentativo) != 4 or not tentativo.isdigit():
        print("Per favore, inserisci un numero valido a 4 cifre.")
        continue
    numero_tentativi += 1
    tentativo_lista = list(tentativo)

    print(numero_da_indovinare_lista)

    numero_cows = 0
    numero_bulls = 0

    for posizione_cifra in range(4):
        if numero_da_indovinare_lista[posizione_cifra] == tentativo_lista[posizione_cifra]:
            numero_cows += 1
        else:
            if numero_da_indovinare_lista[posizione_cifra] in tentativo_lista:
                numero_bulls += 1

    if numero_cows == 4:
        print("Hai indovinato in " + str(numero_tentativi) + " tentativi!")
        break

    print("Numero cows =" + str(numero_cows) + " , numero bulls =" + str(numero_bulls))
