from datetime import datetime

class Call:
    
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y %H:%M %p") # format mm-dd-yyyy hh-mm
    
    def __init__(self, id, name, phone, reason):
        self.id = id
        self.name = name
        self.phone = phone
        self.reason = reason
        
    def display(self):
        print(f'Caller unique id: {self.id} ')
        print(f'Caller Name: {self.name} ')
        print(f'Caller Phone number: {self.phone} ')
        print(f'Current time: {self.current_time} ')
        print(f'Reason for calling: {self.reason} ')
        
class CallCenter:
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
        
    def add(self, new):
        # will add at the end of the list, if it's an call object
        if type(new) == Call:
            self.calls.append(new)
        else:
            print('call not valid')
    
    def remove(self):
        # will remove the first call once the method called
        self.calls.pop(0)
        
    def info(self):
        # loop around and display all the calls name and phone number
        count = 0
        for i in self.calls:
            print(f'Name: {i.name}, Phone Number: {i.phone} ')
            count += 1
        print(f'There are {count} calls in the queues')
    
c = Call(1, 'Israel', '456-123-0987', 'Appointment for tomorrow')
d = Call(2, 'John', '987-456-0123', 'Schedule a new appointment')
e = Call(3, 'Oshil', '123-456-7890', 'Cancel an appointment')

central = CallCenter()
#adding the three calls to the call center
central.add(c)
central.add(d)
central.add(e)
#show the call list
central.info()
#remove a calls
central.remove()
#show the new call list
central.info()
    