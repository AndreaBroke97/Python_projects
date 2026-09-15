import requests


#response = requests.get('https://httpbin.dev/delay/10', timeout = 3)


#se mettiamo timeout = stiamo definendo il tempo massimo della chiamata, se supera un tot di tempo da errore

#print(type(response))

#print(response.text) da un codice html/http
#print(response.status_code) #da un numero di errore

#################################################################################

'''
try:
    global response
    response = requests.get('https://httpbin.dev/delay/10', timeout = 15)
    
except requests.exceptions.ReadTimeout:
    print("catturato errore di TimeOut")
    
    
print(response.status_code)
'''

#################################################################################

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
#inviamo una chiamata https con get prendiamo la risposta in json 

print(response.json())