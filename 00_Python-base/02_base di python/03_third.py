#name = input("tell me what's your name: ") #salvo in memoria l'input utente perchè mi tornerà utile più avanti

#<---------------------------------------------------->
'''
a = [1, 2, 3]
b = [4, 5, 19]

c = a+b

print(c)
'''

#<---------------------------------------------------->

'''
a = [1,2,3,2,3,4,5,6,2,2]


a.remove(5)
a.remove(2) #rimuove solo il primo dei tanti non rimuove tutti
print(a)

while 2 in a: #cancella tutti i 2
    a.remove(2)
'''

#<---------------------------------------------------->

'''
a = "Forza Catania"

c = "Catania" in a #restituira true o false è un boolean

print(c)

print(a[2:5]) #2:5 prende dalla lettera 2 fino alla 5 ma l'ultima cioè la 5 non viene contata quind risulterà la 4
#in lettura una stringa può essere richiamata come iterabile
#in scrittura no
'''

#<---------------------------------------------------->

'''
s = "hello world"

print(s.capitalize()) #rende in maiuscolo solo la prima lettera H e W
print(s.upper()) #rende tutto maiuscolo
print(s.lower()) #rende tutto minuscolo

s2 = "        python          "

print(s2) #printa con tutti gli spazi
print(s2.strip()) #rimuove gli spazi all'inizio e alla fine
print(s2.replace("th","TONYPITONY")) #replace mettendo "th" diciamo di cambiarlo con qualcos'altro 
                                     #quindi "TONYPITONY" e diventerà pyTONYPITONYon

print(s2)
'''

#ESERCIZIO
'''
s2 = " hello woRld"
print(s2)

print(s2.strip().capitalize())  
#con la concanetazione rimuove la R maiuscola lasciandola r e ingrandisce la H, e strip rimuove gli spazi
'''

#<---------------------------------------------------->

'''
s = "123abc"
s2 = "123abc-?"
s3 = "123"
s4 = "CIAO A TUTTI"

print(s.isalnum(), s2.isalnum()) #alnum Alfa Numerico s2 e false per -?
print(s.isdigit(), s3.isdigit()) #digit controlla se quella stringa può essere convertita in un numero
print(s.isdigit(), s3.isdigit())
print(s4.isupper()) #controlla se e tutto maiuscolo
'''

#<---------------------------------------------------->

'''
#esempi di errori logici
age = int(input("quanti anni hai")) #se non definiamo INT non funziona e stamperà due volte l'età 

print(age*2) #stampa due volte l'età invece di moltiplicarla per 2 se manca int perchè un numero lo vede come stringa invece di un int
'''