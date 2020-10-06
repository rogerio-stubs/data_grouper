from pynput.keyboard import Listener
import screen as sc
import controller as ct

def key_action(key):
    key_data = str(key)

    if key_data == 'Key.ctrl_l' or key_data == 'Key.ctrl_r':
        print('Pergunta')
        ct.get_information(True)
        sc.Selector()

    if key_data == 'Key.esc' or key_data == 'Key.esc':
        print('Resposta')
        ct.get_information(False)
        sc.Selector()

    if key_data == 'Key.alt_l':
        print('Abrir busca')
        sc.Search()

def keyboard():
    with Listener(on_press=key_action) as listener:
        listener.join()
