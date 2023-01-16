import math
import random
import threading
import time


# def summ(a, b):
#     return  a + b
#
# def main2():
#     print('start t1')
#     print(f'summa: {summ(5,5)}')
#     print('end t1')
#
# th1 = threading.Thread(target=main2).start()
# print(f'main thread ')

# def thread_func(name):
#     print(f'Thread: {name} start')
#     time.sleep(2)
#     print(f'Thread: {name} finished')
#
# def x1(i):
#     print('x1')
#
# def x2(i):
#     print('x2')
#
# def x3(i):
#     print('x3')
#
# thread = []
# func = [x1,x2,thread_func]
#
# for i in range(3):
#     print(f'Main: create and start thread {i}')
#     t = threading.Thread(target=func[i], args=(i,))
#     thread.append(t)
#
# for i  in thread:
#     i.start()
#
# print(f'end main thread')
##TODO daemno
# def timer():
#     counter = 0
#     while True:
#         counter +=1
#         time.sleep(1)
#         print(f'Gone {counter}')
#
# t = threading.Thread(target=timer,daemon=True)
# t.start()
# input('Enter Y to exit: ')

# def myfunc(a,b):
#     print('sum: ', a+b)
#
# t = threading.Thread(target=myfunc, args=(2, 3), daemon=True)
# t.start()
# t.join()
# while True:
#     if t.is_alive():
#         print('in progress')
#     else:
#         print('ended')
#     time.sleep(2)

# def thread_func(name):
#     print(f'Thread: {name} start')
#     time.sleep(2)
#     print(f'Thread: {name} finished')
#
# def x1(i):
#     print('x1')
#
# def x2(i):
#     print('x2')
#
#
# thread = []
#
# for i in range(3):
#     print(f'Main: create and start thread {i}')
#     t = threading.Thread(target=thread_func, args=(i,))
#     thread.append(t)
#     t.start()
#
# for i, th  in enumerate(thread):
#     print(f'Main: before joinig thread {i}')
#     th.join()
#     print(f'Main: thread {i} done')
#
# print(f'end main thread')

##TODO Barrier
# b = threading.Barrier(2)
# ls = []
#
# def func1():
#     global ls
#     time.sleep(2)
#     for i in range(10):
#         ls.append(random.randint(1,10))
#     print('t1 fiil list')
#     b.wait()
#
# def func2():
#     global ls
#     # b.wait()
#     print(ls,'\t')
#
# t1 = threading.Thread(target=func1).start()
# t2 = threading.Thread(target=func2).start()
# # b.wait()

##TODO Semaphore
# s = threading.Semaphore(3)
#
# def func1(name):
#     s.acquire()
#
#     for i in range(0,10000):
#         for j in range(0,10):
#             n = j*i
#
#     for i in range(3):
#         print(f'hello - {name}')
#         s.release()
#
# t1 = threading.Thread(target=func1, args=('thread-1',)).start()
# t2 = threading.Thread(target=func1, args=('thread-2',)).start()
# t3 = threading.Thread(target=func1, args=('thread-3',)).start()
# t4 = threading.Thread(target=func1, args=('thread-4',)).start()
##TODO Timer
# def func1():
#     print('tic-tak')
#
# t = threading.Timer(4, func1)
# t.start()

##TODO Event
# e = threading.Event()
#
# def f():
#     time.sleep(1)
#     e.set()
#     print('t1')
#
# t1 = threading.Thread(target=f).start()
# print('t2')
# print(e.is_set())
# e.wait()
# print(e.is_set())
# e.clear()
# print(e.is_set())

##TODO Event class
# class MyThread(threading.Thread):
#     def __init__(self,e):
#         super().__init__()
#         self.stopped = e
#
#     def run(self) -> None:
#         while not self.stopped.wait(1):
#             print('my action')
#
# stop = threading.Event()
# t = MyThread(stop)
# t.start()
#
# time.sleep(5)
# stop.set()

#TODO multiprocessing
from multiprocessing import*
import os
from timeit import  default_timer as timer
# print('Number of cpu:', multiprocessing.cpu_count())

# def func():
#     print('Hello from child Process')
#
# if __name__ == '__main__':
#     print('Hello from main Process')
#     print(f'Main PID: {os.getpid()}')
#
#     proc = Process(target=func)
#     proc.start()
#     print(f'Process PID: {os.getpid()}')
#     print()
##TODO join
# def func():
#     print('Hello from child Process')
#
#
# if __name__ == '__main__':
#     print('Hello from main Process')
#
#     proc = Process(target=func)
#     proc.start()
#     print(f'Proc is_alive status: {proc.is_alive()}')
#     proc.join()
#     print('Goodbye')
#     print(f'Proc is_alive status: {proc.is_alive()}')
##TODO class

# class MyProc(Process):
#     def __init__(self, limit):
#         Process.__init__(self)
#         self._limit = limit
#
#     def run(self):
#         for i in range(self._limit):
#             print(f'From CustomerProcess: {i}')
#             time.sleep(0.5)
#
# if __name__ == "__main__":
#     cpr = MyProc(3)
#     cpr.start()

##TODO deamon
#
# def func(name):
#     counter = 0
#     while  True:
#         print(f'proc {name}, counter = {counter}')
#         counter += 1
#         time.sleep(0.1)
#
# if __name__ == "__main__":
#     proc1 = Process(target=func, args=('proc1',), daemon=True)
#
#     proc2 = Process(target=func, args=('proc2',))
#     proc2.daemon = True
#
#     proc1.start()
#     proc2.start()
#     time.sleep(0.3)

##TODO Queue

# def func1(q):
#
#     q.put([22,None, 'hello'])
#
# def func2(q):
#     print(q.get())
#
# def main():
#     q = Queue()
#     p2 = Process(target=func2, args=(q,)).start()
#     p1 = Process(target=func1, args=(q,)).start()
#
# if __name__ == '__main__':
#     main()

##TODO Pool
#
# def func(number):
#     time.sleep(3)
#     return  number ** 2
#
# def main():
#     start = timer()
#     print('Start main')
#
#     numbers = [1, 2, 3]
#     with Pool() as pool:
#         # print(pool.map(func,numbers))
#         res = pool.map(func,numbers)
#         print(res)
#     end =timer()
#     print(f'end  - {end -start}')
#
# if __name__ == '__main__':
#     main()

user_path = 'thread.txt'
if not os.path.exists(user_path):
    print('File not found')
    exit(0)


def func1():
    with open(user_path, 'w') as f:
        f.write(' '.join(map(str, [random.randint(0, 10) for _ in range(10)])))

    print('List generate')


def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

def func2():
    res = []
    with open(user_path, 'r') as f:
        data = f.readline()
        for i in data:
            num = list(map(int, list(i.replace(' ',''))))
            for x in num:
                res.append(x) if is_prime(int(x)) else False
    with open('find.txt','w') as f:
        f.write(' '.join(list(map(str,res))))

    print('Simple value finished')


def func3():
    res = []
    with open(user_path, 'r') as f:
        data = f.readline()
        num = list(map(int, list(data.replace(' ', ''))))
        res = list(map(lambda x: math.factorial(x),num))

    with open('fact.txt', 'w') as f:
        f.write(' '.join(list(map(str, res))))
    print('Factorial finished')




thread1 = threading.Thread(target=func1)
thread1.start()

thread2 = threading.Thread(target=func2)
thread2.start()
thread3 = threading.Thread(target=func3)
thread3.start()
