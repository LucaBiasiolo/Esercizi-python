def genera_fibonacci(quanti_fibonacci):
    if quanti_fibonacci < 1:
        print("Errore, numero non valido");
        return []
    elif quanti_fibonacci == 1:
        return [0]
    elif quanti_fibonacci == 2:
        return [0,1]
    else:
        fibonacci_n_meno_2 = 0
        fibonacci_n_meno_1 = 1

        lista_fibonacci = [0,1]

        #uso metodo iterativo per generare numeri di Fibonacci
        for _ in range(quanti_fibonacci -2):
            fibonacci_n = fibonacci_n_meno_1 + fibonacci_n_meno_2
            lista_fibonacci.append(fibonacci_n)

            fibonacci_n_meno_2 = fibonacci_n_meno_1
            fibonacci_n_meno_1 = fibonacci_n
        return lista_fibonacci

quanti_fibonacci = int(input("Ciao, sono Python. Quanti numeri di Fibonacci vuoi generare? "))

print(genera_fibonacci(quanti_fibonacci))