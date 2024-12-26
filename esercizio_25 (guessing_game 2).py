print("""Hi, i'm Python. Choose a number between 0 and 100 and i will try to guess it.
       Just tell me if my guesses are too high, too low or exactly the number you're thinking of""")

number_of_guesses = 0
start_interval = 0
end_interval = 100
while True:
    
    half_interval = (end_interval + start_interval)//2

    user_answer = input(f"Is it {half_interval}? h/l/e: ")
    number_of_guesses +=1

    if user_answer == "h":
        end_interval = half_interval
    elif user_answer == 'l':
        start_interval = half_interval
    else:
        print(f"I guessed correctly! It took me {str(number_of_guesses) } guesses to guess your number.")
        break