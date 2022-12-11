
class IIterator:

    @staticmethod
    def has_next():
        """return obj if obj exists"""


    @staticmethod
    def next():
        """return obj"""

class Iterable(IIterator):

    def __init__(self, aggregates):
        self.index = 0
        self.aggregates = aggregates


    def next(self):
        if self.index < len(self.aggregates):
            aggregates = self.aggregates[self.index]
            self.index += 1
            return aggregates
        raise Exception('Cannot use not position indexnumber')

    def has_next(self):
        return self.index < len(self.aggregates)

class Person1:

    def __init__(self,v):
        self.v = v

class Person2:

    def __init__(self, v):
        self.v = v

persons = [Person1(1),Person1(2),Person1(3),Person1(4)]
# for i in persons:
#     print(i.v)

iterable = Iterable(persons)
iterable.next()
iterable.next()
print(iterable.next().v)