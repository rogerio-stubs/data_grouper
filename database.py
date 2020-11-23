from pymongo import MongoClient

client = MongoClient('localhost', 27017)
# cliente = MongoClient('mongodb://localhost:27017/')
database = client.dataGrouperDB
information = database.dataDB


def saved_question(data):
    param = 'Pergunta: ' + ' '.join(str(data).split()) + '\n'
    inserting_data(param)

def saved_answer(data):
    param = 'Resposta: ' + ' '.join(str(data).split()) + '\n'
    inserting_data(param)

def inserting_data(information):
    pass
    