print("This program will calculate an astronaut's BMI.")
weight = float(input("Enter the astronaut's weight, in pounds: "))
height = float(input("Enter the astronaut's height, in inches: "))
bmi = weight * 703/(height * height)
if bmi < 10.5:
    print("The astronat is underweight")
elif bmi > 25:
    print("The astronaut is overweight")
else:
    print("The astronaut's weight is optimal")
SystemExit