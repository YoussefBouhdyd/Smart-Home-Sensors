from pymongo import MongoClient
client = MongoClient("mongodb+srv://projetiot:PigZNQGf6lPy97Pk@projetiot.mwwvunz.mongodb.net/")
db = client["Database"] 
collection = db["Motion"] 

