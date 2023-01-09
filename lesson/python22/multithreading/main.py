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

b = threading.Barrier(2)
ls = []

def func1():
    global ls
    time.sleep(2)
    for i in range(10):
        ls.append(random.randint(1,10))
    print('t1 fiil list')
    b.wait()

def func2():
    global ls
    b.wait()
    print(ls,'\t')

t1 = threading.Thread(target=func1).start()
t2 = threading.Thread(target=func2).start()
# b.wait()