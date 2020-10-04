#Name: Kyle Look Fong
#Assignment Number: 2
#Date: 08/17/2020
#Secton: 12:30PM-2:00PM
#Description: A program that will help Mrs. Pie run her business operation
#calculating the number, type, total amount, discount amount, and final charge for pies.

#Constants
TAX_RATE = 1.0725
DISCOUNT_RATE = 0.06
CINNAMON_PRICE = 9.50
CINNAMON_MAX = 10
BERRY_PRICE = 12.50
BERRY_MAX = 20
DISCOUNT_AMOUNT_NEEDED = 40

#Variables
loop_again = "y"
pie_type = ""
pie_name = ""
pie_price = 0
pie_max = 0
num_pies = 0
total_charge = 0
discount_amount = 0

#While loop to repeat the program if needed
while loop_again == "y":
    print("Welcome to Delicious Pies (DP)") #Introductory remarks
    print("===============================")
    print("Cinnamon Apple (C or c)")
    print("Berry Apple (B or b)")

    #Prompting for the type of pie
    #if it's not c, C, b, or B, then it will not continue

    pie_type = input("Please enter the type of pie: ")

    #Setting the name, maximum numbers, and amounts to the respective names, 
    # maximum amounts, and amounts
    if (pie_type == "C" or pie_type == "c") or (pie_type == "B" or pie_type == "b"):   
        if pie_type == "c" or pie_type == "C": #Cinnamon Apple
            pie_name = "Cinnamon Apple" 
            pie_max = CINNAMON_MAX
            pie_price = CINNAMON_PRICE   
        else: #Berry Apple name, max amount, and price
            pie_name = "Berry Apple"
            pie_max = BERRY_MAX
            pie_price = BERRY_PRICE
        
        num_pies = int(input("Please enter the number of pie(s):")) #inputting the user to enter number of pies
        if num_pies <= 0: #if pies is zero
            print("You have entered a negative number or zero, no transaction will be conducted!")
        
        elif num_pies > pie_max: #if pies is more than max pies
            print("You cannot enter more than", pie_max, "pies!")
       
        else: #if pies is not zero or more than max
            total_charge = (num_pies * pie_price) #determining the total price
            if total_charge >= DISCOUNT_AMOUNT_NEEDED and pie_name == "Berry Apple": #Determining if the user is eligible for the discount
                #Discount Terms: over $40 and berry apples
                discount_amount = total_charge * DISCOUNT_RATE #Determining the discount total


                total_charge = (total_charge * TAX_RATE) #Chaning the original total charge to include tax
                #then printing it out
                print("The total charge for ", num_pies, " pie(s) is $", format(total_charge, ".2f"), sep = "")


                #printing the discount amount
                print("The discount amount is $", format(discount_amount, ".2f"), sep = "")


                total_charge = total_charge - (discount_amount * TAX_RATE) #Applying the tax to the discount rate
                #printing the amount after the discount
                print("The final charge after discount is $", format(total_charge, ".2f"), sep = "")

            elif total_charge < DISCOUNT_AMOUNT_NEEDED and pie_name == "Berry Apple": 
                #If the user is eligible because it's Berry Apple, 
                #but not eligible because it's under $40
                total_charge = total_charge * TAX_RATE #Calculating total charge
                
                #Printing the total charge and the reason why no discount
                print("The charge for ", num_pies, " pie(s) is $", format(total_charge, ".2f"), sep = "")
                print("The total price before tax is less than $40.00, no discount is given.")
            
            else: #if it was not a berry apple pie
                total_charge = total_charge * TAX_RATE #total charge calculation and print statement
                print("The final charge for ", num_pies, " pie(s) is $", format(total_charge, ".2f"), sep = "")
    else:
        print("You have entered an invalid pie type!") #If the user didn't enter a valid pie type (i.e. if valid_pie was not true)
    
    
    loop_again = input("\nDo you want to loop again? (y to loop again): ")
    print("\n\n")
        #Will either repeat or stop the loop

#At the end of the loop        
print("Thank you for shopping with us!")