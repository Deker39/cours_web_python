# list()
# dict()
#tuple()
# set()
# str()

# myList() -> get,append, remove, change, insert []
# LinkedList

# class Node:
#     def __init__(self,item):
#         self.item = item
#         self.next = None

#add - add on begin
#append - add to end
#insert - insert data in the position(its item)
#len - __len__, get size
#travel - show all list items
#remove - remove item
#search - search elem
#is_empty - is empty?

# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def add(self,item):
#         node = Node(item)
#         node.next,self.head  = self.head,node
#
#     def append(self,item):
#         node = Node(item)
#         if self.is_empty():
#             self.head = node
#         else:
#             cur = self.head
#             while cur.next:
#                 cur = cur.next
#             cur.next = node
#
#     def insert(self,position,item):
#         if position == 0:
#             self.add(item)
#         elif 0 < position < self.__len__():
#             node = Node(item)
#             count = 0
#             cur = self.head
#             while cur:
#                 if position == count + 1:
#                     node.next = cur.next
#                     cur.next = node
#                 cur = cur.next
#                 count +=1
#         else:
#             raise 'index out of range'
#
#     def remove(self,item):
#         cur= self.head
#         cur_pre = None
#         while cur:
#             if cur.item == item:
#                 if cur_pre is None:
#                     self.head = None
#                 else:
#                     cur_pre.next  = cur.next
#             cur_pre =  cur
#             cur = cur.next
#
#     def search(self,item):
#         cur = self.head
#         while cur:
#             if cur.item == item:
#                 return True
#             cur = cur.next
#         return False
#
#     def travel(self):
#         cur = self.head
#         while cur:
#             print(cur.item, end=' --> ')
#             cur = cur.next
#         print('None')
#
#     def __len__(self):
#         cur = self.head
#         count = 0
#         while cur:
#             count += 1
#             cur = cur.next
#         return  count
#
#     def is_empty(self):
#         return self.head is None
#
# # n1 = Node(5)
# # n2 = Node(10)
# # n3 = Node(15)
# #
# # n1.next = n2
# # n2.next = n3
# #
# # print(f'n1: {n1}, n2: {n2}, n3: {n3}')
# # print(n1.next.next.item)
#
# # cur = n1
# # while cur:
# #     print(cur.item)
# #     cur = cur.next
#
# ls = LinkedList()
#
# ls.add(5)
# ls.add(10)
# ls.append(8)
#
# ls.insert(2,6)
# ls.travel()
# ls.remove(6)
#
# ls.travel()
# print(ls.search(10))


# class Node:
#     def __init__(self,item):
#         self.item = item
#         self.next = None
#         self.previous = None

# n1 = Node(5)
# n2 = Node(10)
# n3 = Node(15)
#
# n1.next = n2
# n2.next = n3
#
# n3.previous = n2
# n2.previous = n1
#
# cur1 = n3
# while cur1 is not None:
#     print(cur1.item, '->', end=' ')
#     cur1 = cur1.previous
# print('None')
#
# cur2 = n1
# while cur2 is not None:
#     print(cur2.item, '->', end=' ')
#     cur2 = cur2.next
# print('None')


# is empty(),__str__, travel(start=true),add_to_front,add_to_back,add_before_node,remove_first,remove_last,remove_key
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def is_empty(self):
#         return  not self.head
#
#     def __str__(self):
#         ls = ''
#         cur = self.head
#         while cur is not None:
#             ls += f'{cur.item} --> '
#             cur = cur.item
#         ls += 'None'
#         return  ls
#
#     def travel(self,start: bool = True):
#         if start:
#             cur = self.head
#             while cur is not None:
#                 print(f'{cur.item} --> ',end='')
#                 cur = cur.next
#         else:
#             cur = self.tail
#             while cur is not None:
#                 print(f'{cur.item} --> ',end='')
#                 cur = cur.previous
#
#     def add_to_front(self,item):
#         node = Node(item)
#         if self.is_empty():
#             self.head = self.tail = node
#         else:
#             node.next = self.head
#             self.head.previous = node
#             self.head = node
#
#     def add_to_back(self,item):
#         node = Node(item)
#         if self.is_empty():
#             self.head = self.tail = node
#         else:
#             self.tail.next = node
#             node.previous = self.tail
#             self.tail = node
#
#     def insert(self,target,item):
#         node = Node(item)
#         cur = self.head
#         prev_node = Node
#
#         while cur.item != target:
#             prev_node = cur
#             cur =  cur.next
#
#         node.next = prev_node.next
#         prev_node.next.previous = node
#
#         prev_node.next = node
#         node.previous = prev_node
#
#     def remove_first(self):
#         if self.is_empty():
#             print('List empty')
#             return
#         if self.head.next is None:
#             self.head = self.tail = None
#         else:
#             self.head = self.head.next
#             self.head.previous = None
#
#     def remove_last(self):
#         if self.is_empty():
#             print('List empty')
#             return
#         if self.head.next is None:
#             self.head = self.tail = None
#         else:
#             prev = self.tail.previous
#             prev.next = None
#             self.tail = prev
#
#     def remove_key(self,key):
#         if self.is_empty():
#             print('List empty')
#             return
#
#         cur = self.head
#         while cur is not None and cur.item != key:
#             cur = cur.next
#
#         if cur is None:
#             print(f'{key} dose not exist in the list')
#             return
#
#         prev = cur.previous
#
#         if cur.next is None:
#             self.tail = prev
#
#         if prev is None:
#             self.head = cur.next
#             if self.head is not None:
#                 self.head.previous = None
#
#         prev.next = cur.next
#         cur.previous = None
#         prev.next.previous = prev

