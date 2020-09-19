import shelve

# A “shelf” is a persistent,
# dictionary-like object.
# The difference with “dbm” databases is
# that the values (not the keys!)
# in a shelf can be essentially
# arbitrary Python objects — anything
# that the pickle module can handle.
# This includes most class instances,
# recursive data types, and objects
# containing lots of shared sub-objects.
# The keys are ordinary strings
#
# with shelve.open("shelf") as fruit:
#     fruit["orange"]="orange"
#     fruit["apple"]="apple"
#     fruit["lemon"]="lemon"
#     fruit["grape"]="grape"
#
#     print(fruit["lemon"])
# fruit=shelve.open("shelf")
# print(fruit)
#
# pickle is for serializing some object
# (or objects) as a single bytestream
# in a file.
#
# shelve builds on top of pickle
# and implements a serialization
# dictionary where objects are pickled,
# but associated with a key (some string),
# so you can load your shelved data file
# and access your pickled objects via keys.
# This could be more convenient were you
# to be serializing many objects.

import pickle

integers = [1, 2, 3, 4, 5]

with open('pickle-example.p', 'wb') as pfile:
    pickle.dump(integers, pfile)



with open('pickle-example.p', 'rb') as pfile:
    integers = pickle.load(pfile)
    print(integers)

with shelve.open('shelf-example', 'c') as shelf:
    shelf['ints'] = integers

with shelve.open('shelf-example', 'r') as shelf:
    for key in shelf.keys():
        print(repr(key), (shelf[key]),shelf[key])

# The repr() function returns a printable
# representational string of the given object.




