"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from homework_02.exceptions import CargoOverload
class Plane(Vehicle):
    def __init__(self, started=False, weight=100, fuel=200, fuel_consumption=5, cargo=0, max_cargo=8):
        super().__init__(started, weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo
        self.init_cargo = cargo
    def load_cargo(self, num):
         summary = self.cargo + num
         if summary > self.max_cargo:
            raise CargoOverload('too heavy')
         else:
            self.cargo = summary
    def remove_all_cargo(self):
        self.cargo =  self.init_cargo
                 