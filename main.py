# threading

import threading
import time


def wake_up():
    time.sleep(5)
    print('You brush your teeth')


x = threading.Thread(target=wake_up, args=())
x.start()
