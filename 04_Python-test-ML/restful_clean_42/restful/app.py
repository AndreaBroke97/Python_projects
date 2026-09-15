from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#DUE NUOVE LIBRERIE PER IMPORTARE JOBLIB
import pandas as pd
from joblib import load

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
#CARICAMENTO MODELLO MACHINE LEARNING
model = load("modello_mutuo.joblib")


class Product(db.Model):
	name = db.Column(db.String(80), primary_key=True)
	price = db.Column(db.Float, nullable=False)
	description = db.Column(db.Text, nullable=True)
	image_url = db.Column(db.String(255), nullable=True)

''' 
1) flask db init        # una sola volta nel progetto, crea cartella migrations, 
inizializza alembic

2)flask db migrate -m "messaggio"
  scandaglia app.py e visualizza tutti i model presenti. 
3)flask db upgrade

'''	

# ✅ Mostra tutti i prodotti
@app.route('/')
def index():
	products = Product.query.all()
	return render_template('index.html', products=products)


# Aggiungi nuovo prodotto
@app.route('/add', methods=['GET', 'POST'])
def add_product():
	if request.method == 'POST':
		new_product = Product(
			name=request.form['name'],
			price=float(request.form['price']),
			description=request.form.get('description', ''),
			image_url=request.form.get('image_url', '')
		)
		db.session.add(new_product)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('form.html', product=None)


# ✏️ Modifica prodotto esistente
@app.route('/edit/<string:name>', methods=['GET', 'POST'])
def edit_product(name):
	product = Product.query.get_or_404(name)
	if request.method == 'POST':
		product.price = float(request.form['price'])
		product.description = request.form.get('description', '')
		product.image_url = request.form.get('image_url', '')
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('form.html', product=product)


# ❌ Elimina prodotto
@app.route('/delete/<string:name>', methods=['POST'])
def delete_product(name):
	product = Product.query.get_or_404(name)
	db.session.delete(product)
	db.session.commit()
	return redirect(url_for('index'))


# 📄 Mostra singolo prodotto
@app.route('/product/<string:name>')
def view_product(name):
	product = Product.query.get_or_404(name)
	return render_template('product.html', product=product)


#ERRORHANDLER
@app.errorhandler(404)
def page_not_found(error):
	return render_template("404.html"), 404

@app.route("/mutuo", methods=["GET", "POST"])
def mutuo():
	if request.method == "POST":
		dati_cliente = {
			"Gender":            request.form["Gender"],
			"Married":           request.form["Married"],
			"Dependents":        float(request.form["Dependents"]),
			"Education":         request.form["Education"],
			"Self_Employed":     request.form["Self_Employed"],
			"ApplicantIncome":   float(request.form["ApplicantIncome"]),
			"CoapplicantIncome": float(request.form["CoapplicantIncome"]),
			"LoanAmount":        float(request.form["LoanAmount"]),
			"Loan_Amount_Term":  float(request.form["Loan_Amount_Term"]),
			"Credit_History":    float(request.form["Credit_History"]),
			"Property_Area":     request.form["Property_Area"],			
		}
		df = pd.DataFrame([dati_cliente])#ML si aspetta una tabella non un dizionario trasformando il dizionario in una tabella
		predizione  = model.predict(df)[0]#ML guarda la tabella e risponde 1(approvato) oppure 0(rifiutato) [0] prende solo il primo elemento della lista che ritorna
		probabilita = round(model.predict_proba(df)[0, 1] * 100, 1)#chiede al ML quanto è sicuro della sua risposta [0, 1] significa prima riga, seconda colonna della probabilità di approvazione
		esito       = "APPROVATO" if predizione == 1 else "RIFIUTATO"#traduce il numero in una parola
		return render_template("mutuo_risultato.html", esito=esito, probabilita=probabilita)

	return render_template("mutuo_form.html")

		

if __name__ == '__main__':
	app.run(debug=True) ##permette di fare le modifiche!!!

	'''
	=====================================
.venv\Scripts\Activate.ps1 
flask db init

flask db migrate -m "creazione db"

flask db upgrade
=====================================

python app.py

flask run non fa modifiche

http://127.0.0.1:5000/


'''