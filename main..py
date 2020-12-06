#import required modules
from replit import clear
import random
import hangman_words
import hangman_art

#randomly choose word from hangman_words.py list
chosen_word = random.choice(hangman_words.word_list)
#get length of word
word_length = len(chosen_word)

#create statuses for initial game play
end_of_game = False
lives = 6

#Import the logo from hangman_art.py 
print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks to show users how many letters in the randomly chosen word
display = []
for _ in range(word_length):
    display += "_"

#Create a list to keep track of what letters (right or wrong) have already been guessed.
letters_guessed = []

#game play
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in letters_guessed:
        print(f"You already guessed {guess}. Please try again.") 
    #Check if guessed letter is in the word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            letters_guessed.append(letter)

    #Check if user is wrong.
    if guess not in chosen_word:
        if guess in letters_guessed:
            None
        else:
            letters_guessed.append(guess)
            print(f"You guessed {guess}. It's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                 end_of_game = True
                 print("You lose.The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Import the stages from hangman_art.py and print at each stage of the game
    print(hangman_art.stages[lives])
