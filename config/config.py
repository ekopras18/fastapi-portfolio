import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGO_URI"))
try:
    db = client.get_database("fastapi-portfolio")
    print("DB : Successfully connected to MongoDB!")
except Exception as e:
    print("DB : Error Connection to MongoDB!")
    
def db_connection():
    return db