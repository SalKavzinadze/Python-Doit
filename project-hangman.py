import random

def hangman():
    # სიტყვების სია
    words = ["python", "hangman", "programming", "computer", "apple"]
    
    # შემთხვევითი სიტყვა
    word = random.choice(words)
    guessed_letters = []
    tries = 6  # შეცდომების მაქსიმალური რაოდენობა

    print("Welcome to Hangman!")
    
    while tries > 0:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print("\nWord:", display_word)
        
        # თუ ყველა ასო დართულია
        if "_" not in display_word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            tries -= 1
            print("Tries left:", tries)
    
    else:
        print("Game Over! The word was:", word)

# თამაშის გაშვება
hangman()