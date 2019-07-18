"""
2.    Реализовать класс итератора, который будет возвращать переданную ему коллекцию в обратном порядке.
"""

class Reverse(object):
    def __init__(self, collection=None):
        if collection is None:
            raise StopIteration
        else:
            self.args = collection[::-1]
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.args):
            raise StopIteration
        value = self.args[self.idx]
        self.idx += 1
        return value

if __name__ == "__main__":
    l = [i for i in range(1, 16)]
    print(l)
    t = ("a", "b", "c", "d")
    for i in Reverse(l):
        print(i)
    print(t)
    for i in Reverse(t):
        print(i)
    for i in Reverse(("spam", "eggs", "foo", "bar")):
        print(i)