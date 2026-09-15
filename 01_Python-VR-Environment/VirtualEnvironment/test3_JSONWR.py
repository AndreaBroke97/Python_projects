import os
import json
import requests

class JSONWriter:
    def save(self, data, path):
        os.makedirs(os.path.dirname(path), exist_ok = True)
#os.makedirs crea una cartella inesistente
#os.path.dirname(path) estrae la cartella dal percorso ES: "data/pokemon.json"
#exist_ok = True non lancia errori se esiste già
        with open(path, "w") as file:
#with open apre il file in scrittura con "w" se non esiste lo crea senò lo sovrascrive
#with chiude il file automaticamente alla fine
            json.dump(data, file)
#scrive data nel file in formato JSON

class JSONReader:
    def load(self, path):
        try:
            with open(path, "r") as file:
                return json.load(file)
#return json.load(file) legge il file JSON e lo converte in un dizionario python
#che viene restituito con return
        except FileNotFoundError:
            print("Error! File not found")
        except json.JSONDecodeError:
            print("Error! json decode error")
        except KeyError:
            print("Error! Key error")
        
        
ejson = JSONWriter()
print (ejson)
