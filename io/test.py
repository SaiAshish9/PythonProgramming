# x=open("abc.txt",'r')
#
# for line in x:
#     print(line)
#  x.close() so that it can't be corrupted
with open("abc.txt") as x:
    y=x.readline()
    # for a in x:
    #     print(a)
    while y:
        y=x.readline()
        print(y)

with open("abc.txt") as x:
    y=x.readlines()
print(y)


