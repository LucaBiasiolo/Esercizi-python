import random;

lunghezzaPrimaLista = random.randint(1, 20);
lunghezzaSecondaLista = random.randint(1, 20);

primaLista: list[int] = [];
secondaLista: list[int] = [];

for x in range(0, lunghezzaPrimaLista):
    primaLista.append(random.randint(0, 100));
for x in range(0, lunghezzaSecondaLista):
    secondaLista.append(random.randint(0, 100));

primaLista.sort();
secondaLista.sort();

print(primaLista);
print(secondaLista);

listaElementiInComune: list[int] = [];
for x in primaLista:
    for y in secondaLista:
        if x == y :
            if x not in listaElementiInComune:
                listaElementiInComune.append(x);

print(listaElementiInComune);
