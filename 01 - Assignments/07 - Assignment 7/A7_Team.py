#Name: Kyle Look Fong
#Assignment Number: 7
#Date: 11/12/2020
#Secton: 12:30PM-2:00PM
#Description: 

                #Importing the Worker Class
#================================================================#
from Worker import Worker

def getChoice():
    print("\n\nWelcome to the Worker Program")
    print("=============================")
    print("B: Add to new worker or update")
    print("D: Print the workers report")
    #init choice
    choice = ""
    #Asking for the choice
    choice = input("Please enter your choice: ")
    #Validation loop
    while choice.upper() not in ("B", "D"):
        print("Invalid Choice! It must be B or D")
        choice = input("Please enter your choice: ")
    return choice.upper()


def addWorker(dictionary):
    w = Worker('', 0,0,'') #initializing a new instance of the Worker class, w
    try:
        name = input("\nPlease enter the worker's name: ")  
        w.set_name(name)
        rate = float(input("Please enter the hourly rate: $"))
        if rate < 7.5 or rate > 70:
            print("Rate is not between 7.5 and 70, it will be set to 0")
            rate = 0
        w.set_rate(rate)
        hours = float(input("Please enter the hours worked: "))
        if hours < 5 or hours > 40:
            print("Hours is not between 5 and 40, it will be set to 0")
            hours = 0
        w.set_hours(hours)
        worker_type = input("This worker's type is ")
        w.set_type(worker_type)

        if rate < 7.5 or rate > 70:
            rate = float(input("Please enter the rate again: $"))
            if rate < 7.5 or rate > 70:
                print("New hourly rate is out of range! Value not updated")
                rate = 0
        w.set_rate(rate)
        if hours < 5 or hours > 40:
            hours = float(input("Please enter hours again"))
            if hours < 5 or hours > 40:
                print("New hours is out of range! Value not updated")
                hours = 0
        w.set_hours(hours)
        dictionary.update({w.get_name() : w})
    except ValueError as ve:
        print("\nError:", ve)
        print("Worker was NOT successfully added\n")

def printWorker(dictionary):
    print("\n\nDisplay all Workers")
    print("====================")
    for worker in dictionary:
        print("Name is", worker)
        rate = dictionary[worker].rate
        print("Rate is $" + str(rate))
        hours = dictionary[worker].hours
        print("Hours worked is " + str(hours))
        print("Worker type is", dictionary[worker].type)
        print("\nSalary is $" + dictionary[worker].calculate_salary() + "\n\n")
        


def main():
        #CONSTANTS Init
    UPDATE = "B"
    OUTPUT = "D"

        #Create an empty array
    workers = {}

        #Create objects for the following values
    mary = Worker('Mary Johnson', 41.00, 40, 'full-time')
    jason =  Worker('Jason Biden', 30.00, 40, 'full-time')
    joe = Worker('Joe Truth', 24.00, 15, 'part-time')
        
        #Insert objects into dictionary
    workers.update({mary.get_name(): mary})
    workers.update({jason.get_name(): jason})
    workers.update({joe.get_name(): joe})

        #Ask if they want to begin the program
    enter_loop = ""
    enter_loop = input("Do you want to continue the program? Yes to continue: ")
    choice = ""
    while enter_loop.upper() == "YES":
        choice = getChoice()
        if choice == UPDATE:
            try:
                addWorker(dictionary=workers)
            except Exception as err:
                print("ERROR:", err)
        elif choice == OUTPUT:
            try:
                printWorker(dictionary=workers)
            except Exception as err:
                print("ERROR:", err)
        enter_loop = input("\nDo you want to continue the program? Yes to continue: ")
main()
