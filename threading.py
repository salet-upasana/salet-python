import threading
import time
import queue

"""def hello():
    print("thread called")
    print("thread name is :"+t1.getName())

    t1.setName("first thread")
    print("new name is:"+t1.getName())
t1=threading.Thread(name="my thread",target=hello)
t1.start()"""


"""class mythread(threading.Thread):
    def run(self):
        print("start:"+self.getName())
        for i in range(1,11):
            time.sleep(1)
            print(i)

            print("stop:"+self.getName())

t=mythread(name="mythread")
t.start()"""

"""class MyThread(threading.Thread):
    def run(self):
        l1.acquire()
        print("start"+self.name)
        for i in range(1,6):
            print(self.getName()+"-"+str(i))
            time.sleep(1)
        print("stop"+self.name)
        l1.release()
l1=threading.Lock()
t1=MyThread(name="my thread1")
t2=MyThread(name="my thread2")
t1.start()
t2.start()"""

class MyThread():
    def __init__(self,priority,threadname):
        self.priority=priority
        self.threadname=threadname
        print("start thread:"+self.threadname)

    def __gt__(self,other):
            return other.priority>self.priority
q=queue.PriorityQueue()

t1=MyThread(12,"first thread")
t2=MyThread(21,"second thread")
t3=MyThread(34,"thrid thread")
q.put(t1)
q.put(t2)
q.put(t3)

while not q.empty():
    next_thread=q.get()
    print("active thread :"+next_thread.threadname)



