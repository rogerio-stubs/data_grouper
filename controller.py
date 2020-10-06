from bs4 import BeautifulSoup
import win32clipboard as clipboard
import pyautogui 
import pyperclip
import time
import database as data

index = list()
position = list()

def get_name():
    # devolver para a interface o nome dos atendimentos
    return index

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
    # falta apagar o valor na área de transferência 
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.001)
    data_copy = pyperclip.paste()
    if question is True:
        data.saved_question(data_copy)
        print('question')
    else:
        data.saved_answer(data_copy)


def new_service():
    pass

def completed_service():
    # quando finaliza um chat
    pass
