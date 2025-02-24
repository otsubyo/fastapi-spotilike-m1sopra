# fastapi-spotilike-m1sopra

## Launch backend  

1. **Assurez-vous que votre base de données SQL est en cours d’exécution** (si nécessaire).

2. **Allez dans le dossier du backend :**
    ```bash
    cd backend

3. **Créez un environnement virtuel Python et activez-le**
   ```bash
   python -m venv ./venv
   ```
   _bash :_
   ```bash
   source ./venv/bin/activate
   ```
   _powershell :_
   ```bash
   .\Scripts\Activate.ps1
   ```
   _cmd :_
   ```bash
   .\Script\activate.bat
   ```
   

5. **Installez les dépendances Python :** 
    ```bash
    pip install -r requirements.txt

6. **Allez dans le dossier de l'API :**
    ```bash
    cd api

5. **Lancez le serveur FastAPI :**
    ```bash
    uvicorn main:app --reload

6. **Ouvrez votre serveur de base de donnée mysql et lancez le script SeedData.sql sur le schema "spotilike_db_carl_willy"**  


7. **Accédez à la documentation Swagger de l’API :**
    ```bash
    http://localhost:8000/docs

## Lancer ensuite un autre terminal powershell

## Launch frontend

1. **Allez dans le dossier du frontend :**
    ```bash
    cd frontend/spotilike

2. **Installez les dépendances avec npm :**
    ```bash
    npm install

3. **Lancez le serveur de développement :**
    ```bash
    npm run dev

4. **Accédez au site sur :**
    ```bash
    http://localhost:5173
