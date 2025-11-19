# Utilise une image Python officielle comme base
FROM python:3.11-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier de ton application dans le conteneur
COPY app.py .

# Installe la librairie requests (et d'autres dépendances si besoin)
RUN pip install --no-cache-dir requests

# Commande exécutée au démarrage du conteneur
FROM python:3.11-slim
WORKDIR /app
COPY app.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]

