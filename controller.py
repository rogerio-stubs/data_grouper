from pynput.keyboard import Listener
import threading
import pyautogui as py
import win32api as wp
import screen as sc
import web_communication as web


def action(key):
    key_data = str(key)

    if key_data == 'Key.ctrl_l' or key_data == 'Key.ctrl_r':
        print('Pergunta')
        web.get_information()
        sc.Selector()

    if key_data == 'Key.shift' or key_data == 'Key.shift_r':
        print('Resposta')
        sc.Selector()

    if key_data == 'Key.alt_l':
        print('Abrir busca')
        sc.Search()

    if key_data == 'Key.esc':
        print('FINALIZAR')

def key_listener():
    with Listener(on_press=action) as l:
        l.join()

def click_listener():
    state_left = wp.GetKeyState(0x01)
    start = 0
    final = 0
    while start == 0 or final == 0:
        a = wp.GetKeyState(0x01)

        if a != state_left:
            state_left = a
            if a < 0:
                start = py.position()
            else:
                final = py.position()
    print(start, final)
    web.set_postion(start, final)
    click_listener()

if __name__ == "__main__":
    t1 = threading.Thread(target=key_listener)
    t1.start()

    t2 = threading.Thread(target=click_listener)
    t2.start()
 