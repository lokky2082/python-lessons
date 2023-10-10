"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine
class Car(Vehicle):
    def __init__(self, started=False, weight=100, fuel=200, fuel_consumption=5, engine=None):
        super().__init__(started, weight, fuel, fuel_consumption)
        self.engine = engine
    def set_engine(self, engine):
        self.engine = engine
