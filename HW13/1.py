"""
Реализовать классы дескрипторы StaticMethod и ClassMethod.
"""

class StaticMethod(object):
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        return self.method

class SimpleClass(object):
    @StaticMethod
    def simplemethod():
        print("hewooo")

class ClassMethod(object):
    def __init__(self, method):
        self.method = method
    
    def __get__(self, instance, owner):
        if owner is None:
            owner = type(instance)
        def wrapper(*a):
            return self.method(owner, *a)
        return wrapper

class A(object):
    def __init__(self, a):
        self.test = a

    @ClassMethod
    def simplemethod(cls, *a):
        print("classmethod with {}".format(a))

if __name__ == "__main__":
    o = SimpleClass()
    o.simplemethod()

    c = A("a")
    c.simplemethod(1,2,3)