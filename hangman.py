hangman0 = """"   
      _______
     |/      |
     |       
     |      
     |      
     |      
     |
 ____|___"""

hangman1 = """    
      _______
     |/      |
     |      (_)
     |       
     |       
     |      
     |
 ____|___"""

hangman2 = """
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
 ____|___"""

hangman3 = """
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |       
     |
 ____|___"""

hangman4 = """"
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|___"""

hangman5 = """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|___"""

hangman6 = """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 ____|___"""

hangman = [hangman6, hangman5, hangman4, hangman3, hangman2, hangman1, hangman0]

import random
word_list = [
    "airplane", "backpack", "bicycle", "bottle", "calendar", "camera", "carpet",
    "chair", "couch", "desk", "glasses", "helmet", "jacket", "keyboard", "lamp",
    "laptop", "magnet", "mirror", "notebook", "pillow", "puzzle", "radio",
    "refrigerator", "scissors", "shampoo", "socks", "suitcase", "television",
    "toaster", "umbrella", "vacuum", "wallet", "watch", "window", "xylophone",
    "yarn", "zebra", "box", "calculator", "camera", "drum", "envelope", "fork",
    "glove", "hats", "lawnmower", "luggage", "mug", "phone", "printer", "rug",
    "screwdriver", "skateboard", "stereo", "suit", "toothbrush", "trampoline",
    "umbrella", "vase", "wrench", "zipper"
]

def main_game():
    chosen_word = random.choice(word_list)
    display = []
    underscore = "_"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    life = 6
    guessed_letters = ""

#    Generera blanka
    for letters in chosen_word:
        display.append("_")

    print(display)

    # Primär loop
    while underscore in display:
        # Gissning
        guess = input("Guess a letter: ").lower()
        print(guess)

        # Gör så att man bara kan gissa på bokstäver och endast en i taget
        if len(guess) > 1 or guess not in alphabet:
            print("Guess again! You can only guess one LETTER at the time")
            continue

        # Har du redan gissat på denna bokstav?
        if guess in guessed_letters:
            print("You already guessed that, guess again")
            continue

        # Lägg till gissningen i gissade bokstäver
        if guess not in guessed_letters:
            guessed_letters += guess

        # Kontrollera om gissningen finns i ordet och byt ut korrekt _ om det finns
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Förlora ett liv om gissningen inte finns med i ordet   
        if guess not in chosen_word:
            life -= 1
            print(f"Incorrent, you have {life} guesses left")
            print(hangman[life])
    
        # Förlora spelet om liven tar slut
        if life == 0:
            print("You lose!")
            print(f"The word was: {chosen_word}")
            again = input("Would you like to play again? Y/N Yes/No: ").lower()
            if again == "y" or again == "yes":
                main_game()
            elif again == "n" or again == "no":
                print("Thanks for playing!")
                exit()
            else:
                print("Invalid response")
                continue

        print(display)
        print(f"Guessed letters: {guessed_letters}")

    print("You won!")
    again = input("Would you like to play again? Y/N Yes/No: ").lower()
    if again == "y" or again == "yes":
        main_game()
    elif again == "n" or again == "no":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid response")
        again = input("Would you like to play again? Y/N Yes/No: ").lower()
        if again == "y" or again == "yes":
            main_game()
        elif again == "n" or again == "no":
            print("Thanks for playing!")
            exit()


main_game()
