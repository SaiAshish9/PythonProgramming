 # imperative programming allows computer
 # to follow sequence of instructions
# a=10;
# b=20;
# print((10).__add__(20))

class A(object):

    a=123

    def __init__(self, make, price):
        self.make= make
        self.price= price
        self.on= False

    def switch_on(self):
        self.on=True


a=A("1",2)
# print(a.price)
#
# print("{0.make} {0.price} {0.on}".format(a))
# a.switch_on()
# print("{0.on}".format(a))

# class attributes
print(A.a)
A.a=2
print(A.__dict__)
print(a.__dict__)









