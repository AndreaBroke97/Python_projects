import json

# mettendolo qui lo python trasforma come oggetto
class Vehicle:
    def __init__(self, wheels, steering):
        self.wheels = wheels
        self.steering = steering 
        
        
with open("data.json", "r") as f:
    value = json.load(f) # con questo andiamo a leggere cosa c'è in data.json
    


veicolo = Vehicle(**value)

print(type(veicolo))

print(veicolo.steering, veicolo.wheels)