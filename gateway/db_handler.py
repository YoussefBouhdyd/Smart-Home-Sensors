from pymongo import MongoClient
uri = "mongodb+srv://Test:T5doQSlNIkrkoyzI@sensors.ctflhib.mongodb.net/?appName=Sensors"
client = MongoClient(uri)

print(client.list_database_names())
