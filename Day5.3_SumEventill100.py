# YOu are going to write a priogram that calculates the 
# sum of the all the even numbers from 1 to 100, including 1 and 100.

evenTotal=0;
for n in range(1 ,100+1):
    if n%2==0:
        evenTotal += n;

print(evenTotal)


# another method

newEvanTotal=0;
for n in range(0, 101, 2):
    newEvanTotal += n;

print(newEvanTotal)
