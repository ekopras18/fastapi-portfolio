from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .enum_category import Category
from .md_base import PyObjectId

class Users(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId,alias="_id")
    name: str
    username: str
    email: str
    password: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        json_encoders = {ObjectId: str}