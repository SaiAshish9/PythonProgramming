import re

pattern=r"eggs"

if re.match(pattern, "hgdgfgdgfeggsbdfgf"):
    print("found")

if re.search(pattern, "hgdgfgdgfeggsbdfgf"):
    print("found")

print(re.findall(pattern,"eggseggsbnbmmj,n"))