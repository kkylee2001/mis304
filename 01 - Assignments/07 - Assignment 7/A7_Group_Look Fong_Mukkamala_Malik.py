#Name: Kyle Look Fong, Swara Mukkamala, Yusuf Malik
#Assignment Number: 7
#Date: 11/12/2020
#Secton: 12:30PM-2:00PM
#Description: Will allow for the user to either print the workers or add a worker 
# to the worker dictionary. First it will ask for the choice, then it will go over 
# each attribute in the worker class and set for each. After it is set, once the 
# user prompts to print, it will get all of the attributes. This is all using OOP.


from Worker import Worker #import the worker class 

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
    return choice.upper() #returns the choice


def addWorker(dictionary):
    w = Worker('', 0,0,'') #initializing a new instance of the Worker class, w
    try:
        name = input("\nPlease enter the worker's name: ")  #getting the name
        w.set_name(name)

        rate = float(input("Please enter the hourly rate: $"))
        if rate < 9.5 or rate > 80: #checking if the rate is between 9.5 and 80
            print("Rate is not between 9.5 and 80, it will be set to 0")
            rate = 0
        w.set_rate(rate) #setting the rate for the worker

        hours = float(input("Please enter the hours worked: "))
        if hours < 10 or hours > 40: #checking if the hours are between 10 and 40
            print("Hours is not between 10 and 40, it will be set to 0")
            hours = 0
        w.set_hours(hours) #setting the hours for the worker

        worker_type = input("This worker's type is ") #for the worker type
        w.set_type(worker_type)

        #give the user one more chance
        if rate < 9.5 or rate > 80: #if not in the valid range
            rate = float(input("Please enter the rate again: $")) #chance #2
            if rate < 9.5 or rate > 80: #checking
                print("New hourly rate is out of range! Value not updated")
                rate = 0
        w.set_rate(rate) #set the rate, 0 if invalid

        if hours < 10 or hours > 40: #checking if the hours not valid
            hours = float(input("Please enter hours again ")) #2nd chance
            if hours < 10 or hours > 40: #checking the input
                print("New hours is out of range! Value not updated") 
                hours = 0
        w.set_hours(hours) #setting the hours for the worker

        dictionary.update({w.get_name() : w}) #adding to the dictionary

    except ValueError as ve: #exception handling specific value error
        print("\nError:", ve)
        print("Worker was NOT successfully added\n")

def printWorker(dictionary): #will print all of the workers
    print("\n\nDisplay all Workers")
    print("====================")
    for worker in dictionary: #for each of the workers in the dictionary
        print("Name is", worker)
        rate = dictionary[worker].get_rate() #get the rate
        print("Rate is $" + str(rate))
        hours = dictionary[worker].get_hours() #get the hours
        print("Hours worked is " + str(hours))
        print("Worker type is", dictionary[worker].get_type()) #get the type
        print("\nSalary is $" + dictionary[worker].calculate_salary() + "\n\n") #get the salart
        


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
    while enter_loop.upper() == "YES": #if the user says yes
        choice = getChoice()
        if choice == UPDATE: #if they input b
            try: #general exception handling
                addWorker(dictionary=workers) #use the add worker function
            except Exception as err:
                print("ERROR:", err)
        elif choice == OUTPUT: #if they input d
            try: #general exception handling
                printWorker(dictionary=workers) #use the print worker funcition
            except Exception as err:
                print("ERROR:", err)
        enter_loop = input("\nDo you want to continue the program? Yes to continue: ")
#end of loop
main()
