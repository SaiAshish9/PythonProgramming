fruit={
    0:"1"
}
# print(fruit[0])
# print(fruit.get(0))
# # fruit.has_key("0") python 2
#
# print(list(fruit.keys()))
# print(fruit.items())
# print(tuple(fruit.items()))
# print(dict(tuple(fruit.items())))

# print("".join(["1","2","3"]))
# print(", ".join(["1","2","3"]))


# a ={
#     0:"1",
#     1:"2"
# }
#
# b={
#      0:"a",
#      2:"b"
# }
#
# a.update(b)
# print(a)

# print(a.copy())
# print("abc".upper())

# a={0,1,2,1}
# for i in a:
#     print(i)

# b=set([0,1,2,1])
# b.add(5)
# for i in b:
#     print(i)

# print({1,2}.union({3,4,4}))
# print(len({1,2,3}))
# print({1,2}.intersection({1,4}))
# print({1,2} & ({1,4}))
# print("-",*40)
# print("-" * 40)
# print({1,2}.difference({1,4}))
# print({1,2} - {1,4})
# print(sorted({4,6,8}.symmetric_difference({4,7,9})))
# print({4,6,8} ^ {4,7,9})
# The built-in method, discard() in Python,
# removes the element from the set only
# if the element is present in the set.
# If the element is not present in the set,
# then no error or exception is raised and
# the original set is printed.

# a={1,2,3}
# a.discard(1)
# a.remove(2)
# a.discard(3)
# try:
#     a.remove(2)
# except KeyError:
#     print("key does not exist")

# Frozen set is just an immutable version
# of a Python set object. While elements
# of a set can be modified at any time,
# elements of the frozen set remain the same
# after creation.


# # issuperset
# if {1,2,3}.issubset(set(range(5))):
#     print(True)
# print(sorted(set("fdgfhghjkjl") - frozenset("aeiou")))