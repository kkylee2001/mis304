
                        #Worker Class.py
#================================================================#
class Worker():
    #__init__ for all attributes
    def __init__(self, name, rate, hours, worker_type):
        self.__name = name
        self.__rate = rate
        self.__hours = hours
        self.__type = worker_type
    
    #__str__ that will output that values of all variables
    def __str__(self):
        desc = "Name: " + self.__name + " who works for " + str(self.__hours) 
        desc += (" hours at $" + str(self.__rate) + " is a " + self.__type  + " worker.")
        return desc

    #getters for each attribute
    def get_name(self):
        return self.__name
    def get_rate(self):
        return format(self.__rate, '.2f')
    def get_hours(self):
        return self.__hours
    def get_type(self):
        return self.__type

    #setters for each attribute
    def set_name(self, x):
        self.__name = x
    def set_rate(self, x):
        self.__rate = x
    def set_hours(self, x):
        self.__hours = x
    def set_type(self, x):
        self.__type = x

    #Calculate salary method 
    def calculate_salary(self):
        salary = round(self.__hours * self.__rate, 2)
        return format(salary, '.2f')



