import random

list_of_random_numbers = random.choices(range(100),k=20)

print(list_of_random_numbers)

print(list_of_random_numbers[0]) #first element of the list
print(list_of_random_numbers[-1]) #last element of the list
print(list_of_random_numbers[0:3]) #first three elements (element of index 3 not included)
print(list_of_random_numbers[:3]) #first three elements
print(list_of_random_numbers[:-1]) #all elements except last
print(list_of_random_numbers[5:10]) #elements from index 5 to index 10 (10 not included)
print(list_of_random_numbers[:]) #all elements
print(list_of_random_numbers[::2]) #first, third, fifth, seventh...
