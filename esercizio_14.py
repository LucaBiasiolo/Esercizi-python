prima_lista = [1,2,3,4,3,2,1]

def elimina_duplicati(lista):
    lista_senza_duplicati = []
    for elemento in lista:
        if elemento not in lista_senza_duplicati:
            lista_senza_duplicati.append(elemento)
    return lista_senza_duplicati

def elimina_duplicati_con_sets(lista):
    return list(set(lista))

print(elimina_duplicati(prima_lista))
print(elimina_duplicati_con_sets(prima_lista))

#extra 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def elementi_comuni_liste(prima_lista, seconda_lista):
    return set(prima_lista).intersection(set(seconda_lista))

print(elementi_comuni_liste(a,b))