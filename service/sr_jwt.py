from datetime import datetime, timedelta
from jose import JWTError, jwt
import os
from dotenv import load_dotenv

load_dotenv()

class ServiceJWT:
  def __init__(self) -> None:
    self.SECRET_KEY = os.getenv("API_KEY")
    self.ALGORITHM = "HS256"
    self.ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
  def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
    return encoded_jwt