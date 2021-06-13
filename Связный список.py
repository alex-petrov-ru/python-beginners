# a = [1]
# a.append([2])
# a[1].append([3, None])
# p = a
# while p is not None:
#     print(p[0])
#     p = p[1]
#
# a = [x, a]


class LinkedList:
    def __init__(self):
        self._begin = None

    def insert(self, x):
        self._begin = [x, self._begin]

    def pop(self):
        assert self._begin is not None, "list is empty"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x


a = LinkedList()
a.insert(5)
a.insert(10)
print(a.pop())
print(a.pop())