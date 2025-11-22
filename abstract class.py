from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
        def start_engine(self):
            print("car engine started")

car=ABC()
car.start_engine()
