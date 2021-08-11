

weight = input("Enter your weight in kgs :  ");
height = input("Enter your hight in meters :  ");


# My Code
bmi=float(weight)/(float(height)**2);

covBmi=round(bmi,2);

if covBmi < 18.5:
    print(f"Your BMI is {covBmi}, You are Underweight!");
elif covBmi >35:
    print(f"Your BMI is {covBmi}, You are clinically obese!");
elif covBmi > 18.5:
    if covBmi < 25:
        print(f"Your BMI is {covBmi}, You have Normal Weight!");
elif covBmi > 25:
    if covBmi <30:
        print(f"Your BMI is {covBmi}, You are Overweight!");
elif covBmi > 30:
    if covBmi < 35:
         print(f"Your BMI is {covBmi}, You are Obese!!");
else:
     print(f"Your BMI is {covBmi}, Invalid Entry error!!");       
