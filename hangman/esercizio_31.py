import random

def get_random_word():
    with open("c:/Users/acer/Desktop/Python/Esercizi/hangman/sowpods.txt", "r") as sowpods_file:
        sowpods_word_list = sowpods_file.read().split("\n")

        random_word = random.choice(sowpods_word_list)

        return random_word