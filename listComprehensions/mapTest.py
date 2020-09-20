# text="asdfghjk sfdgfhgjh"
# def spam(list:list):
#     return "a" not in list
# d = list(filter(spam,text.split(' ')))
# print(d)
# a=[x.upper() for x in text]
# b=list(map(str.upper,text.split(' ')))
# c=list(map(str.upper,text))
# print(a,b,c,sep='\n')
# def calc(x,y:int):
#     return x+y
# numbers=[1,2,3,4,5]
# import functools
# print(functools.reduce(calc,numbers))

a=[1,2,3,4,5]
b=[1,0]
# 0 {} [] "" None False () 0.0 {{}} ''
print(all(a),any(a),all(b),any(b))