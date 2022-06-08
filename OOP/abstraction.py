from abc import ABC, abstractmethod

class Computer(ABC):
    pass

    @abstractmethod
    def boot(self):
        pass
    
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def boot(self):
        print('System is booting...')

    def process(self):
        print("System running")

lap=Laptop()
lap.boot()
lap.process()


