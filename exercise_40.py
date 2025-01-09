import random

number = random.randint(1, 9)
number_of_guesses = 0
while True:
    try:
        guess = int(input("Guess a number between 1 and 9: "))
        if guess > 9 or guess < 1:
            print("Please insert a integer number between 1 and 9")
            continue
        number_of_guesses += 1
        if guess == number:
            break
    except ValueError:
        print("Please enter an integer number between 1 and 9")
print(f"You needed {number_of_guesses} guesses to guess the number {number}")