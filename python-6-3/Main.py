from SpaceCraftBuilder import SpaceCraftBuilder
def menu():
    print("Available operations: ")
    print("1) Board Crew")
    print("2) Refuel")
    print("3) Launch")
    print("4) Exit")
print("Welcome to the Spacecraft Management System")
name = input("Enter the spacecraft name: ")
crewCapacity = int(input("Enter crew capacity: "))
fuelCapacity = float(input("Enter fuel capacity (in liters): "))
boarder = SpaceCraftBuilder(name, crewCapacity, fuelCapacity)
status = False
print(name, "created successfully")
choice = int(0)
while choice != 4:
    menu()
    print(boarder.getCurrentFuel())
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            crewCount = int(input("Enter the number of crew members to board: "))
            status = boarder.boardCrew(crewCount)
            if status:
                print("Crew boarded successfully. Current crew count:", boarder.getCurrentCrew())
            else:
                print("Failed. Insufficient capacity. Current crew count:", boarder.getCurrentCrew())
        case 2:
            fuelAmount = float(input("Enter the amount of fuel to refuel (in liters): "))
            boarder.refuel(fuelAmount)
            print("Spacecraft refueled. Current fuel level:", boarder.getCurrentFuel(), "liters")
        case 3:
            destination = input("Enter the destination: ")
            boarder.launch(destination)
        case 4:
            print("Goodbye.")
        case _:
            print("Invalid choice.")
SystemExit
