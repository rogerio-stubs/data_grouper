from controller import listen_mouse, listen_keyboard
import sys
import multiprocessing

mouse_thread = multiprocessing.Process(target=listen_mouse.mouse)
keyboard_thread = multiprocessing.Process(target=listen_keyboard.keyboard)

def start():
    keyboard_thread.start()
    mouse_thread.start()

def finish():
    if keyboard_thread.is_alive() and mouse_thread.is_alive():
        mouse_thread.kill()
        keyboard_thread.kill()
    sys.exit()
