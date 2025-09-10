class Animal:

    def __init__(self, color="white"):
        self.color = color

    def sound(self):
        return "УУУУУУ"


class Dog(Animal):

    def __init__(self, color, big_size):
        super().__init__(color)
        self.big_size = big_size

    def sound(self):
        return "гав-гав"


class Cat(Animal):

    def __init__(self, color, small_size):
        super().__init__(color)
        self.small_size = small_size

    def sound(self):
        return "мяу-мяу"

animal = Animal()
dog = Dog("brown", True)
cat = Cat("grey", False)

print(animal.sound())
print(cat.sound())
print(dog.sound())