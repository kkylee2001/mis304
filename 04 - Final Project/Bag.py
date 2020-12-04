class Bag:
    def __init__(self, bag_id: str, price: float, color: str, inventory: int):
        self.__bag_id: str = bag_id
        self.__price = price
        self.__color = color
        self.__inventory = inventory

    def __str__(self):
        return f"\n\nBag ID is {self.get_id()}\n" \
               f"Color is {self.get_color()} \n" \
               f"Price is ${self.get_price()} \n" \
               f"Inventory is {self.get_inventory()}" \

    def set_id(self, x):
        self.__bag_id = x

    def set_price(self, x: float):
        if 0 < x < 40:
            self.__price = x
        else:
            print("Invalid Price")

    def set_color(self, x):
        self.__color = x

    def set_inventory(self, x):
        if x < 0:
            print("Error, inventory cannot be negative!")
        else:
            self.__inventory = x


    def get_id(self):
        return self.__bag_id

    def get_price(self):
        return format(self.__price, '.2f')

    def get_color(self):
        return self.__color

    def get_inventory(self):
        return self.__inventory



class BagWithPocket(Bag):
    def __init__(self, bag_id: str, price: float, color: str, inventory: int, numPocket: int, pricePocket: float):
        super().__init__(bag_id, price, color, inventory)
        self.__numPocket = numPocket
        self.__pricePocket = pricePocket

    def __str__(self):
        return f"{super().__str__()}" \
               f"\nNumber of pockets is {self.get_numPocket()}\n" \
               f"Price of pockets is ${self.get_pricePocket()} \n" \
               f"Total pocket price is ${self.calculate_pocketPrice()}"

    def calculate_pocketPrice(self):
        per_pocket_price = self.__pricePocket * self.__numPocket
        return format(per_pocket_price, '.2f')

    def set_numPocket(self, x):
        self.__numPocket = x

    def set_pricePcoket(self, x):
        if x >= 0:
            self.__pricePocket = x

    def get_numPocket(self):
        return self.__numPocket

    def get_pricePocket(self):
        return format(self.__pricePocket, '.2f')




