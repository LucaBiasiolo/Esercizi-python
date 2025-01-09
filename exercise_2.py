numero = int(input("Ciao, sono Python. Dammi un numero naturale per favore: "));

if numero % 2 == 0:
    print("Numero pari");
else:
    print("Numero dispari");

#extra 1 
if numero % 4 == 0:
    print("Numero multiplo di 4");

#extra 2
num = int(input("Inserisci il numero da controllare: "));
check = int(input("Inserisci il numero per cui dividere: "));

if num % check == 0 :
    print("Il numero da controllare è multiplo del secondo");
else:
    print("Il numero da controllare non è multiplo del secondo");