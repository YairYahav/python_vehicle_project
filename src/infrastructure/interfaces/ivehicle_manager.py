from abc import ABC, abstractmethod


class IVehicleManager(ABC):

    @abstractmethod
    def create_vehicle(self, vehicle_type: str):
        pass

    @abstractmethod
    def start_all(self):
        pass

