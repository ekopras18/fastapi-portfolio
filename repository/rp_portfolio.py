from fastapi import Depends
from pydantic import parse_obj_as
from pymongo.database import Database
from config.config import db_connection 
from models.md_portfolio import Portfolio
from dto.dt_portfolio import InputPortfolio
from typing import List


class RepositoryPortfolio:
  def __init__(self, db:Database = Depends(db_connection)):
    self.repository = db.get_collection("portfolio")
    
  def insert(self, new_portfolio: InputPortfolio):
    return self.repository.insert_one(new_portfolio.dict())

  def get(self, match_filter: dict):
    result = self.repository.find(match_filter)
    result = list(result)
    return parse_obj_as(List[Portfolio], result)
  