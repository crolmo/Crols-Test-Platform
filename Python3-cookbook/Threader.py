from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process

def test(n):
    print(n)
    import time
    time.sleep(n)


if __name__ == '__main__':
    for i in range(10):
        t = Process(target=test,args=(i,))
        t.start()
        t.join()