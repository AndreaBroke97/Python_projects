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
        
    def __str__ (self):
        return f"id: {self.id}\n, name: {self.name}\n, height {self.height}\n, weight {self.weight}\n, types {self.types}\n, stats {self.stats}\n, "

    

class PokemonReader:
    def fetch_as_dict(self, name):
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
            response.raise_for_status()#controlla la risposta http dicendo se ha un errore
            #se c'è lancia un eccezione che viene catturata dall'except
            
            data = response.json()#salva i dati della risposta in un dizionario
            
            return {
                "id": data["id"],
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "types": [t["type"]["name"] for t in data["types"]],
                "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
            }
            
        except  requests.exceptions.Timeout:
            print("Error: TimeOut")
        except  requests.exceptions.ConnectionError:
            print("Error: Connection")
        except  requests.exceptions.HTTPError:
            print("Error: HTTP")
            
       

class JSONWriter:
    def save(self, data, path):
        os.makedirs(os.path.dirname(path), exist_ok = True)
        with open(path, "w") as f:
            json.dump(data, f, indent = 4)
    
        
        
  
class JSONReader:
    
    def load(self, path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print("File not found ERROR!")
        except json.JSONDecodeError:
            print("Error Decode!")
        except KeyError:
            print("Error The key doesn't")
                

name = input("enter the name or id of the pokemon: ")
reader = PokemonReader()

pokemon = reader.fetch_as_dict(name)
if pokemon is None:
    print("Failed to retrieve data.")
else:
    writer = JSONWriter()
    writer.save(pokemon, f"data/creatures/{name}.json")

    creature = Creature(**pokemon)

    print(creature)

    file = input("\ndo you want to reload the creature?: ")
    if file.lower() == "yes":
        reader2 = JSONReader()
        loaded = reader2.load(f"data/creatures/{name}.json")
        creature2 = Creature(**loaded)
        print(creature2)