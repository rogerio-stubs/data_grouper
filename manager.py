import sys
import multiprocessing
import listening_keyboard as lk
import listening_mouse as lm

mouse_thread = multiprocessing.Process(target=lm.mouse)
keyboard_thread = multiprocessing.Process(target=lk.keyboard)

def start():
    keyboard_thread.start()
    mouse_thread.start()

def finish():
    if keyboard_thread.is_alive() and mouse_thread.is_alive():
        mouse_thread.kill()
        keyboard_thread.kill()
    sys.exit()
