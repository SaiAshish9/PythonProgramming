try:
    with open("app.py") as file,open("another.txt") as target:
        print("file opened")
    age=int(input("Age:"))
    if age <=0 :
        raise ValueError("cannot be less than 0")
    b=10/age
except (ValueError,ZeroDivisionError,FileNotFoundError) as ex:
    print("Error",type(ex))
# except ZeroDivisionError:
#     print("zero error")
else:
    print("No Exceptions")
finally:
    print("completed")
    # file.close()