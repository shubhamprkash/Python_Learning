import random as ran;

rawNames=input("Enter few names divided by a comma and space in between them :\n")
namesList=rawNames.split(", ");

#checking the list for testing the working.
print(namesList)

numlen=len(namesList)

val=ran.randint(0,numlen-1)

print(f" \nSo out of all ppl the system chooses : {namesList[val]}\n")