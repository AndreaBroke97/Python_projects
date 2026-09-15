#EXERCISE 1: condivided attribute
'''
class Vehicle:
    type = "Car"
    
    def __init__(self, model):
        self.model = model
        
#creiamo due oggetti
v1 = Vehicle("Ferrari")#modifichiamo i due modelli del costruttore
v2 = Vehicle("Toyota")

#stampo entrambi i type degli oggetti v1, v2
print(v1.type) #stampa "Car"
print(v2.type) #stampa "Car"

#modifico il type della classe da "Car" a "Truck"
Vehicle.type = "Truck"

#stamp dinuovo i type v1, v2 in più la modifica, Vehicle.type
print(v1.type)      # "Truck"
print(v2.type)      # "Truck"
print(Vehicle.type) # "Truck"
'''

##########################################################################################à

#EXERCISE 2: accidental Shadowing (istance attribute) shadowing accidentale: 
'''
#mascheri l'attributo di classe perchè l'attributo di istanza lo va quasi a coprire chiamandolo con lo stesso nome
class Vehicle:
    type = "Car"
    
    def __init__(self, model):
        self.model = model
        
#creiamo due oggetti
v1 = Vehicle("Mazda")#modifichiamo i due modelli del costruttore
v2 = Vehicle("Toyota")

v1.type = "Pippo"
v2.type = "ciao"
#stampo entrambi i type degli oggetti v1, v2
print(v1.type) #stampa "Car"
print(v2.type) #stampa "Car"

#modifico il type della classe da "Car" a "Truck"
Vehicle.type = "Truck"

#stamp dinuovo i type v1, v2 in più la modifica, Vehicle.type
print(v1.type)      # "Truck"
print(v2.type)      # "Truck"
print(Vehicle.type) # "Truck"

print(v1.__dict__) #stampa tot di valori che hanno chiave(nome dell'attributo) e il valore dell'attributo 
print(v2.__dict__) #dict sta per dictionary
print(Vehicle.__dict__)
'''

##########################################################################################

#EXERCISE 3: parametric costructor
'''
class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        print(f"Student {self.name} created!") #segnaliamo la creazione dell'oggetto
    
s1 = Student("Andrea", 7)
s2 = Student("Filippo", 9)
'''

##########################################################################################

#EXERCISE 4: dinamic attributes
'''
class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        print(f"Student {self.name} Created!")
        
        
s1 = Student("Andrea", 9)
s1.age = 20 #aggiungiamo manualmente un attributo age

s2.age #provi ad accedere da un altro oggetto
'''

##########################################################################################

#EXERCISE 5: __str__ (sta per string serve per usare le stringhe ''' condizione ''')
'''
class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        
    def __str__(self):
        
        a = f''' #Student:{self.name} {self.grade}#'''
        #return a
        
        
#s1 = Student("Andrea", 9)
#s2 = Student("Alice", 28)

#print(s2)

##########################################################################################

#EXERCISE 6: __eq__ (sta per equal, confrontiamo i riferimenti in memoria)
'''
class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        
    def __str__(self):
        
        a = f''' #Student:{self.name} {self.grade}#'''
        #return a
'''
    def __eq__(self, other):
        if isinstance(other, Student): #s2 è uno student? si
        #isistance controlla se l'oggetto appartiene a una specifica classe
        #tradotto è (other è un'istanza di Student?) e restituisce True o False
            return self.name == other.name and self.grade == other.grade
        # "Andrea" == "Andrea"  →  True
        # quindi restituisce True
        else:
            return False
        
        
s1 = Student("Andrea", 9)
s2 = Student("Andrea", 9)

print(s1 == s2)
'''

##########################################################################################

#EXERCISE 7: __len__ (sta per lenght, decidiamo cosa "contare" per un determinato oggetto, es in delle liste o una class Playlist)
'''
class Course:
    
    def __init__(self, name, students, course):
        self.name = name.strip().capitalize()
        self.course = course.strip().capitalize()
        self.students = students
    
    
    def __len__(self):
        return len(self.students)
    
sds1 = Course("course 41", ["Andrea", "Marco", "Giulio", "Carlo", "Carmelo", "Filippo"], "Web developer")

print(sds1.name)
print(sds1.students)
print(sds1.course)
print(len(sds1))
'''

##########################################################################################

#EXERCISE 8: __add__ (sta per aggiunta, è chiamato automaticamente quando si fa una somma + tra due oggetti (s1 + s2))
'''
class Course:
    
    def __init__(self, name, students, course):
        self.name = name.strip().capitalize()
        self.course = course.strip().capitalize()
        self.students = students
    
    
    def __len__(self):
        return len(self.students)
    
    def __add__(self, other):
        if isinstance(other, Course):
            newcourse = self.students + other.students #unisce due liste in una sola
            return Course("nome", newcourse, "course") #crea e restituisce un nuovo oggetto Course con la lista unita
        else:
            print("Sum impossible")
            return None
    
sds1 = Course("course 41", ["Andrea", "Marco", "Giulio", "Carlo", "Carmelo", "Filippo"], "Web developer")
sds2 = Course("course 46", ["Luca", "Serena"], "CyberSecurity")

sds3 = sds1 + sds2

print(sds3.students)
print(len(sds3))
'''

