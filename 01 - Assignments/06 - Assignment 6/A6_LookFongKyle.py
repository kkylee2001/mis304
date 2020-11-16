#Name: Kyle Look Fong
#Assignment Number: 6
#Date: 10/28/2020
#Secton: 12:30PM-2:00PM
#Description: A program to help Mr. List append a new student's age to the list,
#find the oldest student in his classm and count the number of times 
#a specific word appears in the string list

                        #Functions Init
#================================================================
def display_menu():
    #1. Print a menu
    print("\n\nWelcome to the list program!")
    print("============================")
    print("A or a: Append to age list")
    print("M or m: Find (M)aximum age")
    print("C or c: Count a specific word\n\n")


def get_choice():
    #A. Display_Menu Variable Init
    choice_selected: str = ""

    #1. Call the display_menu function to print menu
    display_menu()

    #2. Prompt for the choice and return the choice to main
    choice_selected = input("Enter your choice: ")
    return choice_selected

def max_age(age_list): #Parameters: the list with ages
    #A. Max_Age Variable Init
    maximum_age = 0

    #1. Use a built in function to retrieve the largest number and store it
    maximum_age = max(age_list)

    #2. Output the maximum age, NOT return
    print("Maximum age:", maximum_age)


                        #Start of Program
#================================================================
def main():
    #A-a. Main Function Variable Init
    enter_loop: str = "YES"      #ONLY check for "YES", per instructions
    choice: str = ""
    add_age: float = 0
    target_word: str = ""
    word_counter: int = 0

    #1. Declare a string list and a floating point list
    string_list: [str] = ["Long", "long", "ago", "in", "a", "far", "far",
                 "away", "college", "there", "were", "ten", "students"]
    number_list: [float] = [17.5,18,18.2,19,20,18.5,17,19.9,20.3,21]

    #2. Use a while loop to display the menu and process the choices -- YES
    while enter_loop == "YES":
        try: #try except block to handle all errors
            #A-b. Main Function Variable Init
                #This needs to be reinitialized with every while loop iteration
            word_counter: int = 0

            #3. call the get choice function and return value to main
            choice = get_choice()

            #4. Use if-elif-else structure to process each choice and output 
            #error if invalid
            if choice in ["A", "a"]:
                #5A. Prompt for the age to add, make sure age is within 17-60
                #do not use a validation loop. Append to list, if it is successful 
                #output a message and the updated list, or an error message
                try: #Will continue if the input is a number
                    add_age = float(input("Age to add: "))
                    if 17 <= add_age <= 60:
                        number_list.append(add_age) #appending to the list
                        print("The age is added to the list") 
                        print("The new list is:", str(number_list), "\n")
                    else: #If the input is not a number
                        print("The age you have entered is out of range, no age is added\n")
                except:
                    print("You need to enter a number, no number is added\n")
                
            elif choice in ["M", "m"]:
                #5M. Select the oldest student on the list. Call max_age
                max_age(age_list=number_list)

            elif choice in ["C", "c"]:
                #5C. Prompt for the target word, case sensitive. Use a for loop
                #with the len function for the condition
                #compare the target word with each of the elements
                #counter if the word is found
                target_word = input("Target Word: ") #prompt for word

                for i in range(len(string_list)): #for every word-index in the list
                    if string_list[i] == target_word: #if the word at the index is equal to the target word
                        word_counter += 1 #add to accumulator

                if word_counter != 0: #if it's not 0
                    print(target_word, "has appeared", str(word_counter), "times\n")
                                                        #Don't need to do format(,'.0f') b/c it's an int
                                                        
                else: #if it's zero
                    print("The target word was not found!\n")

            else: #if not A,a, M,m, C,c
                print("Invalid Choice!\n")

            enter_loop = input("Repeat (YES to repeat): ") #repeat while loop




        except Exception as err: #If an error is raised
            print("ERROR:", err)
            enter_loop = input("Repeat (YES to repeat): ") #repeat while loop

    #END OF LOOP
    print("This is the end of the program")


#Calling Main    
main()