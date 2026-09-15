#FUNZIONI
def addizione(x, y):
    """Questa funzione somma due numeri"""
    return x + y

def sottrazione(x, y):
    """Questa funzione sottrae due numeri"""
    return x - y

def moltiplicazione(x, y):
    """Questa funzione moltiplica due numeri"""
    return x * y

def divisione(x, y):
    """Questa funzione divide due numeri e gestisce la divisione per zero"""
    if y == 0:
        return "Errore: Impossibile dividere per zero!"
    return x / y 


#MENU
print("Seleziona l'operazione desiderata:")
print("1. Addizione")
print("2. Sottrazione")
print("3. Moltiplicazione")
print("4. Divisione")

while True: # while True permette alla calcolatrice di continuare a funzionare 
            # finché l'utente non decide esplicitamente di uscire digitando 
            # una lettera diversa da "s" alla fine di un calcolo.
            
    # Prende l'input dell'utente
    scelta = input("Inserisci la tua scelta (1/2/3/4): ")

    # Controlla se la scelta è tra le opzioni valide
    if scelta in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
        except ValueError: #gestisce l'errore se l'utente inserisce un input non numerico
            print("Input non valido. Per favore inserisci un numero.")
            continue

        if scelta == '1':
            print(f"Risultato: {num1} + {num2} = {addizione(num1, num2)}")

        elif scelta == '2':
            print(f"Risultato: {num1} - {num2} = {sottrazione(num1, num2)}")

        elif scelta == '3':
            print(f"Risultato: {num1} * {num2} = {moltiplicazione(num1, num2)}")

        elif scelta == '4':
            print(f"Risultato: {num1} / {num2} = {divisione(num1, num2)}")
        
        # Chiede all'utente se vuole fare un altro calcolo
        prossimo_calcolo = input("Vuoi eseguire un altro calcolo? (s/n): ")
        if prossimo_calcolo.lower() != 's':
            print("Chiusura della calcolatrice. Arrivederci!")
            break
    else:
        print("Scelta non valida. Riprova.")