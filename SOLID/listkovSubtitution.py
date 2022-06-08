'''
SOLID PRINCIPLE 3- Liskov Substitution Principle



Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.

This means that every subclass or derived class should be substitutable for their base or parent class
'''

class HomeAppliance:
    def on(self):pass
    def off(self):pass
    
# appliance with templaterature add more methods to what Homeapplicance and do (on of + temperature)    
class HomeApplicanceWithTemperature(HomeAppliance):
    def temperature(self):pass
    
#home appliance with a spinner methods added (on , off,+spinner)
class HomeApplianceWithSpinner(HomeAppliance):
    def spinner(self):pass
    
# a toaster is a Home applicance (has on and off) and also temperature settings
# so it inherites the HomeApplicanceWithTemperature
class Toaster(HomeApplicanceWithTemperature):
    def on(self):pass
    def off(self):pass
    def temperature(self):pass
    
# Juicer only as on and off so it inherits the HomeAppliance
class Juicer(HomeAppliance):
    def on(self):pass
    def off(self):pass

# a washing machine is HomeAppliance(on+off) and as a spinner so we use HomeApplianceWithSpinner 
class WashingMaching(HomeApplianceWithSpinner):
    def on(self):pass
    def off(self):pass
    def spinner(self):pass
    