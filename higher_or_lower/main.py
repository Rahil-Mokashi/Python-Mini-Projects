import logo
import data 
import random 

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def final_score(no):
    print(f"Sorry, that's wrong. Final score: {no}")

def play_game():
    clear_screen()
    print(logo.main_logo)

    playing = True
    count = 0

    random_acc_1 = random.choice(data.data)

    while playing == True:
        
        
        random_acc_2 = random.choice(data.data)

        while random_acc_2 == random_acc_1:
            random_acc_2 = random.choice(data.data)
                                                                                
        person_1 = random_acc_1["name"] + " - " + random_acc_1["profession"] + " - " + random_acc_1["country"]
        
        person_2 = random_acc_2["name"] + " - " + random_acc_2["profession"] + " - " + random_acc_2["country"]


        print(f'Compare A: {person_1}')

        print(logo.vs_logo)

        print(f'Against B: {person_2}')


        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        if choice not in ['A', 'B']:
            print("Invalid entry. Please type 'A' or 'B'.")
            continue

        a_followers = random_acc_1["followers_m"]
        b_followers = random_acc_2["followers_m"]

        if (choice == 'A'and a_followers >= b_followers) or (choice == 'B'and b_followers >= a_followers):
            clear_screen()
            count = count + 1
            print(f"That's Right! Current Score: {count}")
            print(f"\n{random_acc_1["name"]} has {a_followers} Million followers!\n\n{random_acc_2["name"]} has {b_followers} Million followers!\n\n")
            random_acc_1 = random_acc_2   
        else:
            clear_screen()
            final_score(count)
            playing = False
        
while True:
    play_game()

    replay = input("Do you want to play again? Type 'Y' or 'N': ").upper()

    if replay != 'Y':
        print("Thank you for playing...")
        break