
#BLOCCO 1: SUPER CLASSE
'''
class Vehicle:
    
    def __init__(self, model, year):
        self.model = model
        self.year = year
        
    def accelerate(self):
        print(f"{self.model} is accelerating")
    def steering(self, angle):
        print(f"{self.model} he's steering at an {angle} of degrees")

#################################################################################s

#parte 1 
#c = Vehicle("Mazda", 2002)

#c.accelerated()
#c.steering(35)

#################################################################################

#BLOCCO 2: SOTTO CLASSE DELLA SUPER CLASSE
class Car(Vehicle): #class classname (superclass name)
    
    def __init__(self, model, year, doors = 5):
#KEYWORD super() è un richiamo alla super class e serve a fare un riferimento alla classe di sopra
        super().__init__(model, year)#apro il costruttore di veicolo
        #super() richiama il costruttore che si trova nella super classe
        super().accelerate()
        self.doors = doors

#################################################################################

#BLOCCO 3: SOTTO CLASSE DELLA SUPER CLASSE
class Motorcyle(Vehicle):
    def __init__(self, model, year, gear = "manual"):
        super().__init__(model, year)
        self.gear = gear

c1 = Car("Lamborghini", 2022, 2)
c2 = Car("BMW", 2023)
#RICHIAMIAMO I METODI DELLA SUPER CLASSE

c1.accelerate()
c2.steering(25)
'''
#OVERRIDING consiste el chiamare un metodo di una classe in una sotto classe
class Vehicle:
    
    def __init__(self, model, year):
        self.model = model
        self.year = year
        
    def accelerate(self):
        print(f"{self.model} is accelerating")
        
#BLOCCO 2: SOTTO CLASSE DELLA SUPER CLASSE
class Car(Vehicle): #class classname (superclass name)
    
    def __init__(self, model, year, doors = 5):

        super().__init__(model, year)
        super().accelerate()
        self.doors = doors
#questo e un override, sovrascriviamo il def accelerate della classe Vehicle ad ogni richiamo di Car come vediamo sotto
#funzionerà solo quello in questa sotto classe Car di Vehicle e quello di prima non lo vede.
    def accelerate(self): 
        print(f"{self.model} is accelerating, I remind you that it is a car with {self.doors} door ")
#ma non sparisce completamente, intanto sparisce def accelerate(self) della super classe vehicle solo per Car
#e poi se usiamo ex_accelerate e con la super() richiamiamo .accelerate() stiamo facendo il richiamo del
#def accelerate(self) della super classe Vehicle
    def ex_accelerate(self):
        super().accelerate()
        
c1 = Car("mazda", 2002)

c1.accelerate()
c1.ex_accelerate()