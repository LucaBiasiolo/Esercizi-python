numbers_list = [i for i in range(10)]

doubled_list = list(map(lambda x: x*2, numbers_list)) #doubles elements of the list using map()
print(doubled_list)

even_numbers_list = list(filter(lambda x: x%2 == 0, numbers_list)) #filters only the even numbers of the list
print(even_numbers_list)

print(sorted(numbers_list, key=lambda x: -x)) #sorts numbers from highest to lowest using lambda function

print(list(map(lambda x: str(x), numbers_list))) #maps str() on the elements of the list