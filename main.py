from random import *

word_list = ['bleu', 'rouge', 'vert', 'jaune', 'noir', 'rose', 'magenta', 'cyon']

chosen_word = choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 7

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word! You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost!")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives - 1])