import pymongo

client = pymongo.MongoClient("mongodb+srv://mrepras:dXNVcUjJZDHPAPes@mre.jkgdtj3.mongodb.net/?retryWrites=true&w=majority")
try:
    db = client.get_database("fastapi-portfolio")
    print("DB : Successfully connected to MongoDB!")
except Exception as e:
    print("DB : Error Connection to MongoDB!")
    
def db_connection():
    return db