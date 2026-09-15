#piccoli blocchi di codice che ci permette di effettuarli in place
numbers = [1,2,3,4 ]

doubled = list(map(lambda x:x*2, numbers)) #x prima dei due punti e l'input, partendo da x deve restituire x * 2, e x lo prende da numbers
#map e una funzione di ordine superiore, un comando fa applicare la funzione agli elementi dell'iterabile numbers (struttura: funzione iterabile)
# il list di fuori prende tutto convertendolo in una lista
#lo svantaggio di questa funzione lambda, e una funzione in place, non si deve definire e richiamare, e viene applicata solo quando viene scritta

print(doubled)

doubled = list(map(lambda el.capitalize(): el, list)) #da usare più semplice di fare el. capitalize etc per ingrandire