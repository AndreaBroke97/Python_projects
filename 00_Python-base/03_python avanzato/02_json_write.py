#json e un formato di scrittura standardizzato con cui vengono scritti file esterni,
#può essere considerato come "grammatica universale" se dobbiamo fare parlare un applicativo python con un applicativo java etc
#json fa da ponte

'''
import json

data = "ciaooo guardmamiii"
with open('data.json ', 'w') as f:
    json.dump(data, f) #prendiamo la variabile data e la dumpiamo in un file json 
'''

###################################################################à
import json
#per farlo leggere come oggetto copiamo la classe e la mettiamo in json read
class Vehicle:
    def __init__(self, wheels, steering):
        self.wheels = wheels
        self.steering = steering 
        
x = Vehicle(4, "manubrio")

with open('data.json ', 'w') as f:
    json.dump(x.__dict__, f)
