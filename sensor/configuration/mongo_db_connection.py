import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
from sensor.constant.env_variable import MONGODB_URL_KEY
import os
ca=certifi.where()

class MongoDBClient:
    client = None
    def __init__(self,database_name= DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url= "mongodb+srv://ganeshkumarjasti:ganesh0819@cluster0.echtgo5.mongodb.net/?retryWrites=true&w=majority"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e
           
