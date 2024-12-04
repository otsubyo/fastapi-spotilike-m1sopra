from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Session, create_engine, select, Relationship
from datetime import datetime, timedelta
import jwt
from typing import List, Optional
from datetime import time, date, timezone, timedelta
import bcrypt

# --- Configuration de la base de données ---
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/MusicDB"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

# --- Configuration des mdp hashés ---
def hash_password(password: str) -> str:
    """Hache le mot de passe pour le stocker dans la base de données."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Vérifie qu'un mot de passe correspond à son hachage."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# --- Configuration JWT ---
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")

class TokenData(BaseModel):
    username: str

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return TokenData(username=username)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# --- Models ---
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date, time

# Artist Table
class Artist(SQLModel, table=True):
    artist_id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255, nullable=False)
    avatar: Optional[str] = Field(default=None, max_length=255)
    biography: Optional[str] = Field(default=None)

    albums: List["Album"] = Relationship(back_populates="artist")
    track_artists: List["TrackArtist"] = Relationship(back_populates="artist")

# Genre Table
class Genre(SQLModel, table=True):
    genre_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=100, nullable=False)
    description: Optional[str] = Field(default=None)

    track_genres: List["TrackGenre"] = Relationship(back_populates="genre")

# Album Table
class Album(SQLModel, table=True):
    album_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=255, nullable=False)
    cover: Optional[str] = Field(default=None, max_length=255)
    release_date: Optional[date] = Field(default=None)
    artist_id: int = Field(foreign_key="artist.artist_id")

    artist: Optional[Artist] = Relationship(back_populates="albums")
    tracks: List["Track"] = Relationship(back_populates="album")

# Track Table
class Track(SQLModel, table=True):
    track_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=255, nullable=False)
    duration: Optional[time] = Field(default=None)
    album_id: int = Field(foreign_key="album.album_id")
    album_id: int = Field(foreign_key="album.album_id")

    album: Optional[Album] = Relationship(back_populates="tracks")
    track_artists: List["TrackArtist"] = Relationship(back_populates="track")
    track_genres: List["TrackGenre"] = Relationship(back_populates="track")

# Track-Artist Relationship Table
class TrackArtist(SQLModel, table=True):
    track_id: int = Field(foreign_key="track.track_id", primary_key=True)
    artist_id: int = Field(foreign_key="artist.artist_id", primary_key=True)
    role: str = Field(nullable=False)  # Enum: 'Primary', 'Featuring'

    track: Optional[Track] = Relationship(back_populates="track_artists")
    artist: Optional[Artist] = Relationship(back_populates="track_artists")

# Track-Genre Relationship Table
class TrackGenre(SQLModel, table=True):
    track_id: int = Field(foreign_key="track.track_id", primary_key=True)
    genre_id: int = Field(foreign_key="genre.genre_id", primary_key=True)

    track: Optional[Track] = Relationship(back_populates="track_genres")
    genre: Optional[Genre] = Relationship(back_populates="track_genres")

# User Table
class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(max_length=100, nullable=False, unique=True)
    password: str = Field(nullable=False)
    email: str = Field(max_length=255, nullable=False, unique=True)

# --- FastAPI ---

# Application FastAPI avec gestionnaire lifespan
def lifespan(app: FastAPI):
    # Code à exécuter au démarrage
    print("Démarrage de l'application...")
    init_db()
    yield  # Exécution de l'application
    # Code à exécuter à l'arrêt
    print("Arrêt de l'application...")
    
app = FastAPI(
    lifespan=lifespan,
    title="Mon Application API",
    description="Documentation de l'API avec Swagger UI",
    version="1.0.0",
    docs_url="/docs",  # URL pour Swagger UI
)

# --- Endpoints Albums ---
@app.get("/api/albums/")
def get_albums(session: Session = Depends(get_session)):
    return session.exec(select(Album)).all()

@app.get("/api/albums/{id}")
def get_album(id: int, session: Session = Depends(get_session)):
    album = session.get(Album, id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@app.get("/api/albums/{id}/songs")
def get_album_songs(id: int, session: Session = Depends(get_session)):
    album = session.get(Album, id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return session.exec(select(Track).where(Track.album_id == id)).all()

@app.post("/api/albums/{id}/songs")
def add_song_to_album(id: int, track: Track, session: Session = Depends(get_session), token: TokenData = Depends(verify_token)):
    album = session.get(Album, id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    
    new_track = Track(
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
def add_album(album: Album, session: Session = Depends(get_session), token: TokenData = Depends(verify_token)):
    session.add(album)
    session.commit()
    session.refresh(album)
    return album

@app.put("/api/albums/{id}")
def update_album(id: int, album_data: Album, session: Session = Depends(get_session), token: TokenData = Depends(verify_token)):
    album = session.get(Album, id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    for key, value in album_data.obj.model_dump(exclude_unset=True).items():
        setattr(album, key, value)
    session.commit()
    session.refresh(album)
    return album

@app.delete("/api/albums/{id}")
def delete_album(id: int, session: Session = Depends(get_session), token: TokenData = Depends(verify_token)):
    album = session.get(Album, id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    session.delete(album)
    session.commit()
    return {"message": "Album deleted successfully"}

# --- Endpoints Genres ---
@app.get("/api/genres/")
def get_genres(session: Session = Depends(get_session)):
    return session.exec(select(Genre)).all()

@app.put("/api/genres/{id}")
def update_genre(id: int, genre_data: Genre, session: Session = Depends(get_session), token: TokenData = Depends(verify_token)):
    genre = session.get(Genre, id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    for key, value in genre_data.obj.model_dump(exclude_unset=True).items():
        setattr(genre, key, value)
    session.commit()
    session.refresh(genre)
    return genre

# --- Endpoints Artists ---
@app.get("/api/artists/{id}/songs")
def get_artist_songs(id: int, session: Session = Depends(get_session)):
    # Requête pour trouver les morceaux liés à cet artiste
    tracks = session.exec(
        select(Track).join(TrackArtist).where(TrackArtist.artist_id == id)
    ).all()
    
    if not tracks:
        raise HTTPException(status_code=404, detail="No songs found for the given artist")
    
    return tracks

@app.put("/api/artists/{id}")
def update_artist(id: int, artist_data: Artist, session: Session = Depends(get_session), token: TokenData = Depends(verify_token)):
    artist = session.get(Artist, id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    for key, value in artist_data.obj.model_dump(exclude_unset=True).items():
        setattr(artist, key, value)
    session.commit()
    session.refresh(artist)
    return artist

@app.delete("/api/artists/{id}")
def delete_artist(id: int, session: Session = Depends(get_session), token: TokenData = Depends(verify_token)):
    artist = session.get(Artist, id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    session.delete(artist)
    session.commit()
    return {"message": "Artist deleted successfully"}

# --- Endpoints Users ---
@app.post("/api/users/signup")
def signup(user: User, session: Session = Depends(get_session)):
    # Vérifiez si l'utilisateur ou l'email existe déjà
    existing_user = session.exec(select(User).where(User.username == user.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    existing_email = session.exec(select(User).where(User.email == user.email)).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hachez le mot de passe avant l'insertion
    user.password = hash_password(user.password)

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
    session: Session = Depends(get_session)
):
    user = session.exec(select(User).where(User.username == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.delete("/api/users/{id}")
def delete_user(id: int, session: Session = Depends(get_session), token: TokenData = Depends(verify_token)):
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": "User deleted successfully"}

