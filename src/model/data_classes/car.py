from .vehicle import Vehicle
from globals.consts.logger_messages import LoggerMessages
from infrastructure.factories.logger_factory import LoggerFactory
from globals.consts.const_strings import ConstStrings

class Car(Vehicle):

    type_of_vehicle = "car"
    def __init__(self):
        super().__init__("Car")
        self._logger = LoggerFactory.get_logger_manager()

    def start_engine(self):
        self._logger.log(ConstStrings.LOG_NAME_DEBUG,LoggerMessages.ENGINE_STARTED.format(self.type_of_vehicle))

