from bs4 import BeautifulSoup
import win32clipboard as clipboard
import pyautogui 
import pyperclip
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

def get_information():
    # falta apagar o valor na área de transferência 
    pyautogui.hotkey('ctrl', 'c')
    s = pyperclip.paste()
    print('retorno da área de tran sferência', s)

def new_service():
    # soup = BeautifulSoup(file:///C:/Development/code-test/web-teste/index.html)
    # index.append(name)
    pass

def completed_service():
    # quando finaliza um chat
    pass
