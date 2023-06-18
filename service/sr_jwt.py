from datetime import datetime, timedelta
from jose import JWTError, jwt

class ServiceJWT:
  def __init__(self) -> None:
    self.SECRET_KEY = "14fe5656c4b589be5fcf5bb436f2507c2c82d4bc4ab6b763b59f087e0b95ddff"
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