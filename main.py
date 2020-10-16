import threading
import listening_keyboard as lk
import listening_mouse as lm
import screen

if __name__ == "__main__":
    keyboard_thread = threading.Thread(target=lk.keyboard)
    keyboard_thread.start()

    mouse_thread = threading.Thread(target=lm.mouse)
    mouse_thread.start()
