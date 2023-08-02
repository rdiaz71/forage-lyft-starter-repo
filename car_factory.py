from car import Car
import battery
import engine

def create_calliope(self, current_date, last_service_date, current_milage, last_service_milage):
    engine = engine.CapuletEngine(current_milage, last_service_milage)
    battery = battery.NubbinBattery(last_service_date, current_date)
    return Car(engine, battery)

def create_glissade(self, current_date, last_service_date, current_milage, last_service_milage):
    engine = engine.WilloughbyEngine(current_milage, last_service_milage)
    battery = battery.NubbinBattery(last_service_date, current_date)
    return Car(engine, battery)

def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
    engine = engine.SternmanEngine(warning_light_is_on)
    battery = battery.SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)

def create_rorschach(self, current_date, last_service_date, current_milage, last_service_milage):
    engine = engine.WilloughbyEngine(current_milage, last_service_milage)
    battery = battery.SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)

def create_thovex(self, current_date, last_service_date, current_milage, last_service_milage):
    engine = engine.CapuletEngine(current_milage, last_service_milage)
    battery = battery.SpindlerBattery(last_service_date, current_date)
    return Car(engine, battery)