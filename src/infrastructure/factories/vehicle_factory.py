from model.data_classes.vehicle import Vehicle
from model.data_classes.car import Car
from model.data_classes.truck import Truck
from model.data_classes.motorcycle import Motorcycle



class VehicleFactory:
    @staticmethod
    def create(vehicle_type: str) -> Vehicle:
        type_of_vehicle = vehicle_type.lower()

        for v in Vehicle.__subclasses__():
            if v.__name__.lower() == type_of_vehicle:
                return v()
        
        print(f"Unknown vehicle type: {vehicle_type}")
        return None