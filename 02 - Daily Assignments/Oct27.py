#Program 2
string = "Mary had a little lamb little lamb little lamb"

string_list = string.split()

lamb_count = 0
for word in string_list:
    if word == "lamb":
        lamb_count += 1

print("The word 'lamb' was found in the string", 
    lamb_count, "times")


#Program 1
number = input("Input a number: ")
if number.isdigit():
    print("Is a digit!", int(number) + 3)
else:
    print("Not a number")
