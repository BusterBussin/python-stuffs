from SpaceCargo import SpaceCargo
def menu():
    print("Menu:")
    print("1. Calculate Shipping Cost")
    print("2. Display cargo details")
    print("3. Exit")
print("Welcome to the Cargo Management System!")
cargoName = input("Enter cargo name: ")
cargoWeight = float(input("Enter the weight of cargo in tons: "))
cargoDestination = input("Enter the destination planet or moon: ")
cargo = SpaceCargo(cargoName, cargoWeight, cargoDestination)
choice = 0
while choice != 3:
    menu()
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            shippingCost = cargo.calculateShippingCost()
            print(f"Shipping Cost: ${shippingCost:,.2f}")
        case 2:
            cargo.details()
        case 3:
            print("Thank you.")
        case _:
            print("invalid choice.")
SystemExit
