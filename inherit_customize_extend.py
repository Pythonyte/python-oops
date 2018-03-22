"""Inherit, Customize, and Extend
In fact, classes can be even more flexible than our example implies. In general, classes
can inherit, customize, or extend existing code in superclasses. For example, although
we’re focused on customization here, we can also add unique methods to Manager that
are not present in Person, if Managers require something completely different (Python
namesake reference intended). The following snippet illustrates. Here, giveRaise re-
defines a superclass’s method to customize it, but someThingElse defines something
new to extend:
"""



"""
class Person:
    def lastName(self): ...
    def giveRaise(self): ...
    def __repr__(self): ...

class Manager(Person): # Inherit
    def giveRaise(self, ...): ... # Customize
    def someThingElse(self, ...): ... # Extend

tom = Manager()
tom.lastName() # Inherited verbatim
tom.giveRaise() # Customized version
tom.someThingElse() # Extension here
print(tom) # Inherited overload method

• Although we could have simply coded Manager from scratch as new, independent
code, we would have had to reimplement all the behaviors in Person that are the
same for Managers.

• Although we could have simply changed the existing Person class in place for the
requirements of Manager’ s giveRaise, doing so would probably break the places
where we still need the original Person behavior.

• Although we could have simply copied the Person class in its entirety, renamed the
copy to Manager, and changed its giveRaise, doing so would introduce code re-
dundancy that would double our work in the future—changes made to Person in
the future would not be picked up automatically, but would have to be manually
propagated to Manager’ s code. As usual, the cut-and-paste approach may seem
quick now, but it doubles your work in the future
"""