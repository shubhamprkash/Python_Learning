height=int(input("Whats your height?  "))
age=int(input("Whats your age?  "))

if height>=120:
    print("Your Height is eligible to ride!! :D ")
    if age>=18 :
        print("You need to pay: $12")
    elif age<12:
        print("You nedd to pay: $5 ")
    else:
        print("You nedd to pay: $7")
   
else:
    print("Your height is not Eligible for the Ride! :( ")