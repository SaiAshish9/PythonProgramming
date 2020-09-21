# comma seperated value
import csv

# with open("data.csv","w") as file:
#     writer=csv.writer(file)
#     writer.writerow(["a","b","c"])
#     writer.writerow([1,2,3])

with open("data.csv") as file:
    reader=csv.reader(file)
    print(list(reader))
