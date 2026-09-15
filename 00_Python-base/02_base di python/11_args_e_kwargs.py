'''
#*args  and **kwargs 
def product(*numbers):  #*numbers è un valore arbitrario di parametri posizionali che può leggere più parametri in product("ciao" , "carmelo") 
                        #prende tutti i parametri che passo e lli salva dentro una tupla 
    print(len(numbers))
    
product("ciao") #quindi con * due stringe le conta come due invece di contare le parole,
                           #senza * non può leggere più di due parametri ma uno solo definendo quante sono le lettere. 
                           #definendole con numeri: ad esempio CIAO = 
product("ciao", "carmelo")
product("ciao", "carpaccio", "dar")
product("ciao", "cartuccia", "sup", "deck")
'''

###############################################################

'''

#un * per poter inserire quanti parametri vogliamo, senò senza *possiamo inserirne solo uno
def product(*numbers):
    a = 1
    for el in numbers:
        a *= el
    return a

print(product(5))
print(product(4, 5))
print(product(3, 2, 7))
'''

###############################################################


def team( **document): #la base della lettura e scrittura di oggetti e file esterni = salvataggio che e un file di testo 
    print("The document include: ")
    print("role prevists: ", document.keys())
    print("a greater presentation: ")
    for role, name in document.items(): #questo doppio ciclo si usa con items
        print(role, name)
    
#team(founder = "Andrea")
#team(founder = "Andrea", Cofounder = "Luca")
team(founder = "Andrea", Cofounder = "Luca", ambassador = "Mirko")