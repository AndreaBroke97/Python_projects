import os
import json
import requests

class Creature:
    def __init__ (self, **data_dict): 
        self.id = data_dict["id"]
        self.name = data_dict["name"]
        self.height = data_dict["height"]
        self.weight = data_dict["weight"]
        self.types = data_dict["types"]
        self.stats = data_dict["stats"]
        
    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "height": self.height,
                "weight": self.weight,
                "types": self.types,
                "stats": self.stats
                }
        
    def __str__(self):
        return f"POKEMONS | \nID: {self.id}, \nName: {self.name}, \nHeight: {self.height}, \nWeight: {self.weight}, \nTypes: {self.types}, \nStats: {self.stats}"


class PokemonReader:

    def fetch_as_dict(self, name):
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
            response.raise_for_status()
            data = response.json()
            return {
                "id": data["id"],
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "types": [item1["type"]["name"] for item1 in data["types"]],
                "stats": {item2["stat"]["name"]: item2["base_stat"] for item2 in data["stats"]}
            }
        except requests.exceptions.Timeout:
            print("Error! Time Out")
            
        except requests.exceptions.ConnectionError:
            print("Error! Connection failed")
            
        except requests.exceptions.HTTPError:
            print("Error! resource not found")

class JSONWriter:
    def save(self, data, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as file:
            json.dump(data, file)


class JSONReader:
    def load(self, path):
        try:
            with open(path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error! File not found")
        except json.JSONDecodeError:
            print("Error! json decode error")
        except KeyError:
            print("Error! Key error")


name = input("\nEnter a Name or ID: ") 

pokemon = PokemonReader().fetch_as_dict(name)
#entriamo nella classe per chiamare il metodoa

names = JSONWriter().save(pokemon, f"data/creatures/{name}.json")
#assegnamo un attributo a JSONWriter per salvare i dati in un percorso

creature = Creature(**pokemon)
#creiamo un istanza con ** che prende spacchetta un dizionario in keyword arguments

print(creature)

answer = input("\ndo you want to reload the creature: ")
if answer.strip().lower() == "yes":
    
    read = JSONReader().load(f"data/creatures/{name}.json")
    #assegnamo variabile per rileggere i dati della creatura potendola ristampare
    creature2 = Creature(**read)# e con **read prendiamo la lettura json spacchettandolo
    print(creature2)
    