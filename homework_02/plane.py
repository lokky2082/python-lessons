"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
class Plane(Vehicle):
    cargo=0
    def __init__(self, weight=100, fuel=200, fuel_consumption=5, max_cargo=8):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.init_cargo = self.cargo
    def load_cargo(self, num):
         summary = self.cargo + num
         if summary > self.max_cargo:
            raise CargoOverload()
         else:
            self.cargo = summary
    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo


                 