import pyautogui
import time
import database as data
import win32clipboard

index = list()
index.append('Chat')
position = list()

def get_name():
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
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    win32clipboard.OpenClipboard()
    data_copy = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    if question is True:
        data.saved_question(data_copy)
    else:
        data.saved_answer(data_copy)


def new_service():
    pass

def completed_service():
    pass
