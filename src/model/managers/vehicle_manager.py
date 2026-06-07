import time
import threading

from infrastructure.interfaces.ivehicle_manager import IVehicleManager
from infrastructure.interfaces.ivehicle_manager import IVehicleManager
from infrastructure.interfaces.ikafka_manager import IKafkaManager
from model.data_classes.vehicle import Vehicle
from globals.consts.const_strings import ConstStrings
from globals.consts.consts import Consts
from globals.consts.logger_messages import LoggerMessages
from infrastructure.factories.logger_factory import LoggerFactory
from infrastructure.factories.vehicle_factory import VehicleFactory


class VehicleManager(IVehicleManager):

    def __init__(self):
        self._logger = LoggerFactory.get_logger_manager()
        self._vehicles: list[Vehicle] = []

    def create_vehicle(self, vehicle_type: str) -> Vehicle:
        vehicle = VehicleFactory.create_vehicle(vehicle_type)

        if vehicle: 
            self._vehicles.append(vehicle)
            self._logger.log(ConstStrings.LOG_NAME_DEBUG, f"Created vehicle of type: {vehicle_type}")

        else:
            self._logger.log(ConstStrings.LOG_NAME_ERROR, f"Failed to create vehicle of type: {vehicle_type}")
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")


    def start_all(self):
        if not self._vehicles:
            self._logger.log(ConstStrings.LOG_NAME_DEBUG, "No vehicles have been created yet.")
            return
        
        self._logger.log(ConstStrings.LOG_NAME_DEBUG, f"Starting engines for all {len(self._vehicles)} vehicles...")
        for v in self._vehicles:
            v.start_engine()