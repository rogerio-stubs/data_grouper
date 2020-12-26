from database import chats
import pyautogui
import time
import win32clipboard

visitor_name = list()
chats_list = list()
position = list()
agent_id = 666

# Não está funcionando
def set_agent(id):
    agent_id = id

def agent():
    global chats_list
    chats_list = chats.db_chats(agent_id)

def get_name():
    visitor_name.clear()  # por enquanto ele simplesmente limpa o array
    print(type(chats_list))
    for visitante in chats_list:
        print(f"visitante {visitante}")
        visitor_name.append(visitante.get("nome_visitante"))
    return visitor_name


def set_postion(height, width):
    position.clear()
    position.append(min(height))
    position.append(min(width))


def get_position():
    if len(position) == 0:
        position.append(100)
        position.append(100)

    return position[0], position[1]


def get_information(question):
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    win32clipboard.OpenClipboard()
    data_copy = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    if question is True:
        pass
        # data.saved_question(data_copy)
    else:
        pass
        # data.saved_answer(data_copy)


def new_service(agent_id):
    pass


def completed_service():
    pass