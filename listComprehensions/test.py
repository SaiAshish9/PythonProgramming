# print(__file__)
#
# numbers=[1,2,3,4,5]
#
# squares=[number ** 2 for number in numbers]
# squares={number ** 2 for number in numbers}
# print(squares)
#
# squares1=[x**2 for x in numbers if x%2 != 0]
# print(squares1)
#
import timeit
a=[1,2,3]
b=[2,3,5]

c=[(x,y) for x in a for y in b]

print(c)

c=[[(x,y) for x in a] for y in b]

print(c)


