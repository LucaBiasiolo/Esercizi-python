from Esercizi.hangman.esercizio_30 import get_random_word

print("Hi, i'm Python. Welcome to hangman game")

word_to_guess = get_random_word().lower()

unknown_word = "_"*len(word_to_guess)

print(f"The word you have to guess is made of {len(word_to_guess)} characters")
print(f"{unknown_word}")

guessed = False
tried_letters_list = []
while not guessed:
    letter = input("Choose a letter: ")

    if letter in tried_letters_list:
        print("Letter already guessed")
    elif letter in word_to_guess:
        tried_letters_list.append(letter)

        for i in range(len(word_to_guess)):
            word_to_guess_list = list(word_to_guess)
            if word_to_guess_list[i] == letter:
                unknown_word_list = list(unknown_word)
                unknown_word_list[i] = letter
                unknown_word = "".join(unknown_word_list)

        print(f"{unknown_word}")
    else:
        print("Letter not found")
    
    if unknown_word == word_to_guess:
        print(f"You guessed the word {word_to_guess}. Bye!")
        guessed = True