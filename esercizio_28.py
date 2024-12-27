first_number = input("Insert first number: ")
second_number = input("Insert second number: ")
third_number = input("Insert third number: ")

if first_number >= second_number and first_number >= third_number:
    print(f"The biggest number is {first_number}")
elif second_number >= first_number and second_number >= third_number:
    print(f"The biggest number is {second_number}")
else:
    print(f"The biggest number is {third_number}")