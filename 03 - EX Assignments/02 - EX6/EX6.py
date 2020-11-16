#Kyle Look Fong
#EX6
#Slide 11 - Dictionaries
##################################

#1. Declare an empty dictionary and call it dwarf_contact
dwarf_contact: {str:str} = {}


#2. Put in three pairs of data
dwarf_contact.update({
    "Grumpy": '111-2222',
    "Happy": '222-3333',
    "Sleepy": '333-4444'
})

#3. Only output Sleepy's phone number
print("Sleepy:", dwarf_contact["Sleepy"])


#4. Add Sneezy's to the dictionary
dwarf_contact.update( {"Sneezy": '555-5555'} )


#5. Output all values using the items() function
for item in dwarf_contact.items():
    print(item)


#6. Change Sneezy's phone number to 444-5555
dwarf_contact["Sneezy"] = '444-5555'


#7. Delete Grumpy from the Dictionary
dwarf_contact.pop("Grumpy")


#8. Print Dictionary
print(dwarf_contact)