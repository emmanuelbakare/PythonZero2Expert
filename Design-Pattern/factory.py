from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    
    @abstractclassmethod
    def delivery(self):
        pass
    
class Truck(Vehicle):
    def delivery(self):
        print('Deliver via a TRUCK')
        
class Ship(Vehicle):
    def delivery(self):
        print('Deliver via a SHIP')
        
class AirBus(Vehicle):
    def delivery(self):
        print('Deliver via a AIRBUS')

def factory_method(vehicle_type):
    mapper={
        'truck':Truck,
        'ship': Ship,
        'airbus': AirBus,
    }

    return mapper[vehicle_type]() 



deliveryVehicle=factory_method('airbus')     

deliveryVehicle.delivery()  
