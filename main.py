import sys


class Point:
    def __init__(self, x, y=-1):
        self.x = x
        self.y = y


import dis
def spam(a):
    x=42
    return(x>a)

if __name__ == "__main__":
    p = Point(0,0)
    print('dir(Point): {}'.format(dir(Point)))
    print('dir(p): {}'.format(dir(p)))

    print(sys.getrefcount(p))
    print(sys.getsizeof(p))

    print(type(spam))
    print(spam.__code__.co_code)
    print(spam.__code__.co_argcount)
    print(spam.__code__.co_varnames)
    print(spam.__code__.co_consts)
    print(dis.dis(spam))
    pass