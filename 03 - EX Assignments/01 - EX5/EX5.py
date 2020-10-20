#Kyle Look Fong
#EX-5


                        #Instructions
#============================================================
#Create a list using [5..25], take each value and subtract 4 and replace it with the new value
#Print the values in the list, then print the list
#Output to a file
#Example Output:
#1,6,11,16,21,[1,6,11,16,21]



#============================================================
my_list = [5,10,15,20,25]   #Create list

with open('Output.txt','w') as output:  #Opening a File

    for i in range(len(my_list)): #Iterate over each item in the list
        my_list[i] -= 4     #Subtract 4 from each item at their respective index
        output.write(str(my_list[i]) + "\n") #Write the value at index
    output.write(str(my_list))  #Write entire list

#Don't need to close, used -- with open() as: 
