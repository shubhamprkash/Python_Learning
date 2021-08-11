stuHeight=input("Enter the Height of student:  ").split();
for n in range(0, len(stuHeight)):
    stuHeight[n]=int(stuHeight[n]);

print(stuHeight)


length = 0;
totalHeight=0;
for n in stuHeight:
    totalHeight += n;
    length = length +1;

print(totalHeight)
avg= totalHeight/length
print(f"the avg of class is {round(avg)}")