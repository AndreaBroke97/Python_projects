''' #booleano
a = "ananas"
b = "Banana"


print(a > b)
'''

#<---------------------------------------------------->

#truthy e falsy values #PEP8
'''
a = 3 # questo e un truthy, non è un boleano ma viene convertito da python in boleano inserendolo nell'if

#if 3 < 5:
if a: #se "a" esiste truthy senò falsy
    print("3 is lower than 5")
    
#FALSY 0, NONE, NULL, EMPTY STRING, EMPTY COLLECTIONS
'''

###########################################################

'''
a = input("what do you thinking: ") 
#truthy diventa boleano se inserisco un messaggio e vero senò messaggio non valido cioè falso
if a:
    print(f"you have insert the current message:\n {a}")
else:
    print("message not valid")
'''

###########################################################

'''
shopping_list = []

if shopping_list:
    print(f"le cose da comprare sono: {shopping_list}")
else:
    print("the shopping list is vuota, nothing to visualizing")
'''

###########################################################

'''
a = int(input("insert age: "))


if(a < 18):
    print("user is underage")
elif(a < 30): #elif e una condizione a cascata che si attiva solo alla prima sarebbe un (else if)
    print("user is younger")
elif(a < 60):
    print("user is less young ")
else:
    print("user is old")
'''

###########################################################

'''
a = int(input("insert age: "))
#operatore ternario
if(a < 18):
    is_adult = False
else:
    is_adult = True


is_ad = False if a < 18 else True
'''

###########################################################



#ESERCIZIO
#fare inserire l'età all'utente. se è minorenne, stampa "accesso vietato"
#se è maggiorenne, eseguire un ulteriore controllo. se età è minore di 35, stampa "membro junior"
#se età compresa tra 35 e 50 stampa "membro mid"
#se età maggiore di 50 stampa "membro senior"
a = int(input("insert age: "))

if (a < 18):
    print("access denied")
else:
    if (a < 35):
        print("junior member")
    elif(a < 50):
        print("mid member")
    else:
        print("senior member")

