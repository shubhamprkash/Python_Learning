# FIzzBuzz
# print from 1 to 100
# for number divisible by 3 == print fizz
# for number divisible by 5 == print buzz
# if divisible by both === print fizzBuzz

for n in range(1,100 +1):
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%5==0:
        print("Buzz")
    elif n%3==0:
        print("Fizz")
    else:
        print(n)
