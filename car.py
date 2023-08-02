from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, Engine, Battery, Tires):
        self.engine = Engine
        self.battery = Battery
        self.tires = Tires
        
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
        