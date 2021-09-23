import random
import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls') # for windows
    else:
        _ = os.system('clear') # for mac and linux(here, os.name is 'posix')
def game_init():
    #os.system('clear')
    clear()
    with open('words_alpha.txt', 'r') as fh:
        words = [line[:-1] for line in fh]
    life=5
    word = random.choice(words).upper()
    guessed_word = list('_'*len(word))
    screen(guessed_word,life)
    character(word,life,guessed_word)




def character(word,life,guessed_word):
    #print(word)
    letter = input('\n Escribe una letra: ')
    if len(letter) != 1 or not(letter.isalpha()):
        print('\n **********************')
        print('Escribe correctamente UNA SOLA LETRA \n')
        return character(word,life,guessed_word)
    else:
        letter = letter.upper()
        return Ahorcado(letter,word,life,guessed_word)
        
def Ahorcado (letter,word,life,guessed_word):
    if letter in word:
        for i,char in enumerate(word):
            if letter == char:
                guessed_word[i]=letter
                clear()
                if "".join(guessed_word) == word:
                    print("YOU WIN")
                    print("""
                    \\o/
                     |
                    / \\
                    """)
                    if input('Do you wanna play again?\n Press Y\n').upper()=='Y':
                        game_init()
                    else:
                        exit
                
        screen(guessed_word,life)
        character(word,life,guessed_word)
        #continue
    else:    
        life -= 1
        clear()
        if life == 0:
            screen(guessed_word,life)
            print("""
            ************************
            *                      *
            *       GAME OVER      *
            *                      *
            ************************   
            """)
            print('\n The word was {}\n'.format(word))
            if input('Do you wanna play again?\n Press Y\n').upper()=='Y':
                game_init()
            else:
                exit
            
                
        else:
            screen(guessed_word,life)
            character(word,life,guessed_word)

def screen(guessed_word,life):
    
    dibujo=[
    """+------+
   |  o.
   |  /|\\
   |  / \\
___|___""",
    """+------+
   |  
   |  /|\\
   |  / \\
___|___""",
    """+------+
   |  
   |  /|
   |  / \\
___|___""",
    """+------+
   |  
   |   
   |  / \\
___|___""",
    """+------+
   |  
   |  
   |  / 
___|___""",
    """+------+
   |  
   |  
   |  
___|___"""
    ]
    print('\n'," ".join(guessed_word),"\n")
    print(dibujo[life])
    return 

def run():
    game_init()
    
if __name__ == '__main__':
    run()

