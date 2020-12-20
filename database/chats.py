from pymongo import MongoClient
from database.connection import chats

def retorno():
    service = chats.find()
    return service