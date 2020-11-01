data_dict = {}

def saved_question(data):
    data_dict.update({'pergunta': data})
    # print(data_dict)

def saved_answer(data):
    data_dict.update({'resposta': data})
    # print(data_dict)
    if len(data_dict) == 2:
        # print('entrou no if')
        # data_file = open("C:/data_grouper/data.txt", "a")
        # data_file.writelines(data_dict)
        data_dict.clear()