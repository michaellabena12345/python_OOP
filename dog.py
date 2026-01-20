class Dog:
    def __init__(self, name):
        self.name= name
    def bark(self):
        print(f"my dog name {self.name} say wooff!!")

bogart = Dog("bogart")
bogart.bark()
