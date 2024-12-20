def elemento_presente(numero: int, lista_numeri: list[int]):
    if numero in lista_numeri:
        return True
    else:
        return False

def elemento_presente_binary_search(numero: int, lista_numeri: list[int]):

    while len(lista_numeri) > 1:
        indice = len(lista_numeri) // 2
        
        if numero < lista_numeri[indice]:
            lista_numeri = lista_numeri[0:indice]
        else:
            lista_numeri = lista_numeri[indice:]

    if len(lista_numeri) == 0:
        return False
    elif lista_numeri[0] == numero:
        return True
    else: 
        return False

numero_da_cercare = int(input("Ciao, che numero vuoi cercare all'interno della lista? "))
lista_interi = [1, 3, 5, 30, 42, 43, 500]

print(elemento_presente(numero_da_cercare, lista_interi))
print(elemento_presente_binary_search(numero_da_cercare, lista_interi))