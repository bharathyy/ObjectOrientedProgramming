class animal(object):
    def __init__(self,type):
        self.type=type
    def display(self):
        print("type is ",self.type)


class cat(animal):
    def __init__(self,name,type):
        self.name=name
        animal.__init__(self,type)
    def display(self):
        print("type is ",self.type)
        print("Name is ",self.name)


a=cat("bumroo","cat")
b=cat("whitey","cat")

a.display()
b.display()

