

print("Welcome to Treasure Hunt!!")
one =["😶","😶","😶"]
two =["😶","😶","😶"]
three =["😶","😶","😶"]

map = [one,two,three]

print(f"{one}\n{two}\n{three}\n")
destination=input("enter ur coordinates to enter : ")

hor=int(destination[0])
ver=int(destination[1])

selection=map[hor -1][ver-1]="🙋";
print(f"{one}\n{two}\n{three}\n")