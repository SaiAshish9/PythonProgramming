import sys

print(sys.argv)

if len(sys.argv) ==1:
    print("password")
else:
    password=sys.argv[1]
    print(password)