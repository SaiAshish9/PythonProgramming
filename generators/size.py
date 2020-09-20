# generator functions are a
# special kind of function that
# return a lazy iterator. These are objects
# that you can loop over like a list. However, unlike
# lists, lazy iterators do not store their conten
# Python generators are a simple way of creating iterators.

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]

for char in rev_str("hello"):
    print(char)

def fibonacci():
    current,previous=0,1
    while True:
        current,previous=current+previous,current
        yield current

fib=fibonacci()

# for i in range(6):
#     print(next(fib))

def oddnumbers():
    n=1
    while True:
        yield n
        n+=2

def pi_series():
    odds=oddnumbers()
    approx=0
    while True:
        approx+=(4/next(odds))
        yield approx
        approx-=(4/next(odds))
        yield approx

approx=pi_series()

for x in range(100000):
    print(next(approx))

