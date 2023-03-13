class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
zahar = Person("Zahar", 18)
ivan = Person("Ivan", 19)

l = [zahar, ivan]

print([name.name for name in l])