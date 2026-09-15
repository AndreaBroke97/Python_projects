'''
#List comprehension
a = []
for i in range(100):
    a.append(i*3)
print(a)

l = [i*3 for i in range(100)]
print(l) 

# l = [a for b in c if b] e la sintassi per questo tipo di lista 
'''

#<---------------------------------------------------->

'''
#Booleano
l = [] 
for i in range(20):
    if(i % 2 == 0):
        l.append(i) #se la condizione e vera appene i * 3, senò falso
print(l)    #in questo caso appendiamo i nell'array

12 = [i for i in range(20) if i % 2 == 0]

13 = [i*2 for i in range(11)]

print(12)
print(13)
'''

#<---------------------------------------------------->

'''
s = "ciao come stai, sono andrea ho rubato un camion e lorenzo e un pollo"

s2 = s.split() #split mette in una lista quello che abbiamo scritto prima richiamando la variabile s

print(s2)

lw = [len(i) for i in s2] #per ciascuna parola devo calcolare la lunghezza usando for i in s2
#LW = lenght word
cw = [i.capitalize() for i in s2] 

ow = ["p" if len(i) % 2 == 0 else "d" for i in s2 if not i.isalpha()]
# e stato inserito un operatore ternario al posto di a: "p" if len(i) % 2 == 0 else "d" ed è un valore dinamico
# in questo modo lavora

print(lw)
print(cw)
print(ow)
'''

#<---------------------------------------------------->

'''
#E UNO SWITCH
command = input("insert a command: ")

match command:
    case "start":
        print("the programm are inizializating")
    case "stop":
        print("the programm going to finish")
    case "help":
        print("the programm is bugged")
    case _:
        print("Error 404")
'''