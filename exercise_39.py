import datetime

nome = input("Ciao, sono Python. Come ti chiami? ")
print(f"Benvenuto {nome}")
age = int(input("Quanti anni hai? "))
annoCentenario = datetime.datetime.now().year - age + 100
messaggioCentenario = f"Diventerai centenario nel {str(annoCentenario)}"
print(messaggioCentenario)