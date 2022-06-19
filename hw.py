class Ship:
    
    def __init__(self, name, price, passangers, capacity, sales):
        self.name = name
        self.price = price
        self.passangers = passangers
        self.capacity = capacity
        self.sales = sales
    
    def __str__(self):
        return f"-'{self.name}', {self.price} Euro p. P., {self.passangers} out of {self.capacity} passengers on board, total sales: {self.sales} Euro"
    
    def __repr__(self):
        return f"-'{self.name}', {self.price} Euro p. P., {self.passangers} out of {self.capacity} passengers on board, total sales: {self.sales} Euro"
    
    def check(self):
        return [self.price, self.passangers/self.capacity]
    
class Passenger:
    
    def __init__(self, full_name, birth_year, student):
        self.full_name = full_name
        self.birth_year = birth_year
        self.student = student
        
    def __str__(self):
        return f"-'{self.full_name}', {self.birth_year}, '{self.student}'"
    
    def __repr__(self):
        return f"-'{self.full_name}', {self.birth_year}, '{self.student}'"
    
class Menu:
    
    def __init__(self):
        self.data = list()
        self.ships = list()
        self.passengers = list()

    def add_ship(self, x):
        self.data.append(x.check())
        self.ships.append(x)
    
    def add_passenger(self, x):
        self.passengers.append(x)
    
    def manage_ship(self, cap_price, isavailable = True):
        if cap_price != None and isavailable == True:
            for i in self.data:
                if i[0] < cap_price and i[1] < 1:
                    return i
        if cap_price == None and isavailable == True:
            for i in self.data:
                if i[1] < 1:
                    return i
        if cap_price != None and isavailable == False:
            for i in self.data:
                if i[0] < cap_price:
                    return i  
        return "No ships are available"
        
    def __str__(self):
        return str(self.ships)
    
    def __repr__(self):
        return repr(self.ships)
 
M = Menu()
M.add_ship(Ship("Arielle", 5, 100, 100, 40))
M.add_ship(Ship("Nightmare", 10, 13, 150, 150))
M.add_passenger(Passenger("Nick", 1992, "Yes"))
M.manage_ship(cap_price = 12, isavailable = True)
M.ships
M.passengers
