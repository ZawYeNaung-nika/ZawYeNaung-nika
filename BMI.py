height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round((weight/height**2),2)
if bmi < 18.5:
    print(f"Your BMI is {bmi} and underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi} and normalweight")
elif 25 < bmi < 30:
    print(f"Your BMI is {bmi} and overweight")
elif 30 < bmi < 35:
    print(f"Your BMI is {bmi} and obese")
elif bmi > 35:
    print(f"Your BMI is {bmi} and clinical obese")