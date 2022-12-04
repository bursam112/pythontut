# threading.Thread(target=func, args=(first_arg, ...)
import threading
import time


def brush_teeth():
    time.sleep(4)
    print('I, squeaky clean!')


def go_pee():
    time.sleep(3)
    print('Soothing')


def get_dressed():
    time.sleep(5)
    print('Drippy')


x = threading.Thread(target=brush_teeth, args=())
x.start()

y = threading.Thread(target=go_pee, args=())
y.start()

z = threading.Thread(target=get_dressed, args=())
z.start()

print('Threads :', threading.active_count())

x.join()
y.join()
z.join()

print('Threads :', threading.active_count())
print(time.perf_counter())

