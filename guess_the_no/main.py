import random


logo = r'''
 ________ ____ ______________ _________ _______ __ ______________ ____________ __  _______   ____ ___  _____ _______________________________ 
 /  _____/|    |   \_   _____//   _____//   _____/  \__    ___/   |   \_   _____/   \      \ |    |   \/     \\______   \_   _____/\______   \
/   \  ___|    |   /|    __)_ \_____  \ \_____  \     |    | /    ~    \    __)_    /   |   \|    |   /  \ /  \|    |  _/|    __)_  |       _/
\    \_\  \    |  / |        \/        \/        \    |    | \    Y    /        \  /    |    \    |  /    Y    \    |   \|        \ |    |   \
 \______  /______/ /_______  /_______  /_______  /    |____|  \___|_  /_______  /  \____|__  /______/\____|__  /______  /_______  / |____|_  /
        \/                 \/        \/        \/                  \/        \/          \/                \/       \/        \/         \/ 

'''


comp_no = random.randint(1,100)


def easy_level(comp_no):
    attempt_counter = 10
    while attempt_counter >= 1:
        print(f"You have {attempt_counter} attempts remaining to guess the number.")
        guess_no = int(input("Make a guess: "))
        if guess_no > comp_no:
            attempt_counter = attempt_counter - 1
            print("Too High!\nGuess Again.")
        elif guess_no < comp_no:
            attempt_counter = attempt_counter - 1
            print("Too low!\nGuess Again.")
        else:
            print(f"You got it! The answer was {comp_no}.")
            return 
    print("You've run out of guesses. Restart the page to run again.")

def hard_level(comp_no):
    attempt_counter = 5
    while attempt_counter >= 1: 
        print(f"You have {attempt_counter} attempts remaining to guess the number.")
        guess_no = int(input("Make a guess: "))
        if guess_no > comp_no:
            attempt_counter = attempt_counter - 1
            print("Too High!\nGuess Again.")
        elif guess_no < comp_no:
            attempt_counter = attempt_counter - 1
            print("Too low!\nGuess Again.")
        else:
            print(f"You got it! The answer was {comp_no}.")
            return 
    print("You've run out of guesses. Restart the page to run again.") 
      



print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level == 'easy':
    easy_level(comp_no)
elif level == 'hard':
    hard_level(comp_no)
else:
    print("Incorrect Prompt!")
    

