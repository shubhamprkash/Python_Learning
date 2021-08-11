
import random

# step 1

wordbank=["hello","welcome","bye"]

#1. randomly choose a word from thr word_list and assign it to a variable called actualword.

actualword=random.choice(wordbank)
print(actualword)


#2. ask the user input and assign to a variable. make it lowercase.

guessedWord=input("Think a letter: ").lower()
print(guessedWord)

#3. chech if the user guessed the ryt or not and repeat.

for letter in actualword:
    if letter==guessedWord:
        print("good")
    else:
        print("bad")