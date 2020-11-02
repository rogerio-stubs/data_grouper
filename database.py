import os.path

def saved_question(data):
    param = 'Pergunta: ' + ' '.join(str(data).split()) + '\n'
    inserting_data(param)

def saved_answer(data):
    param = 'Resposta: ' + ' '.join(str(data).split()) + '\n'
    inserting_data(param)

def inserting_data(information):
    if os.path.isfile('C:/Development/BD_grouper/novo-arquivo.txt') is False:
        archive = open('C:/Development/BD_grouper/novo-arquivo.txt', 'w')
        archive.writelines(information)
        archive.close()
    else:
        archive = open('C:/Development/BD_grouper/novo-arquivo.txt', 'r')
        content = archive.readlines()
        content.append(information)
        archive = open('C:/Development/BD_grouper/novo-arquivo.txt', 'w')
        archive.writelines(content)

