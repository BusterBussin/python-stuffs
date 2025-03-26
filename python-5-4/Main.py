import math

def currentSpeed(target, rate, minutes):
    return math.pow((target) / (1 + rate), minutes)

target = float(input("Enter target speed: "))
rate = float(input("Rate of speed increase per minute: "))
minutes = float(input("Minutes until target speed achieved: "))
current = currentSpeed(target, rate, minutes)
print(f"Current speed: {current:,.2f}")