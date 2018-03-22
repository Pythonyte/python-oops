class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.name.split()[-1]) # Extract object's last name
    sue.pay *= 1.10 # Give this object a raise
    print('%.2f' % sue.pay)
    import pdb;pdb.set_trace()


"""
We’ve added the last three lines here; when they’re run, we extract bob’s last name by
using basic string and list operations on his name field, and give sue a pay raise by
modifying her pay attribute in place with basic number operations. In a sense, sue is
also a mutable object—her state changes in place just like a list after an append call
"""


"""
What we really want to do here is employ a software design concept known as encap-
sulation— wrapping up operation logic behind interfaces, such that each operation is
coded only once in our program. That way, if our needs change in the future, there is
just one copy to update. Moreover, we’re free to change the single copy’s internals
almost arbitrarily, without breaking the code that uses it.
 
"""