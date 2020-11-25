class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.remaining = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.remaining[carType - 1] > 0:
            self.remaining[carType - 1] -= 1
            return True
        return False
