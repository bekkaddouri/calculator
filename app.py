from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder="templates")

# Configuration de la base de données
DB_HOST = os.getenv("DATABASE_HOST", "localhost")
DB_NAME = os.getenv("DATABASE_NAME", "notes_db")
DB_USER = os.getenv("DATABASE_USER", "user")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
db = SQLAlchemy(app)

# Modèle de données
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    semester1 = db.Column(db.Float, nullable=False)
    semester2 = db.Column(db.Float, nullable=False)
    average = db.Column(db.Float, nullable=False)

# Route principale
@app.route('/calculate', methods=['POST'])
def calculate_average():
    data = request.json
    semester1 = data.get('semester1')
    semester2 = data.get('semester2')

    if semester1 is None or semester2 is None:
        return jsonify({'error': 'Les notes des deux semestres sont requises'}), 400

    try:
        semester1 = float(semester1)
        semester2 = float(semester2)
        average = (semester1 + semester2) / 2

        # Enregistrer dans la base de données
        note = Note(semester1=semester1, semester2=semester2, average=average)
        db.session.add(note)
        db.session.commit()

        return jsonify({'average': round(average, 2)})
    except ValueError:
        return jsonify({'error': 'Les valeurs doivent être des nombres'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)

