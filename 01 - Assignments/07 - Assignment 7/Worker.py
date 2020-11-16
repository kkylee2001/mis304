
                        #Worker Class.py
#================================================================#
class Worker():
    #__init__ for all attributes
    def __init__(self, name, rate, hours, worker_type):
        self.name = name
        self.rate = rate
        self.hours = hours
        self.type = worker_type
    
    #__str__ that will output that values of all variables
    def __str__(self):
        desc = "Name: " + self.name + " who works for " + str(self.hours) 
        desc += (" hours at $" + str(self.rate) + " is a " + self.type  + " worker.")
        return desc

    #getters for each attribute
    def get_name(self):
        return self.name
    def get_rate(self):
        return self.rate
    def get_hours(self):
        return self.hours
    def get_type(self):
        return self.type

    #setters for each attribute
    def set_name(self, x):
        self.name = x
    def set_rate(self, x):
        self.rate = x
    def set_hours(self, x):
        self.hours = x
    def set_type(self, x):
        self.type = x

    def calculate_salary(self):
        salary = round(self.hours * self.rate, 2)
        return format(salary, '.2f')



