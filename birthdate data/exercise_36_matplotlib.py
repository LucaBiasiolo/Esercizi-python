from collections import Counter
import json
import matplotlib.pyplot as plt

with open('./Esercizi/birthdate data/birthdate_dictionary.json') as birthdate_dictionary_file:
    birthday_dictionary = json.load(birthdate_dictionary_file)

months_dictionary = {1: 'January', 2: 'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10: 'October', 11: 'November', 12: 'December'}

months_list = []
for person in birthday_dictionary:
    person_birthday: str = birthday_dictionary[person]
    birthday_month_number = int(person_birthday.split("/")[1])
    month_name = months_dictionary[birthday_month_number]
    months_list.append(month_name)

months_counter = Counter(months_list)

print(months_counter)

months_names = list(months_dictionary.values())
months_counts = [ months_counter[month] for month in months_dictionary.values()]

print(months_names)
print(months_counts)

plt.bar(months_names, months_counts)
plt.xlabel("Month of birth")
plt.ylabel("Number of persons born")
plt.title("Number of persons per month of birth")
plt.show() 