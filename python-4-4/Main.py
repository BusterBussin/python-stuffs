size = int(input("How big do you want the star field to be (1-15): "))
horizontal = 0
vertical = 0
while size <= 0 or size > 15:
    print("Sorry, that's an invalid number.")
    size = int(input("How big do you want the starfield to be? (1-15): "))
while vertical < size:
    while horizontal < size:
        horizontal += 1
        print("X", end=" ")
    print("")
    horizontal = 0
    vertical += 1
SystemExit