##########################################################################################

#EXERCISE 9: dir() (mostra tutto: attributi miei + netidu nagucu ereditati da python) e __dict__ è il dizionario interno degli attributi dell'istanza. mostra: ['name', '_Person__age'] → si vede il name mangling applicato)
#Istanziare significa creare un oggetto concreto a partire da una classe.
#La classe è lo schema (il progetto), l'istanza è l'oggetto reale creato da quello schema
'''
class Course:
    
    def __init__(self, name, students, course):
        self.name = name.strip().capitalize()
        self.course = course.strip().capitalize()
        self.students = students
    
    
    def __len__(self):
        return len(self.students)
    
    def __add__(self, other):
        if isinstance(other, Course):
            newcourse = self.students + other.students #unisce due liste in una sola
            return Course("nome", newcourse, "course") #crea e restituisce un nuovo oggetto Course con la lista unita
        else:
            print("Sum impossible")
            return None
    
sds1 = Course("course 41", ["Andrea", "Marco"], "Web developer")
#sds2 = Course("course 46", ["Luca", "Serena"], "CyberSecurity")

#sds3 = sds1 + sds2

print(dir(sds1))  #lista di tutto: metodi magici + attributi tuoi
print(sds1.__dict__)    # dizionario solo con gli attributi dell'istanza sds1
print(Course.__dict__)  # attributi e metodi definiti nella classe Course
#dizionario con quello che sta DENTRO LA CLASSE (__init__, __len__, __add__)

#print(sds3.students)
#print(len(sds3))
'''

##########################################################################################

#EXERCISE 10: isinstance (controlla se uno specifico oggetto si trova in quella classe e restituisce True o False)
'''
class Vehicle:
    
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        
        
class Car(Vehicle):

    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed) #Richiama il costruttore di Vehicle
#super() serve a dire "chiama il costruttore della classe madre" così non riscriviamo gli attributi da 0 cioè (brand, speed)
        self.fuel_type = fuel_type #Aggiunge il suo attributo
    
            
            
c1 = Car("Ferrari", 320, "Gasoline")

if isinstance(c1, Vehicle):
    print("c1 is a vehicle")
else:
    print("c1 is not a vehicle")
'''

##########################################################################################

#EXERCISE 11: attributes control
'''
class person:
        
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = person("Andrea", 19)#istanza

def check(object, attribute):#funzione passiamo nei parametri con nomi a piacere un oggetto e l'attributo da cercare per hasattr
    if hasattr(object, attribute) == True: #questo oggetto ha questi attributi? si == True quindi stampa
        print("Has attribute X")
    else:
        print("Missing attribute X")
        
check(p1, "name" )
check(p1, "no" )
'''
    
##########################################################################################

#EXERCISE 12: dinamic access
'''
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"Name: {self.name}, \nAge: {self.age}\n"
    

p1 = person(andrea, 19)

print(getattr(p1, "age"))
'''

##########################################################################################

#EXERCISE 13: dinamic creation
'''
class person:
    
    def __init__(self, name):
        self.name = name
   
        
p1 = person("Andrea")
setattr(p1, "age", 19)

print(p1.__dict__)
'''

##########################################################################################

#EXERCISE 14: dinamic metod
'''
class person:
    def hello(self):
        print("surprise motherfucker")
        
p1 = person()
p1.hello()
'''

##########################################################################################

#EXERCISE 15: private attributes
'''
class Account:
    def __init__(self):
        self.__balance = 0
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
        
acc = Account()
acc.deposit(500)
print(acc.get_balance())
'''

##########################################################################################

#EXERCISE 16: access negated
'''
class Account:
    def __init__(self):
        self.__balance = 0 #name mangling __balance python lo trasforma in _Account__balance
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
        
acc = Account()
#acc.deposit(500)
#acc.get_balance()

print(acc.__balance)
print(acc._Account__balance)
'''

##########################################################################################

#EXERCISE 17: private metod
'''
class Account:

    def __log_transaction(self):
        print("log effectuated | MAY 19/05/2026")
        
    def call(self):
        self.__log_transaction()
        
acc = Account()

acc.call()
'''

##########################################################################################

#EXERCISE 18: base gerarchy
'''
class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        
    def describe(self):
        print(f"{self.model} - {self.year}")

class Car(Vehicle):
    def __init__(self, model, year, doors):
        super().__init__(model, year)
        self.doors = doors
        

car = Car("Ferrari", 2020, 2)

car.describe()
'''
##########################################################################################

#EXERCISE 19: override
'''
class Vehicle:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        
    def describe(self):
        print(f"{self.model} - {self.year}")

class Car(Vehicle):
    def __init__(self, model, year, doors):
        super().__init__(model, year)
        self.doors = doors
    
    def describe(self):#OVERRIDE
        print(f"{self.model} - {self.year} - Doors: {self.doors}")
        

car = Car("Ferrari", 2020, 2)

car.describe()
'''

