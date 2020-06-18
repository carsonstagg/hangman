#This program will play hangman and genererate a random word

from hangmanWords import *
from random import randint

def main():
    words = getwords()
    word = words[randint(0,2241)]
    


def play(word):
   wordCompletion = "_" * len(word)
   guessed = False
   guessedLetters = []
   guessedWords = []
   tries = 6
   print("Let's play hangman!")
   print(display_hangman(tries))
   print(wordCompletion)
   print("\n")
   while not guessed and tries > 0:
       guess = input("Please guess a letter or word: ")
       if len(guess) ==1 and guess.isalpha
            if guess in guessedLetters:
                print("You already guessed the letter")
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessedLetters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessedLetters.append(guess)
                wordAsList = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                wordCompletion = "".join(wordAsList)
                if "_" not in wordCompletion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print("You already guessed the word", guess)
                elif guess != word:
                    print(guess, "is not the word.")
                    tries -= 1
                    guessedWords.append(guess)
                else:
                    guessed = True
                    wordCompletion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(wordCompletion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word!")
    else:
        print("Sorry, you ran out of tires. The word was " + word, ", better luck next time!")




