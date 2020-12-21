from pymongo import MongoClient
from database.connection import agents

def login(user, password):
    user_id = -1
    acesso = "Acesso negado"
    for user_id in agents.find({"user": user, "password": password}, {"atributo":0}):
        if user_id != -1:
            acesso = user_id.get("_id")

    return acesso