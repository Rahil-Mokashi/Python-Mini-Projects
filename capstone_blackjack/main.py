import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = r'''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/           
'''

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]

def calculate_score(card_list):
    score = sum(card_list)
    while 11 in card_list and score > 21:
        ace_index = card_list.index(11)
        card_list[ace_index] = 1
        score = sum(card_list)
    return score

def final_prompt(user_cards, computer_cards):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if user_score == 21 and len(user_cards) == 2:
        print("BlackJack!! 😎")
    elif user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 🥳")
    elif user_score > computer_score:
        print("You win 🥳")
    elif user_score < computer_score:
        print("You lose 😭")
    else:
        print("It's a tie 🪢")


while True:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game != 'y':
        break

    clear_screen()
    print(logo)

    user_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=2)

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 21 or user_score > 21:
            game_over = True
        else:
            user_input = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_input == 'y':
                user_cards.append(random.choice(cards))
            else:
                game_over = True

    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = calculate_score(computer_cards)

    final_prompt(user_cards, computer_cards)
