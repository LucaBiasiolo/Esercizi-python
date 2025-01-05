from esercizio_30 import get_random_word

print("Hi, i'm Python. Welcome to hangman game")

wants_to_play_again = 'y'
while wants_to_play_again == 'y':
    word_to_guess = get_random_word().lower()

    unknown_word = "_"*len(word_to_guess)

    print(f"The word you have to guess is made of {len(word_to_guess)} characters")
    print(f"{unknown_word}")

    guessed = False
    tried_letters_list = []
    remained_guesses = 6

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
            remained_guesses -=1
            print(f"Letter not found. You have {remained_guesses} guesses left")
            print(f"{unknown_word}")
        
        if remained_guesses == 0:
            print(f"You lost. That's a pity!. The word was {word_to_guess}")
            break

        if unknown_word == word_to_guess:
            print(f"You won! You guessed the word {word_to_guess}")
            guessed = True

    wants_to_play_again = input("Do you wish to play again? y/n: ")
    if wants_to_play_again == 'n':
        break

#TODO: show hangman graphics instead of written sentence