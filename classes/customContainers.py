class TagCloud:
    def __init__(self):
        self.tags={}

    def add(self,tag):
        self.tags[tag]= self.tags.get(tag,0)+1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(),0)

    def __setitem__(self, key, value):
        self.tags[key.lower()]=value

    def __iter__(self):
        return iter(self.tags)

    def __len__(self):
        return list(self.tags.values())[0]


cloud=TagCloud()
# cloud.add("python")
[cloud.add("python") for x in range(3)]
print(cloud.tags)
print(len(cloud))
