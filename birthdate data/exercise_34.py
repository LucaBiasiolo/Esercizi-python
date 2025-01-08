import json

with open("./Esercizi/birthdate data/birthdate_dictionary.json") as json_file:
    birthday_dictionary: dict = json.load(json_file)

print("Hi, i'm Python. Welcome to birthday dictionary. We know the birthday dates of")

for key in birthday_dictionary.keys():
    print(key)

person = input("Whose birthday do you want to look up? use name and surname in lowercase letters: ")

if person in birthday_dictionary.keys():
    print(f"{person}'s birthday is {birthday_dictionary[person]}")
else:
    print("Person not found on birthdays dictionary")

add_person_choice = input("Do you want to add an entry to the birthdays dictionary? y/n: ")
if add_person_choice == 'y':
    new_person = input('Enter person name and surname: ')
    new_person_birthday = input('Enter their birthday date: ')
    birthday_dictionary[new_person] = new_person_birthday
    with open('./Esercizi/birthdate data/birthdate_dictionary.json', 'w') as json_file:
        json.dump(birthday_dictionary, json_file)
    print('Person added successfully')