from pynput.keyboard import Listener
from view import screen
from controller import controller

def key_action(key):
    key_data = str(key)

    if key_data == 'Key.ctrl_l' or key_data == 'Key.ctrl_r':
        print('Pergunta')
        controller.agent()
        controller.get_information(True)

    if key_data == 'Key.esc' or key_data == 'Key.esc':
        print('Resposta')
        controller.agent()
        controller.get_information(False)

    if key_data == 'Key.alt_l':
        print('Abrir busca')
        screen.Search()

def keyboard():
    with Listener(on_press=key_action) as listener:
        listener.join()

