def genera_riga(n):
    return " --- " * n

def genera_colonna(n):
    return "|    " *(n+1)

n = int(input("Benvenuto nel generatore di griglie per giochi. Quante celle deve avere un lato della griglia? "))

riga = genera_riga(n)
colonna = genera_colonna(n)

griglia = ""
for _ in range(n):
    griglia += riga + "\n" + colonna + "\n"

griglia += riga #genero riga finale

print(griglia)