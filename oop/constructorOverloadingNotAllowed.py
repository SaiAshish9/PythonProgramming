# class A:
#     def __init__(self,a):
#         self.a=a
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

# The constructor overloading
# is not allowed in Python.

# In the above code, the object st
# called the second constructor
# whereas both have the same
# configuration. The first method
# is not accessible by the st object.
# Internally, the object of the
# class will always call the last
# constructor if the class has multiple
# constructors.

class Student:
    def __init__(self):
        print("The First Constructor")
    def __init__(self):
        print("The second contructor")

st = Student()



# a=A(1)
# b=A(1,2)
# print(a.__dict__,b.__dict__)