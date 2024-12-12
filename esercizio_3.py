numeroSoglia: int = int(input("Ciao, sono Python. Per favore dammi un numero naturale "));

listaNumeri: list[int] = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
listaFiltrata: list[int] =[];
for numero in listaNumeri:
    if numero < numeroSoglia:
        listaFiltrata.append(numero);

print(listaFiltrata);

print([ numero for numero in listaNumeri if numero < numeroSoglia])