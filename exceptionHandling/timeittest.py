from  timeit import timeit

code ="""
def calculate(age):
   if age<=0:
      return 10/age
      
xfactor=calculate(-1)
if xfactor == None:
    pass
# does not do anything
"""
print(timeit(code,number=10000))