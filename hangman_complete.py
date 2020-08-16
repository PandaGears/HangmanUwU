import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_comp = "_" * len(word)
    guessed = False
    guessed_let = []
    guessed_word = []
    tries = 6
    print("\033[1;35;40m" + display_hangman(tries) + "\033[0;37;40m")
    print("\n")
    while not guessed and tries > 0:
            print("\033[1;35;40m LETTEWS U GUESSED OwO: \033[1;36;40m " + str(guessed_let)[1: -1] + "\033[0;37;40m")
            guess = input("Pweez gess teh lettew: \033[0;37;40m").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_let:
                    print('\x1bc')
                    print("\033[1;31;40m    But... u sed that lettew aweddy OwO \033[0;37;40m")    
                    tries -= 1
                elif guess not in word:
                    print('\x1bc')
                    print("\033[1;31;40m    Oh noooooes >w< \033[0;37;40m")    
                    tries -= 1
                    guessed_let.append(guess)
                else:
                    print('\x1bc')
                    print("\033[1;32;40m    YAAAAAY OwO \033[0;37;40m")    
                    guessed_let.append(guess)
                    word_as_list = list(word_comp)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_comp = "".join(word_as_list)
                    if "_" not in word_comp:
                        guessed = True
            elif len(guess) > 1 and guess.isalpha():
                if guess in guessed_word:
                    print('\x1bc')    
                    print("\033[1;31;40m    But... u sed that lettew aweddy OwO \033[0;37;40m")
                elif guess != word:
                    print('\x1bc')
                    print("\033[1;31;40m    Oh noes, that wasn't it T_T \033[0;37;40m")
                    tries -= 1
                    guessed_let.append(guess)
                else:
                    guessed = True
                    word_comp = word     
            else:
                print('\x1bc')    
                print("\033[1;31;40m    Siwwy Wiwwy, this wuz a wong word OwO \033[0;37;40m")
            print("\033[1;35;40m" + display_hangman(tries) + "\033[0;37;40m")
            print(word_comp)
            print("\n")
    if guessed:
        print("\033[1;32;40m    YAAAAAAY!!!! HUGGI WUGGIES UwU \033[0;37;40m")
    else:
        print("\033[1;31;40m    Nooooooooes the word wuz '" + word + "' ... Oh noes.. \033[0;37;40m")  



def display_hangman(tries):
    stages = ["""
    
                ----------     ______________             
                |/       |     | GAYME OVER |            
                |     _( UwU)  |____________|^ ^
                |     |  |  |          |____(OwO )
                | \\o/ ___|___ \\o/ \\o/\\o/      |\\ o \\o/ \\o/
                |\\o/  |     | \\o/\\o/\\o/       | \\  o \\o/
                |   \\o/  \\o/  \\o/ \\o/\\o/\\o/   |     o \\o/
                | \\o/\\o/\\o/\\o/\\o/\\o/\\o/\\o/   / \\ o \\o/\\o/
                |\__________________________/___\\_______|
                """,
                """
    
                ----------                   
                |/       |                  
                |     _( OwO)                ^ ^
                |     |  |  |               (OwO )
                |   o ___|                   /|\\ o    o
                |  o  |         o  o   o    / | \\  o
                |     o   o   o   o   o    o  |      o
                |   o   o   o   o   o   o    / \\  o   o
                |\__________________________/___\\_______|
                """,
                """
    
                ----------                   
                |/       |                  
                |     _( OwO)                ^ ^
                |     |  |  |               (OwO )
                |        |                   /|\\ 
                |                           / | \\
                |                             |
                |   o   o    o     o     o   / \\   o   o
                |\__________________________/___\\_______'
                """,
                """
    
                ----------                   
                |/       |                  
                |     _( OwO)                ^ ^ 
                |     |  |                  (OwO )
                |        |                   /|\\
                |                           / | \\
                |                             |
                |  o    o    o      o        / \\
                |\__________________________/___\\_______'
                """,
                """
    
                ----------                   
                |/       |                  
                |      ( OwO)                ^ ^
                |        |                  (OwO )
                |        |                   /|\\
                |                           / | \\
                |                             |
                |   o   o    o               / \\
                |\__________________________/___\\_______'
                """,
                """
    
                ----------                   
                |/       |                  
                |      ( OwO)                ^ ^
                |                           (OwO )
                |                            /|\\ 
                |                           / | \\
                |                             |
                |   o                        / \\
                |\__________________________/___\\_______'
                """,
                """
    
                ----------                   
                |/       |                  
                |        O                   ^ ^
                |                           (OwO )
                |                            /|\\ 
                |                           / | \\
                |                             |
                |                            / \\
                |\__________________________/___\\_______'
                """
    ]
    return stages[tries]


def main():
    while input("\033[1;32;40m  HEWWO, WANNA PWAY?  (Y/N)  UwU      \033[0;37;40m").upper() == "Y":
        word = get_word()
        play(word)
        while input("\033[1;36;40m  THAT WAS FUN OwO! WANNA GO TO MENOO?  (Y/N)      \033[0;37;40m").upper() == "N":
            word = get_word()
            play(word)
    print('\x1bc')
    print("\033[1;34;40m\n  BYE BYE, I HOPE TOO SNUGGWE U AGAIN~ OwO \033[0;37;40m")

if __name__ == "__main__":
    main()