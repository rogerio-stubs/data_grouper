import threading
import listening_keyboard as lk
import listening_mouse as lm


if __name__ == "__main__":
    t1 = threading.Thread(target=lk.keyboard)
    t1.start()

    t2 = threading.Thread(target=lm.mouse)
    t2.start()
