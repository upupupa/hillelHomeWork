"""
1.    Реализовать класс итератор типа range. (с 1, 2 и 3 аргументами)
4.    Реализовать итерируемую версию zip - izip чтоб он работал как itertools.izip.
5.    Реализовать функцию которая рекурсивно обходит дерево указанной папки и генерирует пути ко всем файлам в дереве. Использовать генераторы.
"""

class Range_iterator(object):
    def __init__(self, iterable, start=0, end=None, step=1):
        self.iterable = iterable
        self.idx = start
        if end is None:
            end = len(self.iterable)
        elif end > len(self.iterable):
            raise KeyError("End must be less or equal than length of iterable")
        self.end = end
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx == self.end:
            raise StopIteration
        value = self.iterable[self.idx]
        self.idx+=self.step
        return value


if __name__ == "__main__":
    l = [i for i in range(15)]
    t = ("a", "b", "c", "d", "e")
    print(l)
    for i in Range_iterator(l, start=3, end=15, step=2):
        print(i)
    print(t)
    for i in Range_iterator(t):
        print(i)
    