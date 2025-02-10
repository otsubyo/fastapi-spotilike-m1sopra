# fastapi-spotilike-m1sopra

## Launch backend  

1. **Assurez-vous que votre base de données SQL est en cours d’exécution** (si nécessaire).  

2. **Installez les dépendances Python :** 
   ```bash
   pip install -r requirements.txt

3. **Lancez le serveur FastAPI :**
    ```bash
  uvicorn main:app --reload

4.**Accédez à la documentation Swagger de l’API :**
    ```bash
  http://localhost:8000/docs


## Lancer ensuite un autre terminal powershell

## Launch frontend

1. **Allez dans le dossier du frontend :**
    ```bash
  cd frontend

2. **Installez les dépendances avec npm :**
    ```bash
  npm install

3. **Lancez le serveur de développement :**
    ```bash
  npm run dev

4. **Accédez au site sur :**
    ```bash
  http://localhost:5173