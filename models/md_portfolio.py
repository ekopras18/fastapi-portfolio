from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from datetime import datetime
from .enum_category import Category
from .md_base import PyObjectId

class Portfolio(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId,alias="_id")
    name: str
    description: Optional[str]
    category: Category
    image: str
    date: Optional[datetime] = datetime.now()
    url: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        json_encoders = {ObjectId: str}