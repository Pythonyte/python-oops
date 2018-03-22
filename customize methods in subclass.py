class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self): # Added method
        return '[Person: %s, %s]' % (self.name, self.pay) # String to print

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        self.pay = int(self.pay * (1 + percent + bonus)) # Bad: cut and paste

class ManagerX(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus) # Good: augment original

"""
    instance. method( args...)
is automatically translated by Python into this equivalent form:
    class. method( instance, args...)
"""