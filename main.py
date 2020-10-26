# import threading
# import listening_keyboard as lk
# import listening_mouse as lm
# import screen as sc
import manager as mn


if __name__ == "__main__":
    # mouse_thread = threading.Thread(target=lm.mouse)
    # keyboard_thread = threading.Thread(target=lk.keyboard)
    # keyboard_thread.start()
    # mouse_thread.start()
    # sc.Manager()
    mn.start()