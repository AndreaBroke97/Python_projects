#BLOCCO 1
#il try se tutte queste operazioni arrivano alla fine le esegue, al contrario
#se ci sono dei problemi l'esecuzione non deve interrompersi e io devo gestire quel problema
#comandi base che gestiscono gli errori in python evitando che il programma si interrompe
#un esempio e come il try catch di java

'''
try:
    a = int(input("Insert a number: ")) #value error
    b = 5 / a #ZeroDivisionError
        
    print(b) 
except ZeroDivisionError: #abbiamo gestito il primo errore con la divisione di 0
    print("\nyou cannot divide for 0\n")
#gli except si possono forcare, posso gestire ogni evenutale caso, 
#PRIMA GLI ERRORI SPECIFICI E POI QUELLO GENERICI, QUINDI PRIMA ZERO DIVISION ERROR E POI QUELLO GENERICO
except ArithmeticError:
    print("generic error aritmetic")
except:
    print("generic error\n")

else: #si attiva solo se il try va bene
    print("been succesful\n")
finally: #quando apriamo un file poi vogliamo chiuderlo, sia se va a buon fine o no,
    print("this activates in any case")
'''       
    
###########################################################

'''
try:
    a = int(input("Insert a number: ")) #value error
    b = 5 / a #ZeroDivisionError
        
    print(b) 
#possiamo anche gestire più casi(errori) nei parametri di except
except (ValueError, ZeroDivisionError) as e: #as e, abbiamo salvato except in una variabile per manipolarlo
    
    print(f"\nerror {e}, {type(e)}\n")#questo è il messaggio di errore che spunta nei file di log
    print(f"\nerror {str(e)}, {repr(e)}\n") #repr sta per rappresentation, utile per il debug perché vedi subito che tipo di errore è, non solo il messaggio.
#il file di log e importante per vedere come debuggare un software
except:
    print("generic error\n")

else: #si attiva solo se il try va bene
    print("been succesful\n")
finally: #quando apriamo un file poi vogliamo chiuderlo, sia se va a buon fine o no,
    print("this activates in any case")
    
#file di log, e un file di registro, quando apriamo un programma, si caricano librerie a catena etc, i file di log
#sono questi file che al millisecondo viene spiegato cosa succede
'''

###########################################################

'''
try:
    a =   a = int(input("\nInsert a number: ")) #value error
    b = 5 / a #ZeroDivisionError
    print(b)
except ZeroDivisionError as e:
    print("\nyou cannot divide for zero.\n")
    raise ZeroDivisionError("i say you.. YOU CANNOT DIVIDE FOR 0!")
#raise blocca il programma, posso decidere di interrompere il mio programma
#ho controllo sul flow del mio programma

###########################################################

#altro motivo per usare raise, serve in casi come questo per interrompere il comportamento del programma se succede qualcosa di strano

age = int(input("enter user age: "))

if age > 120 or age < 0:
    raise ValueError("unlikely age")
'''

###########################################################

#noi potremmo aver bisogno di scrivere i nostri errori.

class VehicleError(Exception):
    def __init__(self, message = "vehicle is broken"):
        super().__init__(message)
        
a = input()

if Vehicle.doors > 9:
    raise VehicleError