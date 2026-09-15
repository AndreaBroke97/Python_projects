# Progetti Python

Esercizi e progetti in linguaggio Python svolti durante i miei studi alla Steve Jobs Academy, sede di Catania. Più che una raccolta, è un percorso: parte dalle fondamenta del linguaggio — sintassi, strutture dati, programmazione a oggetti — e arriva fino allo sviluppo di applicazioni web con Flask e all'integrazione di un modello di Machine Learning. Le cartelle sono numerate in ordine perché ognuna si appoggia a quella prima: i concetti imparati negli esercizi di base tornano, in forma più strutturata, nei progetti web, e questi ultimi confluiscono nel progetto finale.

## Sul mio contributo ai progetti

Flask, SQLAlchemy, Jinja2 e le altre librerie usate qui non sono state scritte da me: sono strumenti già esistenti e ampiamente diffusi nello sviluppo Python. Nelle esercitazioni web il punto di partenza era spesso un progetto Flask con la struttura di base già predisposta.

Il mio lavoro è consistito nello studiare il funzionamento di questi strumenti e nel costruirci sopra applicazioni complete: definire i modelli dei dati e le route, scrivere la logica di lettura e conversione dei dati inseriti dall'utente, realizzare le pagine HTML e, soprattutto, gestire i casi di errore che possono presentarsi lungo il percorso. Negli esercizi di base, invece, il codice è interamente mio, ed è lì che ho imparato i fondamentali su cui tutto il resto si appoggia.

## 00_Python-base

Le fondamenta del linguaggio, raccolte in un unico percorso che parte dal primo "hello world" e arriva alla programmazione a oggetti. Il cuore è la cartella `02_base di python`, dove si concentra il grosso del lavoro: tipi di dato e operatori, condizioni e cicli, poi le funzioni affrontate a fondo — scope, ricorsione, `*args` e `**kwargs`, funzioni lambda — e ancora list comprehension, dizionari e gestione delle eccezioni con `try-except`. La progressione si chiude sui pilastri della programmazione a oggetti, ereditarietà e composizione, accompagnati da uno schema `.drawio` disegnato per fissare visivamente le relazioni tra le classi.

Attorno a questo nucleo ci sono le tappe che completano il quadro: la cartella `03_python avanzato` fa un passo oltre con la lettura e la scrittura di file e la gestione dei dati in formato JSON — la stessa idea che, più avanti, alimenterà i progetti veri e propri. `00_AMBIENTIVIRTUALI` raccoglie i primi esperimenti con gli ambienti virtuali e le richieste HTTP, `01_assets` contiene i file di testo su cui girano gli esercizi, e `01_analizzatore_testo.py` è un piccolo programma a sé. È la cartella meno appariscente ma la più importante: senza queste basi, nulla di ciò che viene dopo starebbe in piedi.

## 01_Python-VR-Environment

Il primo progetto in cui la programmazione a oggetti smette di essere un esercizio e diventa uno strumento. L'idea è modellare delle "creature" a partire da file JSON: una classe rappresenta la singola creatura, un'altra si occupa di leggerne i dati dal disco, e altre gestiscono la scrittura e la stampa. Il tutto lavora su una raccolta di schede — la cartella `data/creatures`, in cui ogni creatura ha il proprio file — che l'applicazione carica, interpreta e restituisce.

È il ponte tra gli esercizi di base e i progetti web che vengono dopo: gli stessi concetti — classi, lettura e scrittura di JSON — ma finalmente applicati a un caso concreto, con dati che vivono in file separati anziché scritti a mano nel codice. Qui ho capito come far dialogare gli oggetti con dei dati reali, un passaggio che ritorna, quasi identico, quando quei dati inizieranno ad arrivare da un database o da un'API.

## 02_Python-WebApp-test

La prima vera applicazione web con Flask, e la più ricca dei due progetti web "di base". L'utente inserisce il nome di un Pokémon e l'applicazione lo cerca in tempo reale tramite una richiesta HTTP alla PokeAPI, un servizio pubblico esterno; ne estrae i dati principali — id, altezza, peso, tipi e statistiche — e li salva nel proprio database SQLite. È il momento in cui il progetto smette di lavorare solo su dati locali .

Sul piano funzionale è un CRUD completo: si possono creare nuove schede, visualizzarle in elenco o nel dettaglio, modificarle ed eliminarle, il tutto appoggiato a SQLAlchemy e alle migrazioni di Flask-Migrate. La parte a cui ho dedicato più attenzione, è la gestione degli errori: l'applicazione non si blocca se il Pokémon non esiste, se la richiesta va in timeout o se la connessione fallisce, e una pagina 404 personalizzata intercetta gli indirizzi non validi. In ognuno di questi casi l'utente riceve un messaggio chiaro invece di trovarsi davanti a un'applicazione rotta. È l'esercizio in cui ho messo insieme, per la prima volta, il dialogo con un servizio esterno, la persistenza dei dati e un'interfaccia completa.

## 03_Python-WebApp-flask

Un'applicazione Flask che getta le basi di un e-commerce, più magra della precedente e pensata proprio per consolidare la struttura di un progetto web senza le complicazioni di un'API esterna. Il cuore è il modello `Product`, con nome, prezzo, descrizione e immagine, salvato in un database SQLite tramite SQLAlchemy e gestito con le migrazioni di Flask-Migrate. La route principale recupera tutti i prodotti dal database e li passa al template `index.html`, che si occupa di mostrarli.

È un progetto volutamente essenziale, e proprio per questo utile: mette a fuoco il collegamento tra Flask e un database e la visualizzazione dei record in una pagina, senza altri elementi a distrarre. È anche la base da cui parte, riprendendone il modello dei prodotti, il progetto successivo.

## 04_Python-test-ML

Il progetto più completo del percorso, ed è lo stesso tema affrontato all'esame nella sua versione definitiva. Parte dall'applicazione di gestione prodotti del progetto precedente — con il suo CRUD completo su database SQLite — e vi aggiunge l'integrazione di un modello di Machine Learning per la previsione dei mutui, così che nella stessa app trovino posto sia la gestione dei dati sia la previsione.

Il modello è stato addestrato separatamente su un dataset di richieste di mutuo ed esportato come file `.joblib`, che l'applicazione carica una sola volta all'avvio anziché a ogni richiesta. Attraverso la route `/mutuo`, l'utente compila un form con i propri dati anagrafici e finanziari — genere, stato civile, persone a carico, istruzione, redditi del richiedente e dell'eventuale co-richiedente, importo e durata del prestito, storico creditizio e area dell'immobile. L'applicazione converte questi valori nei tipi attesi, li organizza in una tabella con pandas — perché il modello si aspetta una struttura tabellare, non un dizionario — e la sottopone al classificatore. In risposta ottiene una previsione, tradotta in un esito leggibile (approvato o rifiutato), insieme alla probabilità associata. È il punto in cui web app, database e Machine Learning si uniscono nello stesso progetto.


## Come eseguire i progetti

Gli esercizi della cartella `00_Python-base` sono script autonomi: si lanciano da terminale con `python nomefile.py` (oppure `python3 nomefile.py` su macOS e Linux).

Le applicazioni Flask, invece, richiedono un ambiente virtuale .venv con le dipendenze installate. Dal terminale, dentro la cartella del progetto:
