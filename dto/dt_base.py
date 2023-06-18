from pydantic import BaseModel
from typing import List, Optional, Any

class ResponseStandard(BaseModel):
  Status: bool
  Code: int
  Message: str
  
class ResponseWithData(BaseModel):
  Status: bool
  Code: int
  Message: str
  Data: Any = []
  
# class TokenData(BaseModel):
#   userid: str
#   email: str
  
class OutputAuth(BaseModel):
  access_token: str
  token_type: str