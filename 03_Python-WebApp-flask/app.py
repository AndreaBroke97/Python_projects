''' librerie da importare:
flask
flask-restful
flask-sqlalchemy
flask-migrate
'''

# FASE 1 | IMPORTAZIONE DELLE LIBRERIA
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# FASE 2 | CONFIGURAZIONE DELLA WEB APP

app = Flask(__name__) #__name__ consideriamolo come place holder standard e va acontrollare se la web app di flask e salvata nel main folder del nostro progetto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db' #configuro il database, dicendo che e sqlite di nome products.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #è una configurazione, se mettevamo True durante l'esecuzione della web app spuntano su schermo messaggi di aggiornamento, Track tiene traccia di tutte le modifiche, quindi mettiamo False

db = SQLAlchemy(app) #db oggetto della classe SQLAlchemy, collegato all'app
migrate = Migrate(app, db)#metterà in comunicazione la webApp con il DB di SQLAlchemy

# FASE 3 | COLLEGARE IL DATABASE

class Product(db.Model): #creo una scheda di cui all'interno
    name = db.Column(db.String(80), primary_key = True)
    price = db.Column(db.Float, nullable = False)# deve sempre avee un valore, se e campo vuoto return Error
    description = db.Column(db.Text, nullable = True)#text impone un vincolo sul numero di caratteri
    image_url = db.Column(db.String(255), nullable = True)# 
    
    
#########################################
#gestione rotte (routing)
@app.route('/', methods = ['POST', 'GET'])#operatore, quello che vedrà lui nella barra di ricerca cioe /
def index():
    products = Product.query.all()
    return render_template('index.html', products = products)#products = products i dati verranno passati al template
#per fare funzionare render_template nella libreria dobbiamo mettere from flask import Flask, render_template
    
@app.route('/again/<string:variabile>', methods = ['POST', 'GET'])
def index_again(variabile):
    products = Product.query.all()
    return render_template('index.html', variabile = variabile)#products = products i dati verranno passati al template




##########################à

#FINE PROGETTO

if __name__ == '__main__':
    app.run(debug = True)