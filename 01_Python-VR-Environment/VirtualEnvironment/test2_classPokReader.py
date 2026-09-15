import os
import json
import requests

class PokemonReader:
    def featch_as_dict(self, name):
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
            response.raise_for_status() #lancia eccezzioni per errori HTTP
            data = response.json() #variabile response che avremo in JSON
            return {
                "id": data["id"],
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "types": [item["type"]["name"] for item in data["types"]],
                "stats": {item2["stat"]["name"]: item2["base_stat"] for item2 in data["stats"]}
            }
        
        except requests.exceptions.Timeout:
            print("Error! Time Out")
            
        except requests.exceptions.ConnectionError:
            print("Error! Connection failed")
            
        except requests.exceptions.HTTPError:
            print("Error! resource not found")
            
poki = PokemonReader()

print(poki.featch_as_dict("pikachu"))
            
