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