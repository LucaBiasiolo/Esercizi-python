def rovescia_frase(frase: str):
    lista_frase = frase.split()
    lista_frase_rovesciata = lista_frase[::-1]

    frase_rovesciata = ""

    for parola in lista_frase_rovesciata:
        frase_rovesciata = frase_rovesciata +" "+ parola
    return frase_rovesciata

frase: str = input("Ciao, sono Python. Inserisci una frase: ");

print(rovescia_frase(frase))