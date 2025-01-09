import random

primaLista = random.sample(range(1,100), random.randint(1, 20))
secondaLista = random.sample(range(1,100), random.randint(1, 20))

primaLista.sort()
secondaLista.sort()

listaComuni = [ numero for numero in set(primaLista) if numero in secondaLista]

print(primaLista, secondaLista)
print(listaComuni)