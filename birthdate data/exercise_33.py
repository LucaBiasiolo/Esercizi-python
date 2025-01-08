birthday_dictionary = {"luca biasiolo": "01/10/1994", "elia signorini": "28/12/94", "angie trapani": "13/01/94", "maurizio biasiolo": "01/01/62"}
print("Hi, i'm Python. Welcome to birthday dictionary. We know the birthday dates of")

for key in birthday_dictionary.keys():
    print(key)

person = input("Whose birthday do you want to look up? use name and surname in lowercase letters: ")

if person in birthday_dictionary.keys():
    print(f"{person}'s birthday is {birthday_dictionary[person]}")
else:
    print("Person not found on birthdays dictionary")