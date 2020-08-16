import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):

    #word display on console
    word_comp = "_" * len(word)

    #boolean for if the game is won
    guessed = False

    #list for guessed letters in the input
    guessed_let = []

    #list for guessed words in input
    guessed_word = []

    #times the input can be wrong
    tries = 6

    #displays the beautiful hangman pic
    print("\033[1;35;40m" + display_hangman(tries) + "\033[0;37;40m")
    print("\n")

    #while the game has not been won and you still have tries left
    while not guessed and tries > 0:
            print(" The word is " + str(len(word)) + " letters long OwO\n") 
            print("\033[1;35;40m LETTEWS U GUESSED OwO: \033[1;36;40m " + str(guessed_let)[1: -1] + "\033[0;37;40m")
            print("\033[1;35;40m WORDS U GUESSED OwO: \033[1;36;40m " + str(guessed_word)[1: -1] + "\033[0;37;40m")
            guess = input("Pweez gess teh lettew: \033[0;37;40m").upper()
            
            #if your guess is one letter
            if len(guess) == 1 and guess.isalpha():

                #if you guessed the letter before
                if guess in guessed_let:
                    
                    #this clears the console
                    print('\x1bc')

                    print("\033[1;31;40m    But... u sed that lettew aweddy OwO \033[0;37;40m")   
                    
                    #lose a try 
                    tries -= 1

                #else if it is just plain incorrect
                elif guess not in word:

                    print('\x1bc')
                    print("\033[1;31;40m    Oh noooooes >w< \033[0;37;40m")    
                    tries -= 1

                    #adds the letter to the list of guessed letters
                    guessed_let.append(guess)

                else:
                    print('\x1bc')
                    print("\033[1;32;40m    YAAAAAY OwO \033[0;37;40m")  
                    guessed_let.append(guess)

                    #looks where in the word was the correctly guessed letter
                    word_as_list = list(word_comp)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:

                        #replaces the appropriate '_' with the correctly guessed letter
                        word_as_list[index] = guess

                    #displays the word with '_'s and the correctly guessed letters
                    word_comp = "".join(word_as_list)

                    #if all the letters were guessed correctly
                    if "_" not in word_comp:

                        #winning conditions are met so the boolean becomes true
                        guessed = True

            #if you try to guess the full word and it is all letters
            elif len(guess) == len(word) and guess.isalpha():

                #if you guessed that word already
                if guess in guessed_word:
                    print('\x1bc')    
                    print("\033[1;31;40m    But... u sed that lettew aweddy OwO \033[0;37;40m")
                #if that is just wrong   
                elif guess != word:
                    print('\x1bc')
                    print("\033[1;31;40m    Oh noes, that wasn't it T_T \033[0;37;40m")
                    tries -= 1
                    guessed_word.append(guess)
                #if ya got the word right away
                else:
                    guessed = True
                    word_comp = word

            #if nothing ya typed was an valid 
            else:
                print('\x1bc')    
                print("\033[1;31;40m    Siwwy Wiwwy, this wuz a wong word OwO \033[0;37;40m")
            print("\033[1;35;40m" + display_hangman(tries) + "\033[0;37;40m")
            print(word_comp)
            print("\n")

    #Winning sentence OwO
    if guessed:
        print("\033[1;32;40m    YAAAAAAY!!!! HUGGI WUGGIES UwU \033[0;37;40m")

    #Losing sentence UwU
    else:
        print("\033[1;31;40m    Nooooooooes the word wuz '" + word + "' ... Oh noes.. \033[0;37;40m")  


#showing the hangman, for each try is a stage, the last being at full tries and the first being at none
def display_hangman(tries):
    stages = ["""
    
                ----------     ______________             
                |/      ^| ^   | GAYME OVER |            
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
                |/      ^| ^                 
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
                |/      ^| ^                 
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
                |/      ^| ^                
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
                |/      ^| ^                
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
                |/      ^| ^                  
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

#main function to play the game
def main():
    
    #if I say Y, do the following
    while input("\033[1;32;40m  HEWWO, WANNA PWAY?  (Y/N)  UwU      \033[0;37;40m").upper() == "Y":

        word = get_word()
        play(word)

        #after the game is over win or lose
        while input("\033[1;36;40m  THAT WAS FUN OwO! WANNA GO TO MENOO?  (Y/N)      \033[0;37;40m").upper() == "N":
            word = get_word()
            play(word)

    #if I choose to leave the game and not say Y to playing        
    print('\x1bc')
    print("\033[1;34;40m\n  BYE BYE, I HOPE TOO SNUGGWE U AGAIN~ OwO \033[0;37;40m")

if __name__ == "__main__":
    main()
