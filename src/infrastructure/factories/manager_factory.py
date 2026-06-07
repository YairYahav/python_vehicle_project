from infrastructure.factories.infrastructure_factory import InfrastructureFactory
from globals.consts.const_strings import ConstStrings
from infrastructure.interfaces.ivehicle_manager import IVehicleManager
from infrastructure.interfaces.izmq_server_manager import IZmqServerManager
from model.managers.vehicle_manager import VehicleManager
from infrastructure.interfaces.ilogger_manager import ILoggerManager
from globals.enums.vehicle_enums import VehicleEnums


class ManagerFactory:
    @staticmethod
    def create_vehicle_manager() -> IVehicleManager:
        config_manager = InfrastructureFactory.create_config_manager(
            ConstStrings.GLOBAL_CONFIG_PATH)
        return VehicleManager()

    @staticmethod
    def create_example_zmq_manager() -> IZmqServerManager:
        return InfrastructureFactory.create_zmq_server_manager()

    @staticmethod
    def create_all():
        vehicle_manager = ManagerFactory.create_vehicle_manager()

        vehicle_manager.create_vehicle(VehicleEnums.CAR.value)
        vehicle_manager.create_vehicle(VehicleEnums.TRUCK.value)
        vehicle_manager.create_vehicle(VehicleEnums.MOTORCYCLE.value)

        vehicle_manager.start_all()
