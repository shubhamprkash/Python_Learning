

print("Welcome to Python Pizza Delivery! ");
size=input("What size pizza do uh want? S, M or L?  ")
add_pep=input("Do uh want extra pepporoni? Y or N? ")
add_cheese=input("Do you want extra cheese? Y or N? ")

bill=0;

if size=="S" or "s":
    bill +=15;
elif size =="M" or "m":
    bill+=20;
elif size == "L" or "l":
    bill+= 25;

if add_pep=="Y" or "y":
    if size=="S" or "s":
        bill +=2;
    else:
        bill+=3;

if add_cheese=="Y" or "y":
    bill +=1 ;

print(f"Your Final Bill is : {bill}");

input("\nPress Enter to exit")
