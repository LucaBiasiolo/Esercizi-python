def leggi_file_1():
    with open("nomi_1.txt",'r') as file_nomi:
        stringa_nomi = file_nomi.read()

    lista_nomi_file = stringa_nomi.split("\n")
    nomi = set(lista_nomi_file)

    dizionario_nomi_occorrenze = {}
    for nome in  nomi:
        occorrenze_nome = lista_nomi_file.count(nome)
        dizionario_nomi_occorrenze[nome] = occorrenze_nome
    return dizionario_nomi_occorrenze

def leggi_file_2():
    with open("nomi_2.txt",'r') as file_nomi:
        stringa_file = file_nomi.read()
    lista_percorsi_file = stringa_file.split("\n")

    lista_nomi_foto = []
    for percorso_file in lista_percorsi_file:
        nome_foto = percorso_file.split("/")[2]
        lista_nomi_foto.append(nome_foto)

    insieme_nomi_foto_unici = set(lista_nomi_foto)

    dizionario_nomi_foto_occorrenze = {}
    for nome_foto in insieme_nomi_foto_unici:
        occorrenze_nome_foto = lista_nomi_foto.count(nome_foto)
        dizionario_nomi_foto_occorrenze[nome_foto] = occorrenze_nome_foto

    return dizionario_nomi_foto_occorrenze

dizionario_nomi_occorrenze = leggi_file_2()
for nome in dizionario_nomi_occorrenze:
    print("Il nome ", nome, " compare ", dizionario_nomi_occorrenze[nome], " volte nel file.")
