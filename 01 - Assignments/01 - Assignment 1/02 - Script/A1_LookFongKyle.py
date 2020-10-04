#Name: Kyle Look Fong
#Assignment Number: 1
#Date: 08/04/2020
#Secton: 12:30PM-2:00PM
#Description: Two programms that calculate the total charges for cooresponding products in a business.
#The first program calculates the total for a Soap company based on the amount of bottles and the amount of drops
#The second program calculages the total amount, with tax, for a jam company based on the amount of each respective jam ordered


#Program I

#Variable Initialization
bottles: int = 0
lav_drops: int = 0
soap_total: int = 0

#introduction
print("Program One: \n")
print("Welcome to the Soap Company!")
print("************************* \n")

#inputs for each bottle to be purchsed and each drop of lavendar, to be assigned to their variables
bottles = int(input("Please Enter the Number of Bottle(s): "))
lav_drops = int(input("Please Enter the Number of Drop(s) for each bottle: "))

#calculation of the total amount to charge for the soap ($10/bottle and $0.40/lavendar/bottle)
soap_total = (10 * bottles) + (lav_drops * bottles * 0.40)

#Print statement for the total, with currency formatting
print("The total charge for ", bottles, " bottle(s) of hand soap and ", lav_drops,
      " drop(s) of lavendar oil is $", format(soap_total, ".2f"), sep = "")

#printing lines
print("\n\n")





#Program II

#Variable Initialization
name: str = ""
straw_jam: int = 0
blue_jam: int = 0
o_jam: int = 0
straw_total: float = 0.0
blue_total: float = 0.0
o_total: float = 0.0
total_charge: float = 0.0
taxes: float = 0.0
taxed_total: float = 0.0

#introduction
print("Program Two: \n")        
print("Welcome to the Best Jam Store!")
print("************************* \n")

#Inputs for the customer's name and the amount of each jam they want to purchase
name = input("Please Enter Customer Name: ")
straw_jam = int(input("Please enter the quantity for Strawberry Jam ($9.20): "))
blue_jam = int(input("Please enter the quantity for Blueberry Jam ($10.80): "))
o_jam = int(input("Please enter the quantity for Orange Jam ($12.00): "))

#introduction
print("\n\nBusiness Report")
print("######################")

#Printing the total number of jams they purchased
print("Strawberry Jam:", straw_jam, "Jars")
print("Blueberry Jam:", blue_jam, "Jars")
print("Orange Jam:", o_jam, "Jars")

#Finding how much each of the jams cost based on how much they purchased and how much was bought
#Formatted in currency format
straw_total = straw_jam * 9.20 #9.20 is the purchase price, etc.
blue_total = blue_jam * 10.80
o_total = o_jam * 12.00

#Printing the number of jam jars ordered and their totals
print("Charge for ", straw_jam, " jar(s) of Strawberry Jam is $", format(straw_total, ".2f"), sep = "")
print("Charge for ", blue_jam, " jar(s) of Strawberry Jam is $", format(blue_total, ".2f"), sep = "")
print("Charge for ", o_jam, " jar(s) of Strawberry Jam is $", format(o_total, ".2f"), sep = "")

#Finding the total amount to be charged and printing it using currency formatting
total_charge = (straw_jam * 9.20)+(blue_jam * 10.80)+(o_jam * 12.00)
print("The total charge for all types of jam is $", format(total_charge, ".2f"), sep = "")

#Calculating the amount of taxes to be charged (at a rate of 8.25%) 
taxes = total_charge * .0825
taxed_total = total_charge + taxes
print("The total charge for all types of jam plus tax is $", format(taxed_total, ".2f"), sep = "")

#conclusion
print("Thank you", name, "for your purchase! Please come again!")



