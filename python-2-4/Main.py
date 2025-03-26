LOX_RECIPE = 2.56
FUEL = float(input("How many kilograms of fuel are needed for the test?"))
LOX = FUEL * LOX_RECIPE
RP1 = LOX + FUEL
print("You need", LOX, "kilograms of oxidizer for", FUEL, "kilograms of fuel")
print("The total weight of RP-1 required is", RP1, "kilograms")