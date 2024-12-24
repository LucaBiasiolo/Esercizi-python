lista_numeri_primi = []
with open("numeri_1.txt", 'r') as file_numeri_primi:
    lista_numeri_primi = file_numeri_primi.read().split("\n")

lista_numeri_felici = []
with open("numeri_2.txt", 'r') as file_numeri_felici:
    lista_numeri_felici = file_numeri_felici.read().split("\n")

lista_numeri_comuni = []

for numero_primo in lista_numeri_primi:
    if numero_primo in lista_numeri_felici:
        lista_numeri_comuni.append(numero_primo)

print(lista_numeri_comuni)
