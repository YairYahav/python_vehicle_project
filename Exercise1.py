

# Abstract class
class Vehicle:
    def start_engine():
        pass


class Car(Vehicle):
    def start_engine():
        print("I'm driving in a car")


class Truck(Vehicle):
    def start_engine():
        print("I'm driving in a truck")


class Motorcycle(Vehicle): 
    def start_engine():
        print("I'm driving in a motorcycle")




# Factory class
class VehicleFactory: 
    _registered = {}

    @classmethod
    def registerVehicle(cls, vehicleType: str, vehicleClass):
        cls._registered[vehicleType] = vehicleClass

    @classmethod
    def createVehicle(cls, vehicleType: str) -> Vehicle:
        vehicleClass = cls._registered.get(vehicleType)
        if vehicleClass:
            return vehicleClass
        return "Unknoen input"
    


VehicleFactory.registerVehicle("Car", Car)
VehicleFactory.registerVehicle("Truck", Truck)
VehicleFactory.registerVehicle("Motorcycle", Motorcycle)

if __name__ == "__main__": 
    print("Testing")
    
    arr_of_inputs = ["Car", "Truck", "Motorcycle"]

    for x in arr_of_inputs: 
        vehicle = VehicleFactory.createVehicle(x)
        vehicle.start_engine()

    print("End Of Testing!")