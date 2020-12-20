from pymongo import MongoClient

client = MongoClient('localhost', 27017)
# cliente = MongoClient('mongodb://localhost:27017/')
database = client.data_server

documentations = database.documentations

agents = database.agents

chats = database.chats


# from database.connection import information