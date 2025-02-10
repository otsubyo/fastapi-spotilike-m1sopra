from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from fastapi.staticfiles import StaticFiles
import database, JWT_config, model
from datetime import time
import os

# --- FastAPI ---

# Application FastAPI avec gestionnaire lifespan
def lifespan(app: FastAPI):
    print("Démarrage de l'application...")
    database.init_db()
    yield  
    print("Arrêt de l'application...")
    
app = FastAPI(
    lifespan=lifespan,
    title="Mon Application API",
    description="Documentation de l'API avec Swagger UI",
    version="1.0.0",
    docs_url="/docs",  
)

# --- Configuration CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autorise toutes les origines (change pour + de sécurité)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"]  # Important pour les fichiers statiques
)

# Définir le chemin du dossier des images
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "public"))

# Vérifier que le dossier existe
if not os.path.exists(static_dir):
    raise RuntimeError(f"Le dossier 'public' n'existe pas : {static_dir}")

# Monter le dossier pour servir les images sous "/images/"
app.mount("/images", StaticFiles(directory=os.path.join(static_dir, "images")), name="images")

# --- Endpoints Albums ---
@app.get("/api/albums/")
def get_albums(session: Session = Depends(database.get_session)):
    return session.exec(select(model.Album)).all()

@app.get("/api/albums/{id}")
def get_album(id: int, session: Session = Depends(database.get_session)):
    album = session.get(model.Album, id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@app.get("/api/albums/{id}/songs")
def get_album_songs(id: int, session: Session = Depends(database.get_session)):
    album = session.get(model.Album, id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")

    songs = session.exec(select(model.Track).where(model.Track.album_id == id)).all()

    # ✅ Convertit le temps (hh:mm:ss) en secondes (int)
    for song in songs:
        if isinstance(song.duration, time):
            song.duration = song.duration.hour * 3600 + song.duration.minute * 60 + song.duration.second
        else:
            song.duration = 0  # Par défaut, 0 si pas de durée

    return songs


@app.post("/api/albums/{id}/songs")
def add_song_to_album(id: int, track: model.Track, session: Session = Depends(database.get_session), token: JWT_config.TokenData = Depends(JWT_config.verify_token)):
    album = session.get(model.Album, id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    
    new_track = model.Track(
        title=track.title,
        duration=track.duration,
        album_id=id
    )
    session.add(new_track)
    try:
        session.commit()
        session.refresh(new_track)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred while adding the track")
    
    return new_track

@app.post("/api/albums/")
def add_album(album: model.Album, session: Session = Depends(database.get_session), token: JWT_config.TokenData = Depends(JWT_config.verify_token)):
    session.add(album)
    session.commit()
    session.refresh(album)
    return album

@app.put("/api/albums/{id}")
def update_album(id: int, album_data: model.Album, session: Session = Depends(database.get_session), token: JWT_config.TokenData = Depends(JWT_config.verify_token)):
    album = session.get(model.Album, id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    for key, value in album_data.model_dump(exclude_unset=True).items():
        setattr(album, key, value)
    session.commit()
    session.refresh(album)
    return album

@app.delete("/api/albums/{id}")
def delete_album(id: int, session: Session = Depends(database.get_session), token: JWT_config.TokenData = Depends(JWT_config.verify_token)):
    album = session.get(model.Album, id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    session.delete(album)
    session.commit()
    return {"message": "Album deleted successfully"}

# --- Endpoints Genres ---
@app.get("/api/genres/")
def get_genres(session: Session = Depends(database.get_session)):
    return session.exec(select(model.Genre)).all()

@app.put("/api/genres/{id}")
def update_genre(id: int, genre_data: model.Genre, session: Session = Depends(database.get_session), token: JWT_config.TokenData = Depends(JWT_config.verify_token)):
    genre = session.get(model.Genre, id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    for key, value in genre_data.model_dump(exclude_unset=True).items():
        setattr(genre, key, value)
    session.commit()
    session.refresh(genre)
    return genre

# --- Endpoints Artistes ---
@app.get("/api/artists/")
def get_artists(session: Session = Depends(database.get_session)):
    artists = session.exec(select(model.Artist)).all()

    if not artists:
        return []  # ✅ Retourne un tableau vide si aucun artiste

    for artist in artists:
        # ✅ Vérifie si le chemin est déjà correct pour éviter la duplication
        if artist.avatar and not artist.avatar.startswith("/images/artists/"):
            artist.avatar = f"/images/artists/{artist.avatar}"
        elif not artist.avatar:
            artist.avatar = "/images/artists/default.jpg"

    return artists

@app.get("/api/artists/{id}")
def get_artist(id: int, session: Session = Depends(database.get_session)):
    artist = session.get(model.Artist, id)
    
    if not artist:
        raise HTTPException(status_code=404, detail="Artiste introuvable")

    # ✅ Ici, on ne modifie PAS `artist.avatar`, car c'est déjà fait dans `get_artists()`
    return artist


@app.get("/api/artists/{id}/songs")
def get_artist_songs(id: int, session: Session = Depends(database.get_session)):
    # Requête pour trouver les morceaux liés à cet artiste
    tracks = session.exec(
        select(model.Track).join(model.TrackArtist).where(model.TrackArtist.artist_id == id)
    ).all()
    
    if not tracks:
        raise HTTPException(status_code=404, detail="No songs found for the given artist")
    
    return tracks

@app.put("/api/artists/{id}")
def update_artist(id: int, artist_data: model.Artist, session: Session = Depends(database.get_session), token: JWT_config.TokenData = Depends(JWT_config.verify_token)):
    artist = session.get(model.Artist, id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    for key, value in artist_data.model_dump(exclude_unset=True).items():
        setattr(artist, key, value)
    session.commit()
    session.refresh(artist)
    return artist

@app.delete("/api/artists/{id}")
def delete_artist(id: int, session: Session = Depends(database.get_session), token: JWT_config.TokenData = Depends(JWT_config.verify_token)):
    artist = session.get(model.Artist, id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    session.delete(artist)
    session.commit()
    return {"message": "Artist deleted successfully"}

# --- Endpoints Users ---
@app.post("/api/users/signup")
def signup(user: model.User, session: Session = Depends(database.get_session)):
    # Vérifiez si l'utilisateur ou l'email existe déjà
    existing_user = session.exec(select(model.User).where(model.User.username == user.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    existing_email = session.exec(select(model.User).where(model.User.email == user.email)).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hachez le mot de passe avant l'insertion
    user.password = database.hash_password(user.password)

    # Insérez le nouvel utilisateur
    session.add(user)
    try:
        session.commit()
        session.refresh(user)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="An error occurred while creating the user")
    
    return {"message": "User created successfully", "user_id": user.user_id}

@app.post("/api/users/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(database.get_session)
):
    user = session.exec(select(model.User).where(model.User.username == form_data.username)).first()
    if not user or not database.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = JWT_config.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.delete("/api/users/{id}")
def delete_user(id: int, session: Session = Depends(database.get_session), token: JWT_config.TokenData = Depends(JWT_config.verify_token)):
    user = session.get(model.User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": "User deleted successfully"}

