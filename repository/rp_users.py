from fastapi import Depends
from pydantic import parse_obj_as
from pymongo.database import Database
from config.config import db_connection 
from models.md_users import Users
from dto.dt_users import InputUsers
from dto.dt_users import InputLogin
from typing import List


class RepositoryUsers:
  def __init__(self, db:Database = Depends(db_connection)):
    self.repository = db.get_collection("users")
    
  def insert(self, new_users: InputUsers):
    return self.repository.insert_one(new_users.dict())
  
  def find_user_by_email(self, email: str):
    result = self.repository.find_one({"email": email})
    if result is not None:
      return Users.parse_obj(result)
    return None
  
  def find_user(self, input_login: InputLogin):
    result = self.repository.find_one({"email": input_login.email, "password": input_login.password})
    if result is not None:
      return Users.parse_obj(result)
    return None