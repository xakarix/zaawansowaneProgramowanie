class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (
            f"Area: {self.area}\n"
            f"Rooms: {self.rooms}\n"
            f"Price: {self.price}\n"
            f"Address: {self.address}\n"
        )


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + f"Plot: {self.plot}"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f"Floor: {self.floor}\n"


domek = House(300, 8, 1000000, "Wierzbowa 5, Katowice", 1200)
flat1 = Flat(80, 4, 700000, "Mikołowska 12, Katowice", 4)
print(domek, "\n")
print(flat1)
