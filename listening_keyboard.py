from pynput.keyboard import Listener
import screen as sc
import controller as ct

def key_action(key):
    key_data = str(key)

    if key_data == 'Key.ctrl_l' or key_data == 'Key.ctrl_r':
        print('Pergunta')
        # web.get_information()
        sc.Selector()

    if key_data == 'Key.shift' or key_data == 'Key.shift_r':
        print('Resposta')
        sc.Selector()

    if key_data == 'Key.alt_l':
        print('Abrir busca')
        sc.Search()

    if key_data == 'Key.esc':
        print('FINALIZAR')

def keyboard():
    with Listener(on_press=key_action) as listener:
        listener.join()
