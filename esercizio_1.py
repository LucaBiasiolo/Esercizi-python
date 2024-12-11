nome = input("Ciao, sono Python. Come ti chiami? \n");
print("Benvenuto " + nome);
eta = int(input("Quanti anni hai? \n"));
annoCentenario = 2024 - eta + 100;
messaggioCentenario = "Diventerai centenario nel ..." + str(annoCentenario);
print(messaggioCentenario);

#extra
numeroRipetizioni = int(input("Quante volte vuoi ripetere il precedente messaggio? "));

for indice in range(numeroRipetizioni):
    print(messaggioCentenario);
