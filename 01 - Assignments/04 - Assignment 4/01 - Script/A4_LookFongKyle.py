#Name: Kyle Look Fong
#Assignment Number: 4
#Date: 10/09/2020
#Secton: 12:30PM-2:00PM
#Description: Creating a POS System for Cool Hats


def main():
    #CONSTANTS
    M_PRICE = 19.00
    W_PRICE = 21.00
    TAX_RATE = 1.075
    DISCOUNT_RATE = 0.05


    M_LIMIT = 6 #Not in instructions but created constant
    W_LIMIT = 4
    DISCOUNT_NEEED = 50
    
    #VARIABLES
        #Loop
    enter_loop = "Y"
        #Hat selection
    selected_hat = ""
    qty_hat = 0
        #Transaction
    m_accumulator = 0
    w_accumulator = 0
    subtotal = 0
    discount_amount = 0
    total_after_discount = 0
    taxed_charge = 0

    #FUNCTIONS


    def getChoice(): #Prompts the user for their bag choice and returns value
        print("\nWelcome to Cool Hats \n===========================")
        print("M: Handsome UV ($",format(M_PRICE, ".2f"),") Limit ", M_LIMIT, sep = "")
        print("W: Beautiful UV ($",format(W_PRICE, ".2f"),") Limit ", W_LIMIT, sep = "")
        print()
        return input("Please enter your choice: ")  #returned value

    def processTransaction(qty, price): #returns the amount to be accululated
        return qty * price    #qty x price     


    #PROGRAM
    while enter_loop == "Y" or enter_loop == "y": #START LOOP
        selected_hat = getChoice()
        
        if selected_hat == "M" or selected_hat == "m": #Men's hat
            qty_hat = int(input("Please enter the number of hats: ")) #qty
            while qty_hat < 0 or qty_hat > M_LIMIT: #VALIDATION LOOP - Number of hats
                if qty_hat < 1:
                    print("You cannot enter a negative number!")
                else:
                     print("The number entered is", qty_hat, "which is more than", M_LIMIT)
                qty_hat = int(input("Please enter the number of hats: "))
            m_accumulator += processTransaction(qty=qty_hat, price=M_PRICE) #adding the hat to accumulator
        
        elif selected_hat == "W" or selected_hat == "w": #Woman's hat
            qty_hat = int(input("Please enter the number of hats: ")) #qty
            while qty_hat < 0 or qty_hat > W_LIMIT: #VALIDATION LOOP - Number of hats
                if qty_hat < 1:
                    print("You cannot enter a negative number!")
                else:
                     print("The number entered is", qty_hat, "which is more than", W_LIMIT)
                qty_hat = int(input("Please enter the number of hats: ")) 
            w_accumulator += processTransaction(qty=qty_hat, price=W_PRICE) #adding the hat to accumulator
        
        else: #invalid characters
            print("The choice is neither M/m not W/w")

        enter_loop = input("Would you like to repeat the menu? ") #END LOOP
    
    #Transactional Math
    subtotal = m_accumulator + w_accumulator #all hats combined
    discount_amount = subtotal * DISCOUNT_RATE #if discount applied
    total_after_discount = subtotal - discount_amount #if discount applied
    taxed_charge = total_after_discount * TAX_RATE if subtotal >= 50 else subtotal * TAX_RATE #will make the taxed charge determined by the subtotal's amount


    print("Transaction Summary \n=====================") #printing each of the variables
    print("The charge for Handsome UV is $", format(m_accumulator, ".2f"), sep = "") #Men's
    print("The charge for Beautiful UV is $", format(w_accumulator, ".2f"), sep = "") #Women's 
    print("The grand total is $", format(subtotal, ".2f"), sep="") #Subtotal
   
    if subtotal >= 50: #if a discount
        print("Because the grand total has exceeded $", format(DISCOUNT_NEEED, ".2f"), ", You will recieve a $", format(discount_amount, ".2f"), " discount", sep="")
        print("Your total after discount is $", format(total_after_discount, ".2f"), sep = "")
    print("Your final charge with tax is $", format(taxed_charge, ".2f"), sep = "") #Charge with tax

main()
