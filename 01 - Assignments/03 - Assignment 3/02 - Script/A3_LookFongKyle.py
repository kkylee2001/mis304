#Name: Kyle Look Fong
#Assignment Number: 3
#Date: 09/20/2020
#Secton: 12:30PM-2:00PM
#Description: Creating a point of sale system for Mrs. Canva to sell her bags to clients
#tracking her inventory, profits, and revenues.

#Program I



#Constants
OPTIONS = [
    "\n", 
    "Welcome to GLB", 
    "==============",
    "P or p: All Purpose bag", 
    "G or G: Good Looking Bag",
    "T or T: Tote bag"
]       #introductory statements
LOOP_STATEMENT = "Enter R or r to repeat and any other letters to quit! " #loop
BAG_PROFITS = [0.25, 0.32, 0.40] #Profit percentages at same indexes as name and price
BAGS = ["All-Purpose", "Good-Looking", "Tote"]
BAGS_PRICES = [7.99, 9.99, 7.99]
REPEAT_STATEMENT = "Do you want to repeat the menu?" #repeat statement
INITIAL_INV = [15,26,34]




#Variable Initialization
enter_loop = "R" #While Loop


total_bags_sold = 0 #Accounting
revenue = 0
total_revenue = 0
rev = 0
profits = 0
total_profit = 0



bag_chosen = "" #Transaction
number_picked = 0
current_inv = [15, 26, 34]
bags_sold = [0,0,0]




#Business Report

def accounting(all_purpose, good_looking, tote): #parameters are the respective numbers for bags
    print("\n\n")       #intro
    print("Business Report for GLB")
    print("=======================")

    bags_sold = [all_purpose, good_looking, tote] #copying the numbers into an array


    total_bags_sold = 0  #resetting 
    for num_bag in range(0,3):  #for each bag, run the print function and add to total bags
        print("You have sold", bags_sold[num_bag], BAGS[num_bag], "bag(s)")
        total_bags_sold += bags_sold[num_bag]
    
    print("You have sold a total of", total_bags_sold, "bag(s)")    #print total bags


    total_revenue = 0 #resetting
    for num_bag in range(0,3):  #for each bag, determine the revenue and add to total revenue
        rev = bags_sold[num_bag] * BAGS_PRICES[num_bag]
        print("The revenue for ", BAGS[num_bag], " bag(s) is $",format(rev, ".2f"),sep = "")
        total_revenue += bags_sold[num_bag] * BAGS_PRICES[num_bag]

    print("The total revenue is $", format(total_revenue, ".2f"), sep="")


    total_profit = 0 #resetting
    for num_bag in range(0,3): #for each bag determine the profit and add to total profit
        profits = (bags_sold[num_bag] * BAGS_PRICES[num_bag]) * BAG_PROFITS[num_bag]
        print("Your profit for ", BAGS[num_bag], " bag is $", format(profits, ".2f"), sep = "")
        total_profit += (bags_sold[num_bag] * BAGS_PRICES[num_bag]) * BAG_PROFITS[num_bag]

    print("Your total profit is $", format(total_profit, ".2f"), sep = "")



#New transaction

def transaction(bag_name): #when the user inputs a letter, it'll determine what to do with it
    if bag_name == "P" or bag_name == "p": #all purpose, check amount, go into new_transaction
        bag_total = int(input("How many bags does the customer want? "))
        new_transaction(0, bag_total, "All Purpose Bags")


    elif bag_name == "G" or bag_name == "g": #good looking, check amount, go into new_transaction
        bag_total = int(input("How many bags does the customer want? "))
        new_transaction(1, bag_total, "Good-Looking Bags")


    elif bag_name == "T" or bag_name == "t": #tote, check amount, go into new_transaction
        bag_total = int(input("How many bags does the customer want? "))
        new_transaction(2, bag_total, "Tote Bags")


    else: #handling invalid characters
        print("You have entered an invalid letter")
        print()

def new_transaction(index, total, bag_name):
    while total <= 0: #VALIDATION LOOP: continuously prompting the user to input a valid number
        print("You have entered an invalid number. Try Again!")
        total = int(input("How many bags? "))
        print()

    if current_inv[index] >= total:    #if still in stock
        current_inv[index] -= total    #remove from inventory
        print("You have sold", total, bag_name)
        print()
    else:   #if not in stock
        print("Sorry! You do not have enough", bag_name, "for sale") #printing that out of stock
        print()
        print("You only have", current_inv[index], "bag(s) in stock") #printing what is still left in stock
        print()







while enter_loop == "R" or enter_loop == "r": #Start of while loop
        #introductory statements
    for opt in OPTIONS: #print each of the statements
        print(opt)

    bag_chosen = input("Please input the type of bag that the customer wants: ") #prompt user which bag
    print()
    transaction(bag_chosen) #puts that into the transaction function

    print(REPEAT_STATEMENT)
    enter_loop = input(LOOP_STATEMENT) #Prompting user to re-enter loop or exit


for bag in range (3):
    bags_sold[bag] = INITIAL_INV[bag] - current_inv[bag]
    
accounting(bags_sold[0], bags_sold[1], bags_sold[2]) #calls the accounting function for the bag
        #at their respective numbers, default to zero
