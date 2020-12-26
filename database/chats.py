from pymongo import MongoClient
from database.connection import chats

# agent_id = 666
visitante_name = list()
chat_list = list()


def db_chats(agent_id):
    for chat in chats.find({"_id": agent_id}, {"atributo": 0}):
        return chat.get("chats")

