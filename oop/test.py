 # imperative programming allows computer
 # to follow sequence of instructions
# a=10;
# b=20;
# print((10).__add__(20))

class A(object):

    def __init__(self, make, price):
        self.make= make
        self.price= price
        self.on= False

a=A("1",2)
print(a.price)

print("{0.make} {0.price}".format(a))
