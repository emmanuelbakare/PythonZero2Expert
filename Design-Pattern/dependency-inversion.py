# this is how to make sure one object does depend on the other to work

#problem

# class LightBulb:
#     def turnOff(self):
#         print('Turning Off The Light Bulb')
#     def turnOn(self):
#         print('Turning On The Light Bulb')
        
# class PowerSwith:
#     def __init__(self, bulb=LightBulb):
#         self.bulb=bulb
#         self.on=False
        
#     def press(self):
#         if self.on:
#             self.bulb.turnOff()        
#             self.on=False
#         else:
#              self.bulb.turnOn()
#              self.on= True          

# bulb=LightBulb()

# switch=PowerSwith(bulb)
# switch.press()
# switch.press()

# ============================================================
# In the example able, the switch is hardcoded to take in lightbulb.
# this makes the PowerSwith depended on the lightbulb.
# a better implementation is to allow the switch be able to turn on any
# electronic device (bulb, fan, tv etc) by making sure all electronic
# implements the on and off method using python abrstract base class(ABC)

from abc import ABC, abstractmethod

class Electronic:
    
    @abstractmethod
    def turnOn(self):
        pass
    
    @abstractmethod
    def turnOff(self):
        pass
    
# LightBulb  inherits abract class Electronic and must implement turnOn and turnOff       
class LightBulb(Electronic): 
    def turnOff(self):
        print('Turn OFF the LIGHT BULB')
    
    def turnOn(self):
        print('Turn ON the LIGHT BULB')
        
 # Fan  inherits abract class Electronic and must implement turnOn and turnOff       
class Fan(Electronic):
    def turnOff(self):
        print('Turn OFF the FAN')
    
    def turnOn(self):
        print('Turn ON the FAN')
 
class ElectricPowerSwitch:
    def __init__(self, electronic:Electronic):
        self.electronic=electronic
        self.on=False
    
    def press(self):
        if self.on:
            self.electronic.turnOff()
            self.on=False
        else:
            self.electronic.turnOn()
            self.on=True

fan=Fan()
bulb=LightBulb()

fanswitch=ElectricPowerSwitch(fan)
bulbswitch=ElectricPowerSwitch(bulb)

fanswitch.press()
fanswitch.press()
bulbswitch.press()
bulbswitch.press()


