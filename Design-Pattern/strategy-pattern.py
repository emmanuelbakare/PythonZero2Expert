# from abc import abstractmethod
# import string, random
# from typing import List 

# def generate_id(length=8):
#     return ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits, k=length))

# class SupportTicket:
#     id:str
#     customer:str
#     issue:str 
    
#     def __init__(self,customer,issue):
#         self.id=generate_id()
#         self.customer=customer
#         self.issue=issue
  
# class CustomerSupport:
#     tickets: List[SupportTicket] = []
    
     
#     def create_ticket(self, customer, issue):
#         self.tickets.append(SupportTicket(customer, issue))
    
#     def process_tickets(self, processing_strategy:str='lifo'):
#         if len(self.tickets)==0:
#             print('there is no ticket to process')
#             return
        
#         if processing_strategy=='fifo':
#             print('PROCESS TICKET: FIRST IN FIRST OUT')
#             for ticket in self.tickets:
#                 self.process_ticket(ticket)
#         elif processing_strategy=='lifo':
#             print('PROCESS TICKET: LAST IN FIRST OUT')
#             for ticket in reversed(self.tickets):
#                 self.process_ticket(ticket)
#         elif processing_strategy=='random':
#             print('PROCESS TICKET: RANDOMLY')
#             list_copy=self.tickets.copy()
#             random.shuffle(list_copy)
#             for ticket in list_copy:
#                 self.process_ticket(ticket)
        
#     def process_ticket(self, ticket:SupportTicket):
#         print('*'*40)
#         print('Processing Ticket ID:',ticket.id)
#         print('Processing Ticket Customer:',ticket.customer)
#         print('Processing Ticket Issue:',ticket.issue)
            
# # Create app
# app=CustomerSupport() 
     
# # Register few  Tickets
# app.create_ticket("Segun Adams","My computer is not booting")
# app.create_ticket("John Smith","I need to control my Mouse")
# app.create_ticket("Emmanuel oladele","Instructions giving is not clear on the manuals")
# app.create_ticket("Matthew Henry","Something is weird on my keyboard")

# app.process_tickets('random')         

# In the code above, creating fifo,lifo or random ordering can be abstracted 
# such that we will not need to do 'if else' to define them inside CustomerSupport.
# they should be seperated from the CustomerSupport class
# this is so that when new ordering type are made, you will not have to 
# edit the CustomerSupport class- ie. Customer Support class should be able
# to stand on its own

#===========================================================

from abc import ABC, abstractmethod
import string,random 
from typing import List 

def generate_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=length))

class SupportTicket:
    id:str 
    customer:str
    issue: str 
    
    def __init__(self, customer,issue):
        self.id=generate_id()
        self.customer=customer
        self.issue=issue


class TicketSort(ABC):
    
    @abstractmethod
    def sort(self, list:List[SupportTicket])->List[SupportTicket]:
        pass

class LIFOSortTicket(TicketSort):
    def sort(self, list:List[SupportTicket]):
        return list.copy()
    
class FIFOSortTicket(TicketSort):
    def sort(self, list:List[SupportTicket]):
        list_copy=list.copy()
        list_copy.reverse()
        return list_copy
    
class RandomSortTicket(TicketSort):
    def sort(self, list:List[SupportTicket]):
        list_copy=list.copy()
        random.shuffle(list_copy)
        return list_copy  
        
    
class CustomerSupport:
    tickets: List[SupportTicket] =[]
    
    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer,issue))
    
    def process_tickets(self, alltickets=TicketSort):
        
        sortedTickets=alltickets.sort(self.tickets)  
        
        for ticket in sortedTickets:
            self.print_ticket(ticket)
    def get_tickets(self):
        return self.tickets
    
    def print_ticket(self,SupportTicket):
        print("*"*40)
        print('Ticket ID:',SupportTicket.id )
        print('Ticket customer',SupportTicket.customer )
        print('Ticket issue',SupportTicket.issue )
        
        
support=CustomerSupport()    
support.create_ticket("Segun Adams","My computer is not booting")
support.create_ticket("John Smith","I need to control my Mouse")
support.create_ticket("Emmanuel oladele","Instructions giving is not clear on the manuals")
support.create_ticket("Matthew Henry","Something is weird on my keyboard")

# support.process_tickets(LIFOSortTicket())
# support.process_tickets(FIFOSortTicket())
# support.print_ticket
support.process_tickets(RandomSortTicket())  

# for ticket in support.get_tickets():
#     support.print_ticket(ticket)
