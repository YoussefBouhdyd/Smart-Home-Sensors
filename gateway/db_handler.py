from pymongo import MongoClient
client = MongoClient("mongodb+srv://projetiot:PigZNQGf6lPy97Pk@projetiot.mwwvunz.mongodb.net/")
db = client["Testing"] 
collection = db["Room-Agents"] 

