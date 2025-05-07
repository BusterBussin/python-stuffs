from SpaceMission import SpaceMission

missionName = "Planet Explorer"
model = "Astroprobe"
array = True
comms = True
astroProbeMission = SpaceMission(missionName, model, array, comms)
copy = SpaceMission(astroProbeMission)
print("AstroProbe Mission Details:")
print("Mission Name: " + astroProbeMission.getName())
print("Spacecraft Model: " + astroProbeMission.getModel())
print("Advanced Sensor Array: " + astroProbeMission.getArray())
print("Enhanced Communication System: " + astroProbeMission.getComms())
print("\nCosmic Voyager Mission Details: " )
print("Mission Name: " + astroProbeMission.getName())
print("Spacecraft Model: " + astroProbeMission.getModel())
print("Advanced Sensor Array: " + astroProbeMission.getArray())
print("Enhanced Communication System: " + astroProbeMission.getComms())