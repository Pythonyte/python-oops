class AddObjects:
    class_attr = 'i am class attr'
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

o1 = AddObjects(5)
o2 = AddObjects(6)
o2.price = 100
print(o1+o2)
print(o1.__dict__)
print(o1.class_attr) # searched by search tre lookup, but o1 namespace dict doesnot have this
print(o2.__dict__)
print(AddObjects.__dict__)


"""
Class namespace have class attributes and instance namespaces have instance attributes seperately. 

11
{'num': 5}
{'price': 100, 'num': 6}
{'__module__': '__main__', '__add__': <function __add__ at 0x7fdb9beec7d0>, '__init__': <function __init__ at 0x7fdb9beec758>, '__doc__': None}
"""