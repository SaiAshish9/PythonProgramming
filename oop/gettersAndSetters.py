# from gettersAndProperties import A

# The property() method in Python
# provides an interface to instance attributes.
# It encapsulates instance attributes
# and provides a property, same as Java and C#.

class A(object):

    def __init__(self,a):
        self._a=a

    def _get_a(self):
        return self._a

    def _set_a(self,a):
        self._a=a

    def print(self):
        print(self._a)

    a=property(_get_a,_set_a)

    @property
    def b(self):
        return self._a

    @b.setter
    def b(self,a):
        self._a=a

    def __str__(self):
        return "hi"

a=A("123")
print(a.a)
# a.print()

print(a)
a.b=1
print(a.b)