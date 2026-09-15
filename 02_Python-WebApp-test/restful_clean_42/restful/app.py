import os
import requests

from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "instance", "creatures.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Creatures(db.Model):
		id = db.Column(db.Integer, primary_key = True)
		name = db.Column(db.String(40), nullable = True)
		height = db.Column(db.Integer, nullable = False)
		weight = db.Column(db.Integer, nullable = True)
		types = db.Column(db.Text, nullable = True)
		stats = db.Column(db.Text, nullable = True)

''' 
1) flask db init        # una sola volta nel progetto, crea cartella migrations, 
inizializza alembic

2)flask db migrate -m "messaggio"
  scandaglia app.py e visualizza tutti i model presenti. 
3)flask db upgrade

'''	
def fetch_as_dict(name):
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
            response.raise_for_status()
            data = response.json()
            return {
                "id": data["id"],
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "types": [item1["type"]["name"] for item1 in data["types"]],
                "stats": {item2["stat"]["name"]: item2["base_stat"] for item2 in data["stats"]}
            }
        except requests.exceptions.Timeout:
            print("Error! Time Out")
            
        except requests.exceptions.ConnectionError:
            print("Error! Connection failed")
            
        except requests.exceptions.HTTPError:
            print("Error! resource not found")
            


@app.route('/')
def index():
	creatures = Creatures.query.all()
	return render_template('index.html', creatures=creatures)



@app.route('/add', methods=['GET', 'POST'])
def add_creature():
	if request.method == 'POST':
		name = request.form['name']
		data = fetch_as_dict(name)

		if data is None:
			return render_template('form.html', error='Pokémon not found', creature=None)

		new_creature = Creatures(
			id = data['id'],
			name   = data['name'],
            height = data['height'],
            weight = data['weight'],
            types  = ', '.join(data['types']),
            stats  = str(data['stats'])
		)
		db.session.add(new_creature)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('form.html', creature=None)


# ✏️ Modifica prodotto esistente
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_creature(id):
	creature = Creatures.query.get_or_404(id)
	if request.method == 'POST':
		creature.name   = request.form.get('name', '')          # stringa → ok così
		creature.height = int(request.form.get('height', 0))    # Integer → int()
		creature.weight = int(request.form.get('weight', 0))    # Integer → int()
		creature.types  = request.form.get('types', '')         # Text → ok così
		creature.stats  = request.form.get('stats', '')         # Text → ok così
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('form.html', creature=creature)


# ❌ Elimina prodotto
@app.route('/delete/<int:id>', methods=['POST'])
def delete_creature(id):
	creature = Creatures.query.get_or_404(id)
	db.session.delete(creature)
	db.session.commit()
	return redirect(url_for('index'))


# 📄 Mostra singolo prodotto
@app.route('/creature/<int:id>')
def view_creature(id):
	creature = Creatures.query.get_or_404(id)
	return render_template('creature.html', creature=creature)


#ERRORHANDLER
@app.errorhandler(404)
def page_not_found(error):
	return render_template("404.html"), 404


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