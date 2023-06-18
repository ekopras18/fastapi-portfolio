from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from models.enum_category import Category

class InputPortfolio(BaseModel):
    name: str
    description: Optional[str]
    category: Category
    image: str
    date: Optional[datetime] = datetime.now()
    url: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()