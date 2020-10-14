#FUNCTIONS AND TYPES - OCTOBER 5

'''
#A FUNCTION THAT RECIEVES ARGUMENTS AND RETURNS A VALUE
def main():
    number1 = 5
    number2 = 2
    result = subtract(num1=number1, num2=number2)
    print("In main, the result is", result)

def subtract(num1, num2):
    difference = num1 - num2
    return difference

main()


#REWRITE MULTIPLICATION PROGRAM
def main():
    number1 = int(input("Number 1: "))
    number2 = int(input("Number 2: "))
    result = multiply(num1=number1, num2=number2)
    print("The total is", result)

def multiply(num1, num2):
    product = num1 * num2
    return product

main()
'''


#EX-4
#Global Accumulator

def main():
    #Constant
    TENNIS_PRICE = 50.00

    #Variables
    qty_accumulator = 0
    dollar_accumulator = 0
    enter_loop = ""

    
    while enter_loop == "":
        print("\nMENU\n=====================")
        print("Tennis Racket: ($",format(TENNIS_PRICE, ".2f"),")\n", sep = "")
        num_rackets = get_number()
        qty_accumulator += num_rackets
        sutotal = calculate_charge(qty=num_rackets, price=TENNIS_PRICE)
        dollar_accumulator += sutotal
        print()
        print("RECIPT\n=====================")
        print("Tennis Racket ($", format(TENNIS_PRICE, ".2f"), "): ", num_rackets, sep = "")
        print("Subtotal: $", format(sutotal, ".2f"), sep = "")
        enter_loop = input("Press Enter or Return to repeat ")
        
    print("\n\n")
    print("Business Report\n=====================")
    print("Tennis Racket ($", format(TENNIS_PRICE, ".2f"),")",sep = "")
    print("Quantity:", qty_accumulator)
    print("Total: $", format(dollar_accumulator, ".2f"), sep = "")
    print("Thank you for shopping with us!")

def get_number():
    qty_rackets = 88888
    while qty_rackets == 88888:
        try:
            qty_rackets = int(input("Insert Qty: "))
            while qty_rackets <= -1:
                print("You cannot have a negative number, try again!")
                qty_rackets = int(input("Insert Qty: "))
        except:
            print("You have to type in a number silly, try again")
            try:
                qty_rackets = int(input("Insert Qty: "))
                while qty_rackets <= -1:
                    print("You cannot have a negative number, try again!")
                    qty_rackets = int(input("Insert Qty: "))
            except:
                print("You have to type in a number silly, try again!")
                qty_rackets = 88888
    return qty_rackets

def calculate_charge(qty, price):
    product = qty * price
    return product

main()
