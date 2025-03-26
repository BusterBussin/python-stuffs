from LZBuilder import LZBuilder
radius = float(input("Enter the radius of the landing zone: "))
lz = LZBuilder(radius)
print(f"The landing zone's area is {lz.getArea():,.2f}")
print(f"The landing zone's diameter is {lz.getDiameter():,.2f}")
print(f"The landing zone's circumference is {lz.getCircumference():,.2f}")