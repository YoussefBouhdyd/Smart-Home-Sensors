import os
from pymongo import MongoClient

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

if load_dotenv:
    load_dotenv()
mongo_uri = os.getenv("MONGODB_URI")

if not mongo_uri:
    raise RuntimeError("Missing MONGODB_URI environment variable.")

client = MongoClient(mongo_uri)
db = client["DataSensor"] 
collection = db["Data"] 


db = client["Testing"]
collection = db["Room-Agents"]

# Read all documents from the collection
documents = collection.find()
for doc in documents:
    print(f"room: {doc['id']} climat status : {doc['clima']} Window status: {doc['window']}")

