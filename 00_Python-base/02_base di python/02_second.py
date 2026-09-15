'''
a = 4

b = 5

c = a + b
print(c)


s1 = "ci vediamo "

s2 = " a pasqua"
#print(s1 + s2) stampa entrambi
print(s1 *3 ) #stampa s1 per 3 volte

PI = 3.14
'''

#<---------------------------------------------------->
'''
#formatted string fstring
nome = "Andrea"
#print("ciao, io mi chiamo", nome, "e amo questo corso")


#invece di avere tanti pezzi, usare un unica stringa per inserire la variabile
print(f"Ciao,io mi chiamo {nome} e amo questo corso")
#la f dice di far vedere la variabile che abbiamo inserito
'''

#<---------------------------------------------------->

'''
nome = "Andrea"
age = 19
is_funny = True
print(type(nome), type(age), type(is_funny))
#questo stampa il tipo di attributo che abbiamo messo 
'''

#<---------------------------------------------------->
#iterabili
#un array che sarebbe una lista in cui possiamo inserire la qualsiasi cosa
'''
a = [1, 5.4, False, "margherita", [1,2,3]]

print(a)
print(type(a))
'''
#la lista si definisce con le [ ] ed è mutabile
'''
a =[ ["Andrea", 32], ["Margherita", 25], ["Mirko", 27], ["Papauta"]]

print (a[3])
print(a[3][0])



a[0] = "Andrix"

print(a[0])

#tuple si definisce con le tonde ed è immutabile ed è buona prassi far si che l'output e una tupla per non poterlo cambiare

b = (0,1,"Andrea", False)

#print(b[2])

print(type(b)) #tupla immutabile se vogliamo cambiarla possiamo duplicarla 
               #in una lista creandone una copia e possiamo manipolarla
c = list(b)
print(type(c))
'''

#<---------------------------------------------------->
'''
a = 5
b = a
b = 6

print(a , b)

###########################################################à

c = ["anna", "carlo"]
d = c
#quando usiamo l'operatore di assegnazione su un iterabile verrà copiato 
# l'indirizzo e stiamo modificando l'elementro di partenza perchè 
# stanno puntando nello stesso indirizzo di memoria

#per creare un duplicato indipendente
e = c.copy()

d[0] = "pippo"

print(c)
print(d)
print(e)
'''

#<---------------------------------------------------->

frutti = ["ananas", "banana", "cocco", "datteri", "nonLoSo"]
#operazione di slicing
#print(frutti[1:3]) #dall'elemento 1 fino all'elemento dell'indice 3 ma l'ultimo indice viene sempre escluso quindi dando il 2
#se non specifichiamo niente tipo 2: dall'elemento dell'indice 2 fino alla fine
'''
print(frutti[1:3])

print(frutti[1:])

print(frutti[:3]) #dalla un elemento iniziale fino alla fine segnata cioè 3
'''

#possiamo usare anche indici negativi

#print(frutti[-1]) #sta dietro lo 0 e incomincia al contrario quindi da [non lo so]
'''
a = "ananas" in frutti #l'output sarà true o false ananas e in frutti? si, melacaco? no

b = "melacaco" in frutti

print(a)
print(b)
'''

#<---------------------------------------------------->

'''
frutti.append("fragola") #append aggiunge alla lista
print(frutti)

print(len(frutti)) #len indica la lunghezza della lista

a = frutti.pop() #rimuove l'ultimo elemento di frutti però lo salva in a
frutti.pop()
print(a)
print(frutti)

b = frutti.pop(2)  #pop lo elimina dall'iterabile e quando lo cancella lo restituisce 
print(frutti)      #come output e possiamo usarlo, assegnandolo a qualcosa o printandolo
print()

#altro metodo CLEAR
frutti.clear
print(frutti) #svuota l'array senza eliminarlo
'''
