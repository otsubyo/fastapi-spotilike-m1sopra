# --- Configuration de la base de données ---
import bcrypt
from sqlmodel import SQLModel, Session, create_engine


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