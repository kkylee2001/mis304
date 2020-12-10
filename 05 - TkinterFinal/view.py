from tkinter import *
from tkinter import messagebox
from Bag import *

class UI:
    def __init__(self):
        # instantiating bags
        white = Bag('B01', 10.00, 'white', 20)
        green = BagWithPocket('B02', 10.00, 'green', 20, 1, 2.99)
        pink = BagWithPocket('B03', 10.00, 'pink', 20, 2, 2.99)
        self.bags = [white, green, pink]

        # Instantiating the window
        window = Tk()
        window.config(padx=50, pady=50)

        # Making the menu and CTA
        menu = Label(text="Welcome to the\nBag Shop", font=("Arial", 30, "bold")).grid(row=0, column=1)
        cta = Label(text="What would you like to do?")
        cta.grid(row=1, column=1)
        cta.config(pady=20)

        # Making Each Button
        print_bags = self.options_button("Print Bags", self.print_pressed).grid(row=2, column=0)
        pocket_update = self.options_button("Update Pockets", self.update_pressed).grid(row=2, column=1)
        buy_bags = self.options_button("Buy Bags", self.purchase_pressed).grid(row=2, column=2)

        # Selecting the bag
        self.selector = Listbox(window, selectmode="single")
        for bag in self.bags:
            self.selector.insert(END, bag.get_color().title())
        self.selector.grid(row=4, column=1)

        # Specify the number either to update to or buy
        self.num_selected = Entry()
        sub_cta = Label(text="QTY:", justify=RIGHT)
        sub_cta.grid(row=3, column=0)
        sub_cta.config(pady=20)
        self.num_selected.grid(row=3, column=1)

        # Mainloop
        window.mainloop()

# TODO 2: Make view for each bag
    def options_button(self, name: str, func):
        button = Button(text=name, command=func)
        return button

# TODO 3: Make a message box when the user presses print
    def print_pressed(self):
        for bag in self.bags:
            text = bag.__str__()
            bag_message = messagebox.showinfo(title="Printing Bags", message = text)

#TODO 4: Method to get the number of bags and bag name
    def get_info(self):
        try:
            num_selected = int(self.num_selected.get())
        except ValueError as err:
            conversion_error = messagebox.showinfo(title="ERROR", message="Please input a number")
            return
        try:
            bag_selected = str(self.selector.get(self.selector.curselection()))
        except:
            getting_bag_error = messagebox.showinfo(title="ERROR", message="Please input a bag")
            return
        bag_picked: Bag
        for bag in self.bags:
            if bag.get_color().title() == bag_selected:
                bag_picked = bag
        return [bag_picked, num_selected]

# TODO 5: Button command for when the user presses update
    def update_pressed(self):
        try:
            info = self.get_info()
        except:
            return
        num = info[1]
        bag = info[0]
        if 0 < num <= 4:
            if isinstance(bag, BagWithPocket):
                bag.set_numPocket(num)
                success_msg = messagebox.showinfo(title="SUCCESS",
                                                  message=f"You have changed the {bag.get_color()} bag to have {bag.get_numPocket()} pockets ")
            else:
                no_pocket_error = messagebox.showinfo(title="ERROR", message="Choose a bag with pockets")
        else:
            invalid_pocket_amount = messagebox.showinfo(title="ERROR", message="Please input a number between 1 and 4")

# TODO 6: When the user presses on the buy button
    def purchase_pressed(self):
        try:
            info = self.get_info()
        except:
            return
        num = info[1]
        bag = info[0]
        if 0 < num < bag.get_inventory():
            curr_inv = bag.get_inventory()
            new_inv = curr_inv - num
            bag.set_inventory(new_inv)
            purchased = messagebox.showinfo(title="SUCCESS", message=f"You have purchased {num} {bag.get_color()} bags")
        else:
            insufficient_inventory = messagebox.showinfo(title="ERROR", message=f"Insufficient inventory, the {bag.get_color()} bag has {bag.get_inventory()} remaining")
