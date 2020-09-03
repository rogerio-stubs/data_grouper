import win32clipboard as clipboard

index = list()
position = list()

def get_name():
    # devolver para a interface o nome dos atendimentos
    return index

def set_postion(start, final):
    # Encontra a menor posição X e Y
    position.clear()
    if start[0] < final[0]:
        position.append(start[0])
    else:
        position.append(final[0])

    if start[1] < final[1]:
        position.append(start[1])
    else:
        position.append(final[1])

    # Valores não podem ser zerados
    if sum(position) == 0:
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
