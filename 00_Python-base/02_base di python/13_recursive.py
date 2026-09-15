def factorial(n): #se usiamo una funzione ricorsiva dobbiamo implementare il caso base, in questo loop infinito dobbiamo dargli una via di uscita
    #caso base
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) 


    