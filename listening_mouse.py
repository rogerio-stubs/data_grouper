from pynput.mouse import Listener
import controller as ct

height = list()
width = list()

def on_click(x, y, button, pressed):
    if pressed is True:
        height.append(x)
        width.append(y)
    else:
        height.append(x)
        width.append(y)
        ct.set_postion(height, width)
        height.clear()
        width.clear()

def mouse():
    with Listener(on_click=on_click) as listener:
        listener.join()
