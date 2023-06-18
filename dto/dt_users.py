from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from models.enum_category import Category

class InputUsers(BaseModel):
    name: str
    username: str
    email: str
    password: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    
class InputLogin(BaseModel):
    email: str = "ekopras@gmail.com"
    password: str = "1234"

