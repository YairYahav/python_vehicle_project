from .vehicle import Vehicle
from globals.consts.logger_messages import LoggerMessages
from infrastructure.factories.logger_factory import LoggerFactory
from globals.consts.const_strings import ConstStrings

class Truck(Vehicle):

    type_of_vehicle = "truck"
    def __init__(self):
        super().__init__("Truck")
        self._logger = LoggerFactory.get_logger_manager()

    def start_engine(self):
        self._logger.log(ConstStrings.LOG_NAME_DEBUG, f"Engine started for vehicle of type: {self.type_of_vehicle}")
