speed = float(.1)
totalspeed = float(0)
maxSeconds = 0
maxSeconds = int(input("How many seconds is the burn?: "))
while maxSeconds <= 0:
    print("The number of seconds must atleast")
    maxseconds = int(input("How many seconds is the burn?"))
print("Seconds \tTotal Speed")
for i in range(maxSeconds):
    print(i, "\t\t", speed, "km/s")
    speed = speed * 2
totalspeed = speed/2
print("Final speed:\t", totalspeed, "km/s")
SystemExit