# # print(3+5)
# # # name= input('Please enter your name')
# # # print("Name\n"+name)
# # print("""
# # hi
# # sai
# # hope
# # you
# # are
# # fine
# # """)
# # for i in range(1,5//2):
# #     print(i)
# # parrot="Norwegian Blue"
# # print(parrot)
# # print(parrot[0])
# # print(parrot[3])
# # print(parrot[-1])
# # print(parrot[0:6])
# # print(parrot[:6])
# # print(parrot[6:])
# # print(parrot[-4:-2])
# # print(parrot[0:6:2])
# # print(parrot[0::2])
# # print("{0} {1}".format(1,2))
# # print("a"+str(2)+"b")
# # # print("a"+2+"b") error
# # age = 24
# # print("%d" % age)
# # print("%d %s,%d %s"%(age, "years" ,6,"months"))
# # print("%12f" % (22/7))
# # print("%12.50f"%(22/7))
# #
# # for i in range(1,12):
# #     print("{0:2} {1:<4} {2:<4}".format(i,i**2,i**3))
# # # %2d %4d %4d  0->i 2->presion
# #
# # print("{0:12.50}".format(22/7))
# # print("{} {} {}".format(1,2,3))
# # print("{0} {2} {1}".format(1,2,3))
# #
# # def boo():
# #     print('hi');
# #
# # boo();
# #
# # # a=input("name: ");
# # # b=input("what's your age %s"%(a))
# # # print(b)
# #
# # # 15<b<65 or
# #
# #
# # print(
# #     """
# #        False :{0}
# #        None:{1}
# #        0:{2}
# #        0.0:{3}
# #        [] :{4}
# #        ():{5}
# #        '':{6}
# #        "":{7}
# #        {{}}:{8}
# #     """.format(False,bool(None),bool(0),bool(0.0),bool([]),
# #                bool(()),bool(''),bool(""),bool({})
# #                ))
# # #     not in and or if elif else
# #
# # c="6"
# # d="abcd"
# #
# # if c in d:
# #     print(True)
# # elif c not  in d:
# #     print(True)
# # else:
# #     print(False)
# #
# # s="sdfghjkl"
# # for i in range(90,len(s)):
# #        print(s[i],end='')
# #        if s[i] == 'g':
# #               break;
# # else:
# #     print("err")
# #
# # list_1=[1,2,4]
# # list_2=list()
# # if list_1 == list_2:
# #     print(True)
# # print(sorted(list_1,reverse=True))
# #
# # # list_1.append(5)
# #
# # c=[1,2]+[3,4]
# #
# # # returns None
# # c.sort(reverse=True)
#
# # print(c)
# # print("abc".count("a"))
# #
# # # iterables
# #
# # string="123456"
# #
# # for char in string:
# #     print(char)
#
# # my_iterator =iter(string)
# # print(my_iterator)
# # print(next(my_iterator))
# # print(next(my_iterator))
#
# #  in python3 Range is a built in type
# #  in python2 it's implemented as a function
#
# print(list(range(10)))
#
# odd=range(1,10000,2)
# print(odd[986])
#
# # c='cghgffh'
# # print(c.index('c'))
#
#

# decimals = range(0,100)
# my_range=decimals[3:40:3]
# print(my_range==range(3,40,3))
# print(range(0,5,2)==range(0,6,2))

# for i in range(99,0,-2):
#     print(i)

# print(range(0,100)[::-2]==range(99,0,-2))

# t="a","b","c"
# t=t[0],"d",t[1]
# print(t)
# print('a','b','c')
# print(('a','b''c'))

# tuple is immutable object whereas list is mutable
# a=b=c=d=12
# print(a)
# b=13
# a,b=b,a
# print("a is {}".format(a))
# print("b is {}".format(b))
# a,b,c=t
# print(a,b,c)

a='a','b','c',(
    'd','e'
)

print(a)


