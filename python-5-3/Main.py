def calcKilometers(meters):
    return meters * 0.001
def calcInches(meters):
    return meters * 39.97
def calcFeet(meters):
    return meters * 3.281
def menu():
    print("1. Convert to kilometers")
    print("2. Convert to inches")
    print("3. Convert to feet")
    print("4. Quit")
choice = 0
meters = float(input("Enter a distance in meters: "))
while choice != 4:
    menu()
    choice = int(input("Enter your choice: "))
    if choice < 1 or choice > 4:
        print("Invalid choice.")
    if choice == 1:
        print(meters, "meters is", calcKilometers(meters), "kilometers.")
    if choice == 2:
        print(meters, "meters is", calcInches(meters), "inches")
    if choice == 3:
        print(meters, "meters is", calcFeet(meters), "feet")
    if choice == 4:
        print("Have a good day.")
SystemExit