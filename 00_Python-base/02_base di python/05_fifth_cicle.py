'''
a = 0

while a < 11:
    print(a)
    a += 1
#   if (a==3): #possiamo anche usare un if con break per stoppare
        break
else: #si attiva solo se il ciclo termina uscendo dalla condizione diventando false ed else si può usare con while idem break
    print("cicle finished")
    
    #gli indici quando hai un'iterabile che partono da 0
    #i contatori la stessa cosa contatore =  variabile che conta da 0 e ogni volta conta 1
    # la variabile "a" parte da 0 e conta 1 con l'incremento
'''

######################################################################

'''
a = 0

while a < 11:
    a += 1
    if(a%2 != 0):
        continue #continue salta il resto del codice e torna all'inizio del ciclo
    print(a)
else:
    print("cicle finished")
    '''
    
######################################################################


fruits = ["fragola", "banana", "cocco"]

#for el in list
for el in fruits: #el sta per element e assume volta per volta per quell'elemento, 
                  #in realtà possiamo mettere ciò che vogliamo invece di el (è una variabile locale)
    print(el)

for i in range(10): #range e un oggetto speciale e un iterabile come se fosse una lista
    print(i+2)
    
print(range(10))

for i in range(len(fruits)): #len fruits e la lunghezza di fruits che sarebbe 3 ed il range(3) che fa 0,1,2 di cui "i" ne assumerà i valori
    print(f"element {i+1}: {fruits[i]}")
    

for i, el in enumerate(fruits): #enumerate da fragola, banana e cocco crea un array bidimensionale in colonna, 
                                #i il primo cicla sull'indice, el il secondo cicla sui valori
    print(f"element {i+1}: {el}")

    #range(10) #0 a 10
    #range(3,30) #3 a 30 ultimo escluso
    #range(3,30,5) #va da 3 a 30 a passi di 5