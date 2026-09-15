def saluto(nome):
    global b #questa keyword tutte le volte che ci sarà b farà riferimento alla b se lo togliamo alla fine dopo 343 stamperà 5
    print(f"ciao, {nome}")
    b = 343
    print(b)# qui funziona perchè e dentro la "stanza" in cui e b
    #ambito di visibilità, b = 5 esiste solo esclusivamente dentro la funzione, cioè una variabile locale
    

b = 5 #inizia il programma ed è ad un livello globale del codice 
print(b)
saluto("Giacomo")
print(b)
#print(b) #da errore perchè b e dentro una "stanza a parte " 