# dll  = DoublyLinkedList()
# dll.add_to_front(5)
# dll.add_to_front(10)
# dll.add_to_front(15)
# dll.add_to_back(20)
# dll.insert(10,6)
#
#
# # dll.remove_first()
# # dll.remove_last()
# dll.remove_key(10)
# dll.travel()


#push, pop, get_top,is_empty, size
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.size = 0
#
#     def push(self,x):
#         node = Node(x)
#         if node is None:
#             print('Heap Overflow')
#             return
#
#         node.next = self.top
#         self.top = node
#         self.size += 1
#
#     def pop(self):
#         if self.top is None:
#             print('Stacl Overflow')
#             return
#         top = self.top.item
#         self.top = self.top.next
#         self.size -= 1
#
#     def is_empty(self):
#         return self.top is None
#
#     def get_top(self):
#         if not self.is_empty():
#             return self.top.item
#         else:
#             print('Stack empty')
#
#     def size(self):
#         return self.size
#
# stack = Stack()
# stack.push(5)
# stack.push(10)
# stack.push(15)
# print(f'Top: {stack.get_top()}')
# stack.pop()
# stack.pop()
# print(f'Top: {stack.get_top()}')
# stack.pop()
# print(f'Stack empty: {stack.is_empty()}')

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
# # enqueue, dequeue, first, size, is_empty, travel
#
# class Q:
#     def __init__(self):
#         self.h = None
#         self.t = None
#
#     def first(self):
#         return self.h.data if self.h else None
#
#     def size(self):
#         temp = self.h
#         count = 0
#         while temp is not None:
#             count += 1
#             temp = temp.next
#         return count
#
#     def is_empty(self):
#        return self.h is None
#
#
#     def travel(self):
#         print('Elements: ')
#         temp = self.h
#         while temp is not None:
#             print(temp.data, end="--> ")
#             temp= temp.next
#         print('None')
#
#     def enqueue(self,data):
#         if self.t is None:
#             self.h = Node(data)
#             self.t = self.h
#         else:
#             self.t.next = Node(data)
#             self.t.next.prev = self.t
#             self.t = self.t.next
#     def dequeue(self):
#         if self.h is None:
#             return None
#         else:
#             temp = self.h.data
#             self.h = self.h.next
#             self.h.prev = None
#             return temp
#
# q = Q()
# q.enqueue(5)
# q.enqueue(10)
# q.enqueue(15)
#
# q.travel()
# q.dequeue()
# q.travel()

class Node:
    def __init__(self,item):
        self.item = item
        self.rigth = None
        self.left = None

# get_root, is_empty, find_min, print, clear
# add <- __add, find <- __find, delete <- __delete
# insert.. remove
class Tree:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return  self._root

    def is_empty(self):
        return self._root is None

    def clear(self):
        self._root = None

    def add(self,item):
        if self._root is None:
            self._root = Node(item)
        else:
            self.__add(item,self._root)

    def __add(self, item, node):
        if item < node.item:
            if node.left is not None:
                self.__add(item,node.left)
            else:
                node.left = Node(item)
        else:
            if node.rigth is not None:
                self.__add(item, node.rigth)
            else:
                node.rigth = Node(item)

    def find(self,item):
        if self._root == None:
            return  self._root
        elif self._root is not None:
            return self.__find(item,self._root)
        else:
            return None

    def __find(self,item,node):
        if item == node.item:
            return node.item
        elif item < node.item and node.left is not None:
            return  self.__find(item,node.left)
        elif item > node.item and node.rigth is not None:
            return self.__find(item, node.rigth)

    def print(self):
        if self._root is not None:
            self.__print(self._root)

    def __print(self,node):
        if node is not None:
            self.__print(node.left)
            print(str(node.item) + '\n', end=' ')
            self.__print(node.rigth)


t = Tree()
t.add(5)
t.add(7)
t.add(9)
t.add(10)

COUNT = [10]

def print2DUtil(root, space):
    # Base case
    if (root == None):
        return
    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.item)

    # Process left child
    print2DUtil(root.left, space)


# Wrapper over print2DUtil()
def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


print2D(t.root)






