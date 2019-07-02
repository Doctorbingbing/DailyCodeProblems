#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time
import threading
class Scheduler:
    def __init__(self):
        pass

    def starter(self,f,n):
        def sleeper(n):
            time.sleep(n)
            f()
            return
        t= threading.Thread(target=sleeper) 
        t.start()