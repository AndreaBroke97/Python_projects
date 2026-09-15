
#DISPATCH

# COMPOSIZIONE
# Invece di ereditare, un oggetto "contiene" un altro oggetto come attributo.
# Vehicle non eredita da Starting — riceve un oggetto Starting dal costruttore.
# Questo permette di cambiare il comportamento a runtime semplicemente passando un oggetto diverso.

# Classe madre: definisce l'interfaccia comune (il metodo start)
class Starting:
    def start(self):
        print("the mechanism start")

# Classe figlia: sovrascrive start() con avviamento elettrico
class ElettricStarting(Starting):
    def start(self):
        print("electric scooter")

# Classe figlia: sovrascrive start() con avviamento a pedale
class PedalStart(Starting):
    def start(self):
        print("the pedal work")


class Vehicle:
    def __init__(self, model, starting):
        self.model = model
        self.starting = starting
        # starting non è una stringa — è un OGGETTO (ElettricStarting o PedalStart)
        # Vehicle non sa quale tipo di avviamento ha, lo riceve dall'esterno
        # questo si chiama dependency injection: il comportamento viene "iniettato" dall'esterno

    def start(self):
        self.starting.start()
        # chiama il metodo start() sull'oggetto starting passato nel costruttore
        # se starting è ElettricStarting → stampa "electric scooter"
        # se starting è PedalStart → stampa "the pedal work"
        # Vehicle non cambia — cambia solo l'oggetto che gli passi
    
#un istanza in cui passiamo un oggetto PedalStart()
m1 = Vehicle("KTM", PedalStart())
m2 = Vehicle("Panda", ElettricStarting())

#richiama lo stesso metodo della class Vehicle e richiama self.starting.start()
m1.start() #richiama PedalStart
m2.start() # richiama ElettricStarting

print("ora richiamo l'oggetto come attributo..")

#m1.starting è un attributo a cui inseriamo un oggetto
#su questo oggetto richiamiamo il dynamic dispatch
m1.starting.start()