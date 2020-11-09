import os.path

def saved_question(data):
    param = 'Pergunta: ' + ' '.join(str(data).split()) + '\n'
    inserting_data(param)

def saved_answer(data):
    param = 'Resposta: ' + ' '.join(str(data).split()) + '\n'
    inserting_data(param)

def inserting_data(information):
    if os.path.isfile('C:/db-grouper/my-data.txt') is False:
        archive = open('C:/db-grouper/my-data.txt', 'w')
        archive.writelines(information)
        archive.close()
    else:
        archive = open('C:/db-grouper/my-data.txt', 'r')
        content = archive.readlines()
        content.append(information)
        archive = open('C:/db-grouper/my-data.txt', 'w')
        archive.writelines(content)

