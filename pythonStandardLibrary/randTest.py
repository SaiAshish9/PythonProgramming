import random
import string

print(random.random())
print(random.randint(1,10))
print(random.choice([1,2,3]))
print(random.choices([1,2,3],k=2))
print("".join(random.choices("asdfghj",k=4)))
print("".join(random.choices(string.ascii_letters,k=4)))

a=[1,2,3,4]
random.shuffle(a)
print(a)