from collections import Counter
import json

with open('./Esercizi/birthdate data/birthdate_dictionary.json') as birthdate_dictionary_file:
    birthday_dictionary = json.load(birthdate_dictionary_file)

    months_dictionary = {'01': 'January', '02': 'February', '03':'March', '04':'April', '05':'May', '06':'June', '07':'July', '08':'August', '09':'September', '10': 'October', '11': 'November', '12': 'December'}

    months_list = []
    for person in birthday_dictionary:
        person_birthday: str = birthday_dictionary[person]
        birthday_month_number = person_birthday.split("/")[1]
        month_name = months_dictionary[birthday_month_number]
        months_list.append(month_name)

    months_counter = Counter(months_list)

    print(months_counter)

