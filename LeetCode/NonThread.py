from threading import Thread
import random
import time

def some_func():
    time.sleep(random.random())

prev_time = time.time()
while True:
    some_func()
    print(time.time() - prev_time)
    prev_time = time.time()

    time.sleep(5)