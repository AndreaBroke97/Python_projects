import os
import json
import requests

class Creature:
    def __init__(self, **data_dict): #** raccoglie tutti gli elementi in un dizionario
        self.id = data_dict["id"]
        self.name = data_dict["name"]
        self.height = data_dict["height"]
        self.weight = data_dict["weight"]
        self.types = data_dict["types"]
        self.stats = data_dict["stats"]
    
    def to_dict(self): #serve per inviare dati a un'API o salvare su file JSON
        return {"id": self.id,
                "name": self.name,
                "height": self.height,
                "weight": self.weight,
                "types": self.types,
                "stats": self.stats
                }
        
    def __str__(self):
        return f"POKEMONS | \nID: {self.id}, \nName: {self.name}, \nHeight: {self.height}, \nWeight: {self.weight}, \nTypes: {self.types}, \nStats: {self.stats}"
        
creature = Creature(id = 20, name = "Pikachu", height = "120 cm", weight = "60cm", types = "electric", stats = "healer")
print(creature)
        