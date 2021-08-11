
stuScore=input("input the scores: ")
# newscoe=0;
for n in range(0, len(stuScore)):
    stuScore[n]=int(stuScore[n])

# 78 65 89 55 91 64 89

print(stuScore)

# fast method to get highest scroe of all 
# -->  print(max(stuScore))
# fast method to get lowest scroe of all
# --> print(min(stuScore))


highest=0;

for n in stuScore:
    if n > highest:
        highest=n;
print(f"Highest score is : {highest}")
