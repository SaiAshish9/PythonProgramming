print(3+5)
# name= input('Please enter your name')
# print("Name\n"+name)
print("""
hi 
sai
hope 
you 
are
fine
""")
for i in range(1,5//2):
    print(i)
parrot="Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])
print(parrot[-1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-2])
print(parrot[0:6:2])
print(parrot[0::2])
print("{0} {1}".format(1,2))
print("a"+str(2)+"b")
# print("a"+2+"b") error
age = 24
print("%d" % age)
print("%d %s,%d %s"%(age, "years" ,6,"months"))
print("%12f" % (22/7))
print("%12.50f"%(22/7))

for i in range(1,12):
    print("{0:2} {1:<4} {2:<4}".format(i,i**2,i**3))
# %2d %4d %4d  0->i 2->presion

print("{0:12.50}".format(22/7))
print("{} {} {}".format(1,2,3))
print("{0} {2} {1}".format(1,2,3))