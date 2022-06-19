class Transport:
    
    def __init__(self, date, work_time):
        self.date = date
        self.work_time = work_time
        
    def check_transport(self):
        if self.date + self.work_time > 2022:
            return True
        return False
    
    def get_type(self):
        return 0
    
class Auto(Transport):
    
    def __init__(self, date, work_time, capacity, color):
        super().__init__(date, work_time)
        self.capacity = capacity
        self.color = color
        
    def bibi(self):
        print("Bibi nahuy idi!")
        
    def get_type(self):
        return 1
    
    def __str__(self):
        return f"Auto {self.date}, {self.work_time}, {self.capacity}, '{self.color}'"
    
    def __repr__(self):
        return f"Auto({self.date}, {self.work_time}, {self.capacity}, '{self.color}')"
        
class Bus(Auto):
    
    def __init__(self, date, work_time, capacity, color):
        super().__init__(date, work_time, capacity, color)
    
    def proezd(self):
        print("wake up bomzhara, peredaem za proezd!")
        
    def get_type(self):
        return 2
    
    def __str__(self):
        return f"Bus {self.date}, {self.work_time}, {self.capacity}, '{self.color}'"
    
    def __repr__(self):
        return f"Bus({self.date}, {self.work_time}, {self.capacity}, '{self.color}')"
        
class Plane(Transport):
    
    def __init__(self, date, work_time, capacity, speed):
        super().__init__(date, work_time)
        self.capacity = capacity
        self.speed = speed
        
    def Upast_nah(self):
        print("Upal")
        
    def get_type(self):
        return 3
    
    def __str__(self):
        return f"Plane {self.date}, {self.work_time}, {self.capacity}, {self.speed}"
    
    def __repr__(self):
        return f"Plane({self.date}, {self.work_time}, {self.capacity}, {self.speed})"
    
class Base(Transport):
    
    def __init__(self):
        self.data = list()
    
    def check_transport(self):
        for i in self.data:
            print(i.check_transport())
    
    def add_transport(self, x):
        self.data.append(x)
    
    def __str__(self):
        return str(self.data) + ' sosi'
    
    def __repr__(self):
        return repr(self.data)
        
B = Base()

B.add_transport(Bus(2020, 5, 33, "Orange"))
B.add_transport(Plane(2018, 5, 100, 600))
B.add_transport(Auto(2016, 4, 4, "Purple"))

B.check_transport()

B.data 