##########################################################################################

#EXERCISE 20: multilevel gerarchy
'''
class Vehicle:
    def __init__(self, model, year, doors):
        self.model = model
        self.year = year
        self.doors = doors
        
    def describe(self):#OVERRIDE
        print(f"Model: {self.model}")

    
    
class Car(Vehicle):

    def __init__(self, model, year, doors):
        super().__init__(model, year, doors)
    def describe(self):#OVERRIDE
        print(f"Model: {self.model} - Year: {self.year}")


class ElectrictCar(Car):
    
    def __init__(self, model, year, doors):
        super().__init__(model, year, doors)
    def describe(self):#OVERRIDE
        print(f"Model: {self.model} - Year: {self.year} - Doors: {self.doors}")

car1 = Vehicle("Ferrari", 2020, 2)
car2 = Car("Panda", 2010, 4)
car3 = ElectrictCar("Mamba", 2015, 2)

car1.describe()
car2.describe()
car3.describe()
'''

##########################################################################################

#EXERCISE 21: metods conflict
'''
class Flyer:
    def fly(self):
        print("ciao sono flyer")

class Swimmer:
    def fly(self):
        print("suca sei swimmer")

    
class Duck(Flyer, Swimmer):
    def __init__(self):
        pass
    #def fly(self):
        #print("ciao sono flyer swimmer")
    

sd = Flyer()
sd2 = Swimmer()
sd3 = Duck()
sd.fly()
sd2.fly()
sd3.fly()

print(Duck.__mro__)
'''

##########################################################################################

#EXERCISE 22: Analysis MRO
'''
class Flyer:
    def fly(self):
        print("ciao sono flyer")

class Swimmer:
    def fly(self):
        print("suca sei swimmer")

    
class Duck(Swimmer, Flyer):
    def __init__(self):
        pass
    #def fly(self):
        #print("ciao sono flyer swimmer")
    

sd = Flyer()
sd2 = Swimmer()
sd3 = Duck()
sd.fly()
sd2.fly()
sd3.fly()

print(Duck.__mro__)
'''

##########################################################################################

#EXERCISE 23: Classic polymorfism
'''
class Car:
    def __init__(self, car):
        self.car = car
    
    def steer(self):
        print(f"\nthe {self.car} is stering")
    
class Motorcycle:
    def __init__(self, bike):
        self.bike = bike
    
    def steer(self):
        print(f"the {self.bike} is stering\n")

vehicle1 = Car("Ferrari")
vehicle2 = Motorcycle("Kawasaki")

vhc = [vehicle1, vehicle2]

for vehicle in vhc:
    vehicle.steer()
'''

##########################################################################################

#EXERCISE 24: Dynamic dispatch
'''
class Dispatch:
    def action(self):
        print("\nact in dispatch")
        
class Prove:
    def action(self):
        print("act in prove\n")

a = Dispatch()
b = Prove()

a.action()
b.action()
'''

##########################################################################################

#EXERCISE 25: Steering system
'''
class CarSteering:
    def engage_steering(self):
        print("sono in car stering")
    
class BikeSteering:
    def engage_steering(self):
        print("sono in Bike stering")
    
    
class Vehicle:
    def __init__(self, steering):
        self.steering = steering
        
    def engage_steering(self):
        self.steering.engage_steering()


cs = CarSteering()
bs = BikeSteering()
vh = Vehicle(cs)

vh.engage_steering()
'''       

##########################################################################################

#EXERCISE 26: Sostitution at runtime
'''  
class CarSteering:
    def engage_steering(self):
        print("sono in car stering")
    
class BikeSteering:
    def engage_steering(self):
        print("sono in Bike stering")
    
    
class Vehicle:
    def __init__(self, steering):
        self.steering = steering
        
    def engage_steering(self):
        self.steering.engage_steering()


cs = CarSteering()
bs = BikeSteering()
vh = Vehicle(cs) #richiamo la variabile cs

vh.steering = bs #sostituiamo l'oggetto

vh.engage_steering() #stampa senza __str__
'''  

##########################################################################################

#EXERCISE 27: Pure function
'''
def market(money):
    return [n for n in money if n % 2 == 0]

print(market([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
'''

##########################################################################################

#EXERCISE 28: Impure function
'''
def market(money):
    money.append(99)
    print(f"Lista modificata: {money}")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
market(lista)
print(f"Lista originale dopo la chiamata: {lista}")
'''

##########################################################################################

#EXERCISE 29: Triple implementation

def listss(procedure):
        return [n for n in procedure if n > 10]

class OOP:
    def listss(self, procedure):
        return [n for n in procedure if n > 10]
    
elist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]
functional = list((filter(lambda x: x > 10, elist)))
print(functional)

print(listss(elist))

op = OOP()
print(op.listss(elist))

