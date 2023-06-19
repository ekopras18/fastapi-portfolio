from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from dto.dt_base import TokenData
from service import sr_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth")

def get_current_user(
  token: Annotated[str, Depends(oauth2_scheme)],
  service_jwt: sr_jwt.ServiceJWT = Depends()
  ):
    # return TokenData.parse_obj(service_jwt.decode_token(token))
    return service_jwt.decode_token(token)

