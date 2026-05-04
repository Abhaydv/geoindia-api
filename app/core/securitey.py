from passlib.context import CryptContext
from jose import jwt
import datetime

SECRET_KEY = "secret123"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

def create_token(data: dict):
    to_encode = data.copy()
    to_encode.update({
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    })
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)