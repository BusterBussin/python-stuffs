class SpaceCargo:
    cargoName = " "
    cargoWeight = float(0)
    cargoDestination = " "
    def __init__(self, cargoName=None, cargoWeight=None, cargoDestination=None):
        self.cargoName = cargoName
        self.cargoWeight = cargoWeight
        self.cargoDestination = cargoDestination
    def calculateShippingCost(self):
        return self.cargoWeight * 1000
    def details(self):
        print("Cargo name:", self.cargoName, ", Weight:", self.cargoWeight, "tons, Destination:", self.cargoDestination)