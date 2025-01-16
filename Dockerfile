# Étape 1 : Utiliser une image Python
#FROM python:3.9
FROM python:3.9-slim
# Étape 2 : Définir le répertoire de travail
WORKDIR /app

# Étape 3 : Copier les fichiers dans le conteneur
#COPY requirements.txt requirements.txt
#COPY app.py app.py
COPY . /app

# Étape 4 : Installer les dépendances Python
RUN pip install -r requirements.txt

# Étape 5 : Exposer le port
#EXPOSE 5000

# Étape 6 : Lancer l'application
CMD ["python", "app.py"]
