import threading
import time

def func_1():
    for i in range (1, 10):
        print (i)
        time.sleep (1)

def func_2():
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for x in alp:
        print (x)
        time.sleep (1)

thr_1 = threading.Thread(target = func_1)
thr_2 = threading.Thread(target = func_2)

thr_1.start()
thr_2.start()

thr_1.join()
thr_2.join()