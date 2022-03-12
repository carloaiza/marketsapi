from pymongo import MongoClient

class MongoApi:
    def __init__(self,data):
        self.client= MongoClient("mongodb://localhost:5002")
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]

    def read(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item !='_id' } for data in documents]
        return output