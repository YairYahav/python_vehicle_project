from abc import ABC, abstractmethod

class Vehicle(ABC):

    type_of_vehicle: str = ""

    def __init__(self, type_of_vehicle: str):
        self.type_of_vehicle = type_of_vehicle

    @abstractmethod
    def start_engine(self):
        pass