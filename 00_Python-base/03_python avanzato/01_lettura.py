# PATH ASSOLUTA: specifica la posizione completa di un file partendo dalla radice del filesystem
# es. su Windows: C:\A\E\file.py  — parte dal disco (C:\) e scende nelle sottocartelle A ed E
# C:\ e' la radice del disco; da li' si scende: A\E\file.py
# PATH RELATIVA: specifica la posizione di un file rispetto alla cartella di lavoro corrente (working directory)
# es. se sei gia' in C:\A, puoi scrivere E\file.py invece dell'intero percorso assoluto
#e quando creiamo i nostri progetti dobbiamo usare path relative

#interagiamo tramite scrittura e lettura con file esterni

#posso o passare la stringa tramite parametri oppure creare una variabile dandogli una stringa
#file_stream = open("assets/testoo.txt", "r")

#file_stream.close()# ogni volta che apriamo un file si apre questo buffer che dobbiamo sempre andare a chiudere

'''
with open("assets/testoo.txt", "r") as file_stream:
#lettura e scrittura nel file: r, w, a, (reading, writing, append)
   #content1 = file_stream.readline() #legge


#print(content1)

    
print(content)
'''

#ci sono altri due tipi di lettura, read line e read lines, 
#con readlines oltre a prendere tutto, ci mette il tutto in una lista e ci specifica anche gli andamenti a capo
#.readlines()

#con read line legge solo una riga, se poi ne metto un altro va alla successiva content1 = file_stream.readline() #legge

#############################################################################################

'''
file="assets/testoo.txt"
l = ["linea1\n", "linea2\n", "linea3\n"]
with open(file, "a") as file_stream:
#lettura e scrittura nel file: r, w, a, (reading, writing, append)
    new_text = ''
    questo nuovo testo verra inserito
    nella cartella
    ''
    #file_stream.write(new_text) #sovrascrive quello che già era inserito e lo cambia con quello che inseriamo
    file_stream.writelines(l)
    content = file_stream
    
print(content)
'''

#############################################################################################
#mettiamo caso che una cartella non esiste, per gestire il problema usiamo try except

file="assetsDaCarlo/testoo.txt"
l = ["linea1\n", "linea2\n", "linea3\n"]
with open(file, "a") as file_stream:
#lettura e scrittura nel file: r, w, a, (reading, writing, append) oltre a questi abbiamo anche


    new_text = '''
    questo nuovo testo verra inserito
    nella cartella
    '''
    #file_stream.write(new_text) #sovrascrive quello che già era inserito e lo cambia con quello che inseriamo
    file_stream.writelines(l)
    content = file_stream
    
print(content)

'''
di default quando scriviamo a, mette at rt e wt, stiamo leggendo e aprendo file di testo
a   at    ab
r   rt    rb
 w   wt    wb
'''