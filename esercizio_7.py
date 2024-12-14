listaNumeri: list[int] = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

listaPari = [numero for numero in listaNumeri if numero % 2== 0];
listaPosizioniPari = [numero for numero in listaNumeri[::2]];

print(listaNumeri, listaPari, listaPosizioniPari);
