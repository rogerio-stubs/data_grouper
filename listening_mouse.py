from pynput.mouse import Listener
import controller as ct


def on_click(x, y, button, pressed):
    ct.set_postion(x, y)

def mouse():
    with Listener(on_click=on_click) as listener:
        listener.join()
