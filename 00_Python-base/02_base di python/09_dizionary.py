#a = ["gm", 27, "u"]

#nameprint(a[0], a[1], a[2])

d = {
    'key': 'value', 
    'name':'Andrea', 
    'age':27, 
    'gender':'man'}

'''
#print(type(d['nome'])) no
a = input("tell me what do you want to say of this type: ") # con questo facciamo un collegamento rendendolo dinamico
# e possiamo slezionare le key

print(d.get(a, 'key not found'))

#print(d.get('titolofstudy', 'key dont exist'))#di questo dizionario prendi, (mettiamo la chiave)
#se dobbiamo usare una chiave per il dizionario meglio scriverla così 
#il get se ha una chiave che non esiste non si interrompe
#print(f"nome: {d['nome']}, age: {d['age']}, gender: {d['gender']} ") #per accedere alle proprietà di (d)
'''
############################################################

'''
print(d.get("age", "key not found"))

if 'age' in d:
    print(d['age'])
    ###side effect
    
if not 'tifo' in d:
    d['tifo'] = 'Forza Catania'
else:
    print("nothing go to printed")
    ###side effect
    
print(d['tifo'])
'''

############################################################


d = {
    'key': 'value', 
    'name':'Andrea', 
    'age':27, 
    'gender':'man'}

print(len(d)) #quante coppie ha il valore (d) stampando la lunghezza cioè 4 di (d)
print(sorted(d))

for key in d.keys(): # questo stampa i valori
    print(key, d[key])

for value in d.values():
    print (key ,d[key])
    
gender = d.pop('gender')

d.popitem()


d.clear()


