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


class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        self.previous = None

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
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,x):
        node = Node(x)
        if node is None:
            print('Heap Overflow')
            return

        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            print('Stacl Overflow')
            return
        top = self.top.item
        self.top = self.top.next
        self.size -= 1

    def is_empty(self):
        return self.top is None

    def get_top(self):
        if not self.is_empty():
            return self.top.item
        else:
            print('Stack empty')

    def size(self):
        return self.size

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print(f'Top: {stack.get_top()}')
stack.pop()
stack.pop()
print(f'Top: {stack.get_top()}')
stack.pop()
print(f'Stack empty: {stack.is_empty()}')



