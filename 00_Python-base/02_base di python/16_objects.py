################################################################
# BLOCCO 1 — CLASSE BASE E METODI
# Lo schema della classe non è rigido: possiamo aggiungere attributi
# anche dall'esterno, senza dichiararli dentro la classe
################################################################
'''
class Student:
    description = "this class is supposed to be used anytime you will create a new student"
    # CLASS ATTRIBUTE: appartiene alla classe, condiviso da tutte le istanze

    def salutapiano():
        # Metodo SENZA self: python non dà errori se non viene mai chiamato,
        # ma non può essere chiamato su un'istanza (manca il riferimento a self)
        print(f"ciao a tutti")

    def saluta(self):
        # self è obbligatorio nei metodi di istanza: rappresenta l'oggetto stesso
        # equivalente al "this" in altri linguaggi
        print(f"ciao a tutti!, io mi chiamo {self.name}")
'''

################################################################
# BLOCCO 2 — CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE
# CLASS ATTRIBUTE: definito nella classe, condiviso da tutti gli oggetti
# INSTANCE ATTRIBUTE: definito su un singolo oggetto, appartiene solo a lui
################################################################
'''
s1 = Student()
s1.name = "Tommaso"   # instance attribute aggiunto dinamicamente su s1
s1.age = 34           # instance attribute aggiunto dinamicamente su s1

s2 = Student()
s2.name = "Lorenzo"   # s2 non ha age → accedervi darebbe AttributeError

print(s1.age)
print(s1.name, s2.name)
print(s1.role, s2.role)
print(s1, s2)  # stampa il riferimento in memoria (es: <__main__.Student object at 0x...>)
'''

################################################################
# BLOCCO 3 — SHADOWING DEL CLASS ATTRIBUTE
# Se assegni un valore a un attributo su una singola istanza,
# quella istanza smette di guardare il class attribute (shadowing)
################################################################
'''
s1 = Student()

print(s1.description)
# Prima stampa: legge il class attribute (non esiste ancora uno specifico per s1)

s1.description = "questo studente e particolarmente attivo e sveglio."
# Ora s1 ha il SUO description → shadowing del class attribute

print(s1.description)
# Seconda stampa: legge quello di s1, non più quello della classe

print(Student.description)
# Stampa il class attribute originale, che non è stato modificato
'''

################################################################
# BLOCCO 4 — CHIAMATA DI UN METODO DI ISTANZA
################################################################
'''
s1 = Student()
s1.name = "Lorenzo"

s2 = Student()
s2.name = "Pancrazio"

s1.saluta()  # Python passa s1 come self automaticamente
s2.saluta()  # Python passa s2 come self automaticamente
'''

################################################################
# BLOCCO 5 — COSTRUTTORE __init__ E METODI MAGICI
# I metodi magici (dunder: __init__, __eq__, __add__...) definiscono
# il comportamento degli oggetti in situazioni speciali (creazione, confronto, somma...)
# Esiste UN solo costruttore per classe — per casi diversi si usano if/else
################################################################
'''
class Student:
    description = "this class is supposed to be used anytime you will create a new student"
    # CLASS ATTRIBUTE

    def __init__(self, name, surname, age = 99, course = 99):
        # __init__ è il costruttore: viene chiamato automaticamente alla creazione dell'oggetto
        # I parametri possono avere valori di default (age=99, course=99)
        # Possono essere passati anche come keyword arguments (Student(name="x", surname="y"))

        self.name = name.strip().capitalize()      # strip rimuove spazi, capitalize mette maiuscola
        self.surname = surname.strip().capitalize()
        self.age = age
        self.course = course
        self.fullname = self.name + " " + self.surname  # attributo calcolato dagli altri

        # Tutti questi sono INSTANCE ATTRIBUTES: scritti dentro __init__ con self.

s1 = Student("tommaso", "pappalardo", 32, "web developer")
s2 = Student(surname = "Fuffolo", name = "riccardino")  # keyword arguments, ordine libero

print(s1)         # stampa riferimento memoria (non ha __str__ definito)
print(s2.name)
print(s2.surname)
print(s2.fullname)
print(s2.age)     # usa il valore di default: 99
print(s2.course)  # usa il valore di default: 99
'''

