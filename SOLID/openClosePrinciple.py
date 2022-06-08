'''
SOLID PRINCIPLE 2- OPEN CLOSE PRINCIPLE (OCP)

Objects or entities should be open for extension but closed for modification.

This means that a class should be extendable without modifying the class itself.
'''

class StorageLocker:
    client=''
    def authenticate(self):
        if self.client =='aws':
            pass
            # Do some AWS authentication
        elif self.client=='azure':
            pass
            #do som AZURE authentication
        return self.client
    
    def upload(self,filename ):
        if self.client =='aws':
            pass
            # Do some AWS authentication
        elif self.client=='azure':
            pass
            #do som AZURE authentication
        return self.client

# in the code above it becomes daunting to be modifying the StorageLocker class when
# we want to add a new platform like google clound platform
# there is need to abstract the platforms from the StoraLocker class so that we may be
# able to add new platform wthout modifying the StorageLocker class

from abc import ABC, abstractclassmethod

class Auth(ABC):
    @abstractclassmethod
    def authentication(self):
        pass

class Uploader(ABC):
    @abstractclassmethod
    def upload(self, filename):
        pass

class AWS(Auth,Uploader):
    def authentication(self):
        print('Authenticate against AWS Server')
    def upload(filename):
        print('Uploade to AWS Server')
        
class Azure(Auth,Uploader):
    def authentication(self):
        print('Authenticate against Azure Server')
    def upload(filename):
        print('Uploade to Azure Server')
    

class StorageLocker:
    client=''
    