from database import chats, documentations
from view import screen
import pyautogui
import time
import win32clipboard


visitor = dict()
json_client = dict()
json_list = dict()

chats_list = list()
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
    visitor.clear()
    for visitante in chats_list:
        visitor.update({visitante.get("id_visitante"): visitante.get("nome_visitante")})
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
    global json_client
    json_client.clear()
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    win32clipboard.OpenClipboard()
    data_copy = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    data_copy = data_copy.strip()
    print(f"informação copiada: {data_copy}")
    json_client = {"Pergunta": data_copy} if question else {"Resposta": data_copy}
    screen.Selector()

def insert_client(id_client):
    json_list.update({"id": id_client, "documentation": json_client})

def finished_chats():
    documentations.insert_documentation(json_client)
