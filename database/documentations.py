from pymongo import MongoClient
from database.connection import documentations

def insert_documentation(data):
    documentations.insert_one(data)