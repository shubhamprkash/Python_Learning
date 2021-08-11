#IF the bill was $150, split between 5 people, with 12% tip.
# Each person should pay (150/5)*1.12= 33.6
# Round the result to 2 decimal places =33.60

print("Welcome To split And Tip Calculator! ");
bill=float(input("What was the total bill ?   "));
tax=float(input("What percentage tip would you like to give ?\n Like 10, 12, or 15 ? " ));
ppl=float(input("How many people to split the bill ? "));

total=(bill*(1+tax/100))/ppl;
print(f"Each person should pay: {round(total,2)} ");

