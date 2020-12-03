from Bag import Bag
from BagWithPocket import BagWithPocket


def displayMenu():
    print("\n\nWelcome to the Bag Shop")
    print("==========================")
    print("x-print bag information")
    print('y-update number of pockets')
    print('z-buy bag\n\n')


def printBagInformation(list_of_bags):
    for bag in list_of_bags:
        print(bag)


def updatePockets(list_of_bags):
    pocket_updated = 0
    bag_found = 0
    id = input("\nPlease Enter the bag ID: ")
    for bag in list_of_bags:
        if id == bag.get_id():
            bag_found = 1
            if isinstance(bag, BagWithPocket):
                pocket_change = int(input("How many pockets: "))
                while pocket_change < 1 or pocket_change > 4:
                    print("It has to be between 1 and 4")
                    pocket_change = int(input("Please enter the number of pockets: "))
                bag.set_numPocket(pocket_change)
                pocket_updated = 1
                print(f"You have updated the {bag.get_color()} bag to have {pocket_change} pockets")
            break
    if bag_found == 0:
        print("The bag was not found; no update was conducted")
    elif bag_found == 1 and pocket_updated == 0:
        print("The bad does not have pockets; no update was conducted")


def buyBag(bag):
    num_buy = int(input("How many would you like to buy: "))
    if 0 < num_buy <= bag.get_inventory():
        current_inv = bag.get_inventory()
        new_inv = current_inv - num_buy
        bag.set_inventory(new_inv)
        print(f"You have purchased {num_buy} {bag.get_color()} bags")
    else:
        if num_buy < 0:
            print("It cannot be negative; no transaction is conducted")
        elif num_buy > bag.get_inventory():
            print("Insufficient inventory! No transaction was conducted!")



def main():
    bagWhite = Bag('B01', 10.00, 'white', 20)
    bagGreen = BagWithPocket('B02', 10.00, 'green', 20, 1, 2.99)
    bagPink = BagWithPocket('B03', 10.00, 'pink', 20, 2, 2.99)

    bag_list = [bagWhite, bagGreen, bagPink]

    enter_loop = ""

    while enter_loop.upper() != "NO":
        displayMenu()
        user_choice = input("Please select your choice: ").lower()
        if user_choice == "x":
            printBagInformation(bag_list)
        elif user_choice == "y":
            updatePockets(bag_list)
        elif user_choice == "z":
            buy_color = input("What color of bags do you want (white/green/pink): ").lower()
            while buy_color not in ('white', 'green', 'pink'):
                print("Invalid bag color, pick white/green/blue")
                buy_color = input("What color of bags do you want (white/green/pink): ").lower()
            if buy_color == 'white':
                buyBag(bagWhite)
            elif buy_color == 'green':
                buyBag(bagGreen)
            else:
                buyBag(bagPink)
        else:
            print("\nInvalid Choice!")
        enter_loop = input("\nType in 'yes' to start over and 'no' to quit: ")


main()