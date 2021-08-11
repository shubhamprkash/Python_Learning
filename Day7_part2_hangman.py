
# Step 2

#1. create empty list display
    #for each n in actualword, add "_" to display.

import random
wordbank=["hello","welcome","bye"]
actualword=random.choice(wordbank)
print(f"real word: {actualword}")

display=[]
for n in actualword:
    display += "-";
print(display)


guessedWord=input("Think a letter: ").lower()
print(f"Your Guessed woord: {guessedWord}")

#2.loop the actualword
    #if letter matche the actualword letters then replace it as reveal letter

for n in range(len(actualword)):
    letter = actualword[n]
    if letter==actualword:
        display[n]=letter;



#3.print display 

print(display)
