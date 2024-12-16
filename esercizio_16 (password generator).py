#Write a password generator in Python. Be creative with how you generate passwords - 
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#Extra:
#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random
import string

debole_o_forte: str = input("Ciao, sono Python. Benvenuto nel generatore di Password. Vuoi generare una password debole o forte? d/f ")
if debole_o_forte == 'f':
    lunghezza_password = int(input("Quanto lunga deve essere la password? "))

    if lunghezza_password <= 0:
        print("Errore, la lunghezza non può essere negativa o nulla")
    else:
        caratteri_possibili: str = string.ascii_letters + string.digits + string.punctuation
        password_lista = random.sample(caratteri_possibili, lunghezza_password)
        password = "".join(password_lista)
        print(password)
elif debole_o_forte == 'd':
    lista_parole = ['dog', 'cat', 'monkey', 'horse', 'bear', 'mouse', 'dolphin', 'dodo', 'bird', 'robin']
    lista_aggettivi = ['obese', 'epic', 'legendary', 'posh', 'dry', 'stinky', 'clockwork', 'howling', 'screaming', 'whistling']

    parola = random.choice(lista_parole)
    aggettivo = random.choice(lista_aggettivi)

    password = aggettivo + "_" + parola

    print(password)
else:
    print("Scelta non valida, inserire d o f")