import sys
import threading
import listening_keyboard as lk
import listening_mouse as lm

mouse_thread = threading.Thread(target=lm.mouse)
keyboard_thread = threading.Thread(target=lk.keyboard)

def start():
    keyboard_thread.start()
    mouse_thread.start()

def finish():
    keyboard_thread.join()
    mouse_thread.join()
    sys.exit()


