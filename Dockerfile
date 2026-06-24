FROM python:3.11-slim

# Installer les dépendances système pour Playwright
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Dossier de travail
WORKDIR /app

# Copier les fichiers du projet
COPY pyproject.toml .
COPY . .

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install playwright flask gunicorn gevent

# Installer Chromium
RUN playwright install chromium
RUN playwright install-deps chromium

# Exposer le port
EXPOSE 5000

# Lancer avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "--worker-class", "gevent", "html_to_pdf:app"]