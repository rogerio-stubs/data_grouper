import win32clipboard as clipboard

index = list()
position = list()

def get_name():
    # devolver para a interface o nome dos atendimentos
    return index

def set_postion(start, final):
    position.clear()
    position.append(100)
    position.append(100)

def get_position():
    return position[0], position[1]

def get_information():
    # buscar a informação no Win e salve em cache
    # assim que um index for pressionado salva o chache no dicionario
    # clipboard.OpenClipboard()
    # data = clipboard.GetClipboardData()
    # clipboard.CloseClipboard()
    # print(data)
    pass

def new_service(name):
    # quando detecta um novo chat
    index.append(name)

def completed_service():
    # quando finaliza um chat
    pass
