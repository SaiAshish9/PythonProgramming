# # cities=["a","b","c","d"]
#
# # abc.txt w
# # abc.txt r
#
# # with open("abc.txt",'w') as option:
# #     for x in cities:
# #         print(x,file=option)
#
# cities=[]
#
# with open("abc.txt","r") as option:
#     for x in option:
#         cities.append(x.strip("\n").strip("\n"))
#
# print("abccabcdab".strip("ab"))
#
# for x in cities:
#     print(x,end='')

x=1,2,3,(
    (2,3,4),
    (5,6,8)
)

# print(x)

# with open("abc.txt","w") as file:
#     print(x,file=file)

contents=[]

# with open("abc.txt","r") as file:
#     contents=file.readline()
#
# c=eval(contents)
# a,b,c,d=c
# print(a)

with open("abc.txt","a") as table:
    for i in range(10):
        for i in range(5):
            print(i,file=table)
        print("-",file=table)
