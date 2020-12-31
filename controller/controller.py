from database import chats
from view import screen
import pyautogui
import time
import win32clipboard

visitor_name = list()
visitor = dict()
chats_list = list()
json_list = dict()
position = list()
agent_id = 666

# Não está funcionando
def set_agent(id):
    # global agent_id
    agent_id = id

def agent():
    global chats_list
    # global agent_id
    chats_list = chats.db_chats(agent_id)

def get_client():
    # por enquanto ele simplesmente limpa o array
    visitor_name.clear()
    for visitante in chats_list:
        visitor.update({visitante.get("id_visitante"): visitante.get("nome_visitante")})
        visitor_name.append(visitante.get("nome_visitante"))
    return visitor

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
    print(f"informação copiada: {data_copy}")
    screen.Selector()


def create_json():
    pass