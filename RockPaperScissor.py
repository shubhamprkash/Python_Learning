import random as denny

rock = "\n Rock!! \n"

paper = "\n Paper!! \n"

scissors = "\n Scissor!! \n"

choice = int(input("\nWhat do you choose?\n Type 0 for Rock,\n      1 for Paper or\n      2 for Scissors.\n"))
bot_choice = denny.randint(0, 2)
arr = [rock, paper, scissors]

if choice > 2:
    print("Invalid Choice!")
else:
    print(arr[choice])
    print("Computer chose:")
    print(arr[bot_choice])

    if (choice == 0 and bot_choice == 2) or (choice == 2 and bot_choice == 1) or (choice == 1 and bot_choice == 0):
        print("###   You won!   ###\n")
    elif choice == bot_choice:
        print("###   It's a tie!   ###\n")
    else:
        print("###   You lose!    ###\n")

        #Crafted By @Shubham prakash
        #All Copyrights Reserved By Shubham Prakash