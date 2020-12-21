from pymongo import MongoClient
from database.connection import chats

def chats_list(agent_id):
    for chat in chats.find({"_id": agent_id}, {"atributo": 0}):
        return chat