from typing import Optional
from fastapi import Depends
from dto.dt_portfolio import InputPortfolio
from repository.rp_portfolio import RepositoryPortfolio
from models.enum_category import Category

class ServicePortfolio:
  def __init__(self, repository: RepositoryPortfolio = Depends()):
    self.repository = repository
    
  def get(self, category: Optional[Category] = None):
    match_filter = {}
    if category is not None:
      match_filter["category"] = category
      
    return self.repository.get(match_filter)
  
  def insert(self, new_portfolio: InputPortfolio):
    return self.repository.insert(new_portfolio)