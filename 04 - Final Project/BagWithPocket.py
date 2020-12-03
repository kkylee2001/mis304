
from Bag import Bag


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




