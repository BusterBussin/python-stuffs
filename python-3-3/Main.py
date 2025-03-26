tasks = int(input("How many tasks did the astronaut complete?: "))
percentage = 0
if tasks == 0:
    percentage = 0
if tasks == 1:
    percentage = 10
if tasks == 2:
    percentage = 25
if tasks == 3:
    percentage = 45
if tasks == 4:
    percentage = 70
if tasks == 5:
    percentage = 100
print("The astronaut's score is", percentage, "percent.")
SystemExit