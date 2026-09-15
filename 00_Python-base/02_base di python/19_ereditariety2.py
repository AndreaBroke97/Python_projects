#BLOCCO 1
'''
class Vehicle:
 #DUE CLASSI INDIPENDENTI
    def accelerate(self):
        print("the vehicle is accelerating")

class Car:
    def accelerate(self):
        print("the car is accelerating")
        
#POLIMORFISMO
#questa SuperCar e figlia di Vehicle e Car prendendo tutti gli attributi di entrambe le classi
#ma ci sta un problema, entrambi le classi hanno lo stesso metodo
class SuperCar(Vehicle, Car): #in questo caso nei parametri abbiamo Vehicle
    color = "red"
#quindi cosa stamperà? tra questi?, ovviamente Vehicle perchè prende da sinistra verso destra
#prima cerca il metodo nella prima classe Vehicle, se non lo trova scorre alla prossima
bugatti = SuperCar()

bugatti.accelerate()
'''

################################################################################

#BLOCCO 2
#DYNAMIC DISPATCH

class Car:
    def accelerate(self):
        print("the car accelerate with the pedal")
        #op1

class Motorcicle:
    def accelerate(self):
        print("the Motorcicle accelerate with knob(manopola)")
        #op2


class Bike:
    def accelerate(self):
        print("the bike accelerate with pushing")
        #op3


#ASSEGNAZIONE DINAMICA (DYNAMIC DISPATCH) il metodo accelerate esiste in classi differenti
#quando faccio el.accelerate, faccio agire questa linea di codice dando in input elementi appartenenti
#a classi differenti ma che avranno poi la stessa firma.
#sto rendendo il programma flessibile con un miglior design

list = []

c1 = Car()

list.append(c1)

m1 = Motorcicle()

list.append(m1)

b1 = Bike()

list.append(b1)

print(list)

#el sta per element
for el in list:
    el.accelerate() #!!!!!!!!!!!!!!!!