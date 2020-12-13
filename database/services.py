from pymongo import MongoClient
from database.connection import information

def retorno():
    service = information.find()
    return service