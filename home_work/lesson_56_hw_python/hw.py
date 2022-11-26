class Node:
    def __init__(self,item):
        self.i = item
        self.n = None
        self.p = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.limit = 3

    def push(self,x):
        node = Node(x)
        if node is None or self.limit == self.size:
            print('Heap Overflow')
            return

        node.n = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            print('Heap Overflow')
            return

        self.top = self.top.n
        self.size -= 1

    def size(self):
        return self.size

    def empty(self):
        return  self.top is None

    def full(self):
        return True if self.limit == self.size else False

    def clear(self):
        self.top = None
        # self.top.n = None

    def get_item(self):
        if not self.empty():
            return self.top.i
        else:
            print('Stavk empty')

    def travel(self):
        cur = self.top
        while cur is not None:
            print(f'{cur.i} -> ', end='')
            cur = cur.n
        print('None')



s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.travel()
s.pop()
# s.push(20)

s.travel()

#
# print('Work with the stack')
# print('1.Add in stack\n'
#       '2.Push from stack\n'
#       '3.Size the stack\n'
#       '4.Check for emptiness\n'
#       '5.check for fulless\n'
#       '6.Clear  stack\n'
#       '7.Get item\n'
#       '8.Exit')
#
# choose = int(input('Choose: '))
#
# while choose != 8:
#
#     if choose == 1:
#         pass
#     elif choose == 2:
#         pass
#     elif choose == 3:
#         pass
#     elif choose == 3:
#         pass
#     elif choose == 4:
#         pass
#     elif choose == 5:
#         pass
#     elif choose == 6:
#         pass
#     elif choose == 7:
#         pass
#     else:
#         print('Inccorect value')
