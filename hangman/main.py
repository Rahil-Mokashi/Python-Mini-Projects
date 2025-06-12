import random

from wordlist import words

from stages import stages




print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     ''')

lives = 6


chosen_word = random.choice(words)


placeholder = ""

for letter in chosen_word:
    placeholder = placeholder + '_'

print("Word to guess : " + placeholder)




gameover = False

correct_letters = []

while not gameover:
    
    
    
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()


    if guess in correct_letters:
        print(f"You have already guessed {guess}")

  
    display = ""  

    for letter in chosen_word: #eat
        if letter == guess:
            display = display + guess
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'
        

    print("Word to guess: " + display)

    if guess not in chosen_word:
      lives -= 1
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      if lives == 0:
          gameover = True
          print(f"****************************IT WAS {chosen_word}! YOU LOSE****************************")
          break
          

    if "_" not in display:
        gameover = True
        print(f"****************************YOU HAVE GUESSED {chosen_word}, YOU WIN****************************")
        break
    print(stages[lives-1])

        
    
        

    
    

    
        

    
    





