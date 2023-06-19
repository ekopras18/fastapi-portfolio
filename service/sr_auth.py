from fastapi import Depends, HTTPException
from dto.dt_base import TokenData
from dto.dt_users import InputLogin
from service import sr_security
from service.sr_jwt import ServiceJWT
from repository.rp_auth import RepositoryAuth


class ServiceAuth:
  def __init__(self, repository: RepositoryAuth = Depends(), sr_jwt: ServiceJWT = Depends()):
    self.repository = repository
    self.security = sr_security
    self.jwt = sr_jwt
    
  # def insert(self, new_users: InputUsers):
  #   check_email = self.repository.find_user_by_email(new_users.email)
  #   if check_email is not None:
  #     # raise HTTPException(400, detail="Email already exists")
  #     return None
    
  #   # hash password
  #   new_users.password = self.security.get_password_hash(new_users.password)
    
  #   return self.repository.insert(new_users)
  
  def login_user(self, input_login: InputLogin):
    found_user = self.repository.find_user_by_email(input_login.email)
    # if user not found
    if found_user is None:
      # raise HTTPException(401, detail="Invalid email")
      return None
    
    if not self.security.verify_password(input_login.password, found_user.password):
      # raise HTTPException(401, detail="Invalid password")
      return None
    
    # generate jwt token
    # jwt_token = self.jwt.create_access_token(data={"userid": str(found_user.id),"email": found_user.email})
    jwt_token = self.jwt.create_access_token(data=TokenData(userid=str(found_user.id),email=found_user.email))
    return jwt_token