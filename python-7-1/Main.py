from Payroll import Payroll
pr = Payroll()
for i in range(7):
    hours = int(input("Enter the numbers worked by astronaut number " + str(pr.getAstronautIDAt(i)) + ": "))
    while hours < 0:
        hours = int(input("ERROR: Enter 0 or greater for hours: "))
    payRate = float(input("Enter the hourly pay rate for astronaut number " + str(pr.getAstronautIDAt(i)) + ": "))
    while payRate < 15:
        payRate = float(input("ERROR: Enter 15.00 or greater: "))
    pr.setPayRate(i, payRate)
    pr.setHoursAt(i, hours)
    i += 1
print("PAYROLL DATA")
print("============")
for int in range(7):
    print("Astronaut ID: " + str(pr.getAstronautIDAt(i)) + ": ")
    print(f"Gross pay: ${pr.getGrossPay(i):,.2f}")
    i += 1
SystemExit