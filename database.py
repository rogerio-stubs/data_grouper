index = list()
position = list()

def index_atts():
    # devolver para a interface o nome dos atendimentos
    return index

def create(name):
    # cria uma nova instância no data
    index.append(name)

def delete():
    #  salva no banco
    #  finaliza a instancia no data
    pass

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

def get_position():
    return position[0], position[1]
