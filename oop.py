

class Dog:
    # init method (special), allows us to instantiate object right when it is created
    def __init__(self, name, age):
        # attribute of the class dog, which is name
        self.title = name
        self.age = age
    # this is a method, basically a function that goes inside of a class
    def get_name(self):
        return self.title
    def get_age(self):
        return self.age

d = Dog("Jerry", 56)

print(d.get_name())
print(d.get_age())