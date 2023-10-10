from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, started=False, weight=100, fuel=200, fuel_consumption=5):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started
    def start(self):
        if self.started == False:
            if (self.fuel > 0) & (self.fuel > self.fuel_consumption):
                self.started = True
            else:
                raise LowFuelError('low fuel')
    def move(self, distance):
        fuel_waisted = distance * self.fuel_consumption
        if fuel_waisted > self.fuel:
            raise NotEnoughFuel('not enought fuel')
        else:
            self.fuel = self.fuel - fuel_waisted

        
        
        
        
        
        


