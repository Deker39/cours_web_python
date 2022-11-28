class Node:
    def __init__(self,i):
        self.i = i
        self.n = None
        self.p = None

# add ->(if this value are available from list, call mesegge about it, and don't addintion value ),
# remove all added value from list
# show list from the end or the start
# check value in list
# value  replace in list (user decide, which replace only first value or all )
class DoubleList:
    def __init__(self):
        self.h = None
        self.t = None

    def is_empty(self):
        return  not self.h

    def add(self,x):
        node = Node(x)
        if self.is_empty():
            self.h = self.t =  node
        else:
            cur = self.h
            while cur:
                if cur.i == node.i:
                    return print('this value are available from list')
                cur = cur.n

            node.n = self.h
            self.h.p = node
            self.h = node

    def remove(self,x):

        if self.is_empty():
            print('List empty')
            return

        cur = self.h
        while cur is not None and cur.i != x:
            cur = cur.n

        if cur is None:
            print(f'{x} dose not exist in the list')
            return

        prev = cur.p

        if cur.n is None:
            self.t = prev

        if prev is None:
            self.h = cur.n
            if self.h is not None:
                self.h = None

        prev.n = cur.n
        prev.n.p = prev

    def __str__(self):
        ls = ''
        cur = self.h
        while cur is not None:
            ls += f'{cur.i} --> '
            cur = cur.n
        ls += 'None'
        return  ls

    def travel(self, start: bool = True):
        ls = ''
        if start:
            cur = self.h
            while cur is not None:
                ls += f'{cur.i} --> '
                cur = cur.n
        else:
            cur = self.t
            while cur is not None:
                ls += f'{cur.i} --> '
                cur = cur.p
        print(f'{ls}None')

    def search(self,x):
        cur = self.h
        while cur:
            if cur.i == x:
                return print(f'find: {cur.i}')
            cur = cur.n
        return print('This variable not found')

    def replase(self,target,item):
        node = Node(item)
        cur = self.h
        prev_node = None

        while cur.i != target:
            prev_node = cur
            cur = cur.n

        node.n = prev_node.n
        prev_node.n.p = node

        prev_node.n = node
        node.p = prev_node



ddl = DoubleList()

ddl.add(5)
ddl.add(10)
ddl.add(6)
ddl.add(15)

ddl.remove(6)
ddl.search(5)
ddl.replase(10,7)

ddl.travel(False)

