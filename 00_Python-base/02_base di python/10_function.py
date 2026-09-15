'''
def saluto(nome:string, int: age): #qui invece di bloccarsi visto che c'è una string e un int
    print(f"ciao, {nome}!")
    

print("qui start my program") 
saluto("Gianmaria", 20)
saluto("Franco", 50) 
saluto("Antonio", 29) 

saluto("carlo", 70) 
'''

##########################################################


def moltiplicazione(a, b, c = 5):
    if a == 3:
        return 2
    else:
        return a*b*c


print(moltiplicazione(3,2, 6)) # (3,2) sono degli argomenti posizionali che passiamo nei parametri e stanno prima dei keyword
print(moltiplicazione(a = 7, b = 5, c = 4)) # keyword argument che sta sempre all'ultimo
print(moltiplicazione(7,  c = 2, b = 3)) 

#all'interno della funzione possiamo avere anche più return in posizioni differenti, per tornare valori diversi