
##DON'T FORGET THE HEADING


                            #Constants 
#=====================================================================
#--None--


                            #Global Variables
#=====================================================================
#--None--



                            #Functions 
#=====================================================================
#--Exception Handling -- ?? -- Needs to be done
def exceptionHandling(trying, excepting): #Try except, prints out the error and has two functions as
                                            #parameters. TENTATIVE
    try:
        trying()
    except Exception as err:
        print("Error:", err)
        excepting()

###############################
#Get Decision: Will recieve both upper and lower cases of both choices, should have
#four parameters. Return the choice (P, p, F, f) back to main

def getDecision(c1, c2, c3, c4): #The four valid choices
    choice = input("Enter your selection: ") #prompts user for their selection
    
    while choice not in [c1, c2, c3, c4]: #Validation loop to re-enter the choice and check if in choices
        print("Invalid Choice!\n")
        choice = input("Re-enter your selection: ")
        
    return choice #returning the choice


###############################
#Open File: Return the file information based on the user's input, no arguments
#Read: has to be Brownie.txt
#Write: has to be named differently than Brownie.txt

def openFile():
    namedFile = input("Name of File: ") #prompting for name of file
    file_mode = input("Enter file mode: ") #prompting for the access type
    print('\n\n')
    while file_mode not in ("r", "w"): #V-loop ensuring that the file access is correct
        print("Invalid access type. Must be in (r, w)")
        file_mode = input("Enter file mode: ")

    if file_mode == "r": #Reading the file
        while namedFile != "Brownie.txt": #V-loop to make sure that the name is Brownie.txt
            print("You have to use 'Brownie.txt' to use mode r, try again.\n")
            namedFile = input("Name of File: ") #Don't have to check for file type (.txt), it has to be
                                                #Brownie.txt
    else:
        while namedFile == "Brownie.txt": #V-loop ensuring that the file name is not Brownie.txt
            print("You need to use a different file name, not 'Brownie.txt', try again.\n")
            namedFile = input("Name of File: ")
        while ".txt" not in namedFile: #V-loop ensuring that the file extension is txt
            print("File has to has a .txt extension, try again")
            namedFile = input("Name of File: ")

    return open(namedFile, file_mode) #Returning the opened file


###############################
#Update Files: Accept two file variables as parameters. Prompts the user for the number
#of records to write. Use a loop to read the brownie, price and cost, determine profit from
#the input file and copy it to the output file

def updateFile(inputting, updating): #two parameters, the input and update files
    records = int(input("Number of Records: ")) #ask how many records
    brownie_accumulator = 0 #Ensuring that the number of brownies returned is <= number asked
    line = inputting.readline() #Initial

    while line != "" and brownie_accumulator < records: #Until empty or records full
                                                            

        browine_selected = line.rstrip('\n') #Getting rid of the extra space
        updating.write(str(brownie_accumulator+1) + ") Brownie: " + browine_selected + "\n")
                #Writing the brownie selected in the update file
                #ex. 1) Brownie: Caramel Brownie

        line = inputting.readline() #Read next line
        price = float(line) #Formatting the next line into a float -- required
        updating.write("Price: $" + format(price, ".2f") + "\n")
                #Writing the brownie's price to the update file
                #ex. Price: $2.00

        line = inputting.readline() #Read next line
        cost = float(line) #Formatting the cost into a float -- required
        updating.write("Cost: $" + format(cost, ".2f") + "\n")
                #Writing the brownie's cost to the update file
                #e.x. Cost: $0.35

        profit = price - cost #Calculating profit:  profit = rev - costs
        updating.write("Profit: $" + format(profit, ".2f") + "\n")
                #Writing the brownie's profit to the update file
                #e.x. Profit: $1.50

        profit_margin = round(100*(profit/price), 2)
        updating.write("Profit Margin: " + format(profit_margin, ".2f") + "%\n\n")
                #Writing the brownie's profit margin to the update file -- In the example output
                #e.x. Profit Margin: 80% 


        brownie_accumulator += 1
                #Accumulating to see the number of brownies 
        line = inputting.readline() #Next line
        
    print("Completed!") #Out of loop
    inputting.close #Closing files
    updating.close



###############################
#Print Business Report: read the Brownie.txt file and display the file into, each typ
#their price, costs, profit, and profit margins. Rounded to two decimal places

def printBusinessReport(txt_file): #Parameter: the Brownie.txt file_mode

    brownie_accumulator = 0 #To display the number of brownies at the end
    profit_accumulator = 0 #Calculating average profit
    cost_accumulator = 0 #Calculating average cost
    line = txt_file.readline() #First Line
    while line != "": #While the line is not empty

        brownie_type = line.rstrip('\n') #Getting the brownie without the extra \n
        print("Brownie:", brownie_type) #Print
        line = txt_file.readline() # Next Line

        price = float(line) #Calculating price -- next line
        print("Price: $", format(price, ".2f"), sep='')
        line = txt_file.readline()

        cost = float(line) #Calculating Cost -- next line
        print("Cost: $", format(cost, ".2f"), sep='')

        profit = price - cost #Calculating Profit: P = rev - cost
        print("Profit: $", format(profit, ".2f"), sep='')

        profit_margin = round(100*(profit/price), 2) #Calculating profit margin: P% = P/rev
        print("Profit Margin: ", profit_margin, "%", sep='')

        brownie_accumulator += 1 #Add to accumulator
        profit_accumulator += profit #add to accumulator the profit calculated
        cost_accumulator += cost #Add to accumulator the cost calculated
        line = txt_file.readline() #Next Line
    
        print("\n\n") #Printing for readability
    
    print("You have reached the end of the documant\n") #Out of while loop
    print("A total of", brownie_accumulator, "brownies has been processed")

    avg_profit = profit_accumulator/brownie_accumulator #Calculating averages, printing
    avg_cost = cost_accumulator/brownie_accumulator
    print("Average Profit: $", format(avg_profit, ".2f"), sep='')
    print("Average Cost: $", format(avg_cost, ".2f"), sep='')


    txt_file.close()    #Closing file


 
                            #Start of Program
#=====================================================================

def main(): #Main Function -- Calls program
    enter_loop = '' #Allows the use to go through the program multiple times
    while enter_loop == '': #Simply pressing return/enter on keyboard
        try:
            print("\nWelcome to Mr. Brown's Brownie Shop\n===================")
            print("P or p -- (P)rint Brownie Report")
            print("F or f -- Update (F)ile") #intro
            mode = getDecision("P", "p", "F", "f") #Four arguments, P, p, F, f

            if mode in ["P", "p"]: #if it's P or p
                print_file = openFile() #open file and read
                printBusinessReport(print_file) #print the business report


            else: #if not p or P
                print("\n\nInput File-------") #prompt for input
                input_file = openFile()

                print("\nOutput File--------") #prompt for output 
                output_file = openFile()

                updateFile(inputting=input_file, updating=output_file) #writing to the update file
            
            enter_loop = input("Press return to repeat, any key to end: ") #Repeat program or not
        except Exception as err:
            print("ERROR:", err)
            enter_loop = input("Press return to repeat, any key to end: ") #Repeat program or not



main() #Calling main

