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


class VehicleManager(IVehicleManager):

    def __init__(self):
        self._logger = LoggerFactory.get_logger_manager()
        self._vehicles: list[Vehicle] = []

    def create_vehicle(self, vehicle_type: str) -> Vehicle:
        if vehicle_type.lower() == "car":
            vehicle = self._create_car()
        elif vehicle_type.lower() == "truck":
            vehicle = self._create_truck()
        elif vehicle_type.lower() == "motorcycle":
            vehicle = self._create_motorcycle()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
        
        self._vehicles.append(vehicle)
        return vehicle

    def start_all(self):
        if not self._vehicles:
            self._logger.log(ConstStrings.LOG_NAME_DEBUG,LoggerMessages.VEHICLE_NONE_CREATED)
            return
        
        self._logger.log(ConstStrings.LOG_NAME_DEBUG,LoggerMessages.VEHICLE_STARTING_ALL)
        for v in self._vehicles:
            v.start_engine()