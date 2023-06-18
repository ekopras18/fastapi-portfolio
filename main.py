from fastapi import FastAPI
from router.rt_portfolio import r_portfolio
from router.rt_users import r_users

app = FastAPI(title="REST API Portfolio", description="This is my portfolio", version="1.0.0", docs_url="/", redoc_url="/redocs", openapi_url="/openapi.json")

app.include_router(r_users)
app.include_router(r_portfolio)


# from fastapi import FastAPI
# from pydantic import BaseModel,Field, validator, parse_obj_as
# from datetime import datetime
# from typing import Optional
# from enum import Enum
# import pymongo
# from fastapi.encoders import jsonable_encoder
# from bson import ObjectId
# from typing import List

# app = FastAPI()

# class Category(str, Enum):
#     gov = "Government"
#     priv = "Private Project"
#     learn = "Self-directed learning"

# class InputPortfolio(BaseModel):
#     name: str
#     description: Optional[str]
#     category: Category
#     image: str
#     date: Optional[datetime] = datetime.now()
#     url: str

# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid objectid")
#         return ObjectId(v)

#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(type="string")

# class Portfolio(BaseModel):
#     id: PyObjectId = Field(default_factory=PyObjectId,alias="_id")
#     name: str
#     description: Optional[str]
#     category: Category
#     image: str
#     date: Optional[datetime] = datetime.now()
#     url: str

#     class Config:
#         json_encoders = {ObjectId: str}

# client = pymongo.MongoClient("mongodb+srv://mrepras:dXNVcUjJZDHPAPes@mre.jkgdtj3.mongodb.net/?retryWrites=true&w=majority")
# try:
#     database = client.get_database("fastapi-portfolio")
#     db = database.get_collection("portfolio")
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print("Error Connection DB =", e)


# @app.get("/",tags=["Introduction"])
# def introduction():
#     return {
#         "App": "Rest API Portfolio",
#         "Description": "This is my portfolio",
#         "Author": "Eko Prasetio",
#         "Version": "1.0.0",
#         "Url" : "http://127.0.0.1:8000/api/v1/portfolio"
#         }

# # tags=["Portfolio"],response_description="List all students", response_model=List[InputPortfolio]
# @app.get("/api/v1/portfolio", )
# def get_portfolio(category: Optional[Category] = None):
#     if category is not None:
#         match_filter = {"category": category}
#     else:
#         match_filter = {}
#     result = db.find(match_filter)
#     result = list(result)
#     if len(result) == 0:
#         return {
#             "Status": False,
#             "Code": 404,
#             "Message": "Data not found",
#             "Data": []
#         }
#     else:
#         return {
#             "Status": True,
#             "Code": 200,
#             "Message": "Data found",
#             "Data": parse_obj_as(List[Portfolio], result)
#         }
        
# @app.post("/api/v1/portfolio")
# def insert_portfolio(input: InputPortfolio):
#     check = db.insert_one(input.dict())
    
#     if check.inserted_id is None:
#         return {
#             "Status": False,
#             "Code": 500,
#             "Message": "Data failed to insert",
#             "Data": input.dict()
#         }
#     else:
#         return {
#             "Status": True,
#             "Code": 200,
#             "Message": "Data inserted successfully",
#             "Data": input.dict()
#         }