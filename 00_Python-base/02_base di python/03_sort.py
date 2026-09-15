'''
a = ["fragola", "banana", "cocco"]

b = sorted(a)
#il sorted può anche essere usato come funzione per fare una copia

print(sorted(a)) #la modifica non avviene in place, l'originale a non viene toccato, 
                #ma viene creata una copia temporanea su cui avviene il sort
print(a)

a.sort()#sort e "la modifica avviene in place" così facendo modifica direttamente il vettore a

print(a)
'''