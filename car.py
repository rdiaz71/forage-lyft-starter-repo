from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery

class Car(ABC):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery
        
    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service or self.battery.needs_service
        