################################################################
# BLOCCO 6 — __eq__ E __add__ (METODI MAGICI DI CONFRONTO E SOMMA)
################################################################
'''
class Student:
    description = "this class is supposed to be used anytime you will create a new student"

    def __init__(self, name, surname, age = 99, course = 99):
        self.name = name.strip().capitalize()
        self.surname = surname.strip().capitalize()
        self.age = age
        self.course = course
        self.fullname = self.name + " " + self.surname

    def __eq__(self, other):
        # Chiamato automaticamente quando si usa == tra due oggetti (es: s1 == s2)
        # self = oggetto a sinistra dell'==, other = oggetto a destra
        # Prima controlliamo che other sia uno Student (isinstance),
        # altrimenti confrontare attributi di un int darebbe errore
        if isinstance(other, Student):
            return self.name == other.name and self.surname == other.surname and self.age == other.age
        else:
            return False  # se other non è uno Student, il confronto è sempre False

    def __add__(self, other):
        # Chiamato automaticamente quando si usa + tra due oggetti (es: s1 + s2)
        if isinstance(other, Student):
            pass  # qui andrebbe la logica della somma (es: unire dati)
        else:
            print("sum impossibile")
            return None

s1 = Student("Salvatore", "Pappalardo", 15, "web developer")
s2 = Student("Salvatore", "Pappalardo", 40, "web developer")
s3 = Student("Salvatore", "Pappalardo", 15, "cyberSec")

print(s1 == s2)  # False: stessi nome e cognome ma age diversa
print(s1 == s3)  # True: nome, cognome e age uguali (course non è nel confronto)
print(s1 == 5)   # False: 5 non è uno Student, isinstance restituisce False
'''

###################################################################
# BLOCCO 7 — INTROSPECTION E REFLECTION
# Introspection: esaminare a runtime la struttura di un oggetto
#   → capire di cosa è fatto, quali attributi ha, a quale classe appartiene
# Reflection: modificare a runtime la struttura di un oggetto
#   → aggiungere/modificare attributi dinamicamente con setattr
###################################################################
'''
class Playlist:
    description = "class used to represent playlists"

    def __init__(self, name, pl_descr, songs = []):
        self.name = name
        self.pl_descr = pl_descr
        self.songs = songs

pl1 = Playlist("\nestate 25 ", "le canzoni di quando ho conosciuto Morena", ['maracaibo', 'danza koduro'])
pl2 = Playlist("\nestate 25 ", "le canzoni di quando ho conosciuto Morena", "cinciuncian")

print(pl1.name)
# HARD-CODED: il nome dell'attributo è scritto nel codice, non cambia mai a runtime

a = input("enter the attribute you are interested: ")
# SOFT-CODED: l'utente decide quale attributo leggere → il codice è flessibile

if hasattr(pl1, a):
    # hasattr: controlla se l'attributo esiste sull'oggetto (True/False)
    print(getattr(pl1, a, "attribute doesn't exist. "))
    # getattr: legge il valore dell'attributo passando il nome come stringa
    # il terzo argomento è il valore di default se l'attributo non esiste
else:
    b = input("attribute doesn't exist, Now enter the attribute che si vuole associare: ")
    setattr(pl1, a, b)
    # setattr: REFLECTION → aggiunge/modifica un attributo a runtime
print(getattr(pl1, a))

# Altri strumenti di introspection:
#print(type(pl1))                    # → <class '__main__.Playlist'>
#print(isinstance(pl1, Playlist))    # → True: pl1 è un'istanza di Playlist
#print(isinstance(pl1, int))         # → False

#print(hasattr(pl1, "name"))         # → True: l'attributo name esiste
#print(hasattr(pl1, "promotion"))    # → False: promotion non esiste

#print(list(Playlist.__dict__))      # attributi della CLASSE (metodi, class attributes)
#print(list(pl1.__dict__))           # attributi dell'ISTANZA (name, pl_descr, songs di pl1)
'''

################################################################
# BLOCCO 8 — INCAPSULAMENTO E ATTRIBUTI PRIVATI (name mangling)
# Incapsulamento: ogni classe gestisce una responsabilità specifica,
# con attributi pubblici e "privati" separati
# In Python non esiste un vero private, ma __ simula questo comportamento
################################################################

class Person:

    def __init__(self, name, age):
        self.name = name      # attributo pubblico: accessibile direttamente da fuori
        self.__age = age
        # __ davanti al nome = name mangling:
        # Python rinomina internamente __age in _Person__age
        # Questo "nasconde" l'attributo e simula il comportamento private

    def get_age(self):
        # getter: unico modo "ufficiale" per accedere a __age dall'esterno
        return self.__age

p1 = Person("Marta", 23)

print(p1.name)       # pubblico: accessibile direttamente
print(p1.get_age())  # accesso tramite getter

print(list(p1.__dict__))
# __dict__ è il dizionario interno degli attributi dell'istanza
# mostra: ['name', '_Person__age'] → si vede il name mangling applicato

print(p1._Person__age)
# Name mangling: Python salva __age come _Person__age
# tecnicamente accessibile dall'esterno, ma è una convenzione "non farlo"

#print(p1.__age)
# → AttributeError: __age non esiste con quel nome, Python lo ha rinominato
