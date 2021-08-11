year=int(input("Enter a year to check for leap year: "))

if year % 4 == 0:
    if year % 100 == 0:
        print(f"{year} is not a Leap year!")
    elif year % 400 == 0:
            print(f"{year} is a Leap year!")
        # else:
        #     print(f"{year} is not a Leap year!")
    else:
        print(f"{year} is a Leap year!")
else:
    print(f"{year} is not a Leap year!")