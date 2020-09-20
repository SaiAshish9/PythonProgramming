class A:
    def __init__(self,title):
        self.title=title

    def get_title(self):
        return self.title

    name=property(get_title)

a=A("abc")

print(a.name)
