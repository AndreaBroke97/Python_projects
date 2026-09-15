import os #permetteremo di fare delle operazioni all'interno del pc

#a = os.getcwd() #così possiamo manipolarlo

print("cartella corrente", os.getcwd()) #get card working directory


#quando siamo in altre cartelle usiamo questo comando, che scrive tutti i file
#e cartelle presenti in quel livello dentro una list


print("cartelle e file:\n", os.listdir())#è iterabile possiamo effettuare molti controlli

os.chdir('Andrea')

print("cartella corrente:", os.getcwd())
print("cartelle e file:\n", os.listdir())

#if 'requirements.txt' in os.listdir():




#Creiamo una cartella

#os.mkdir("Andrea")

#Rimuoviamo la cartella

#os.rmdir("Andrea")
#possiamo cancellare cartelle solo se dovessero essere vuote

#per correggere l'errore possiamo fare un controllo verificando se e piena o no


############################################################################à