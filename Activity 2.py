class Animal:
    def move(self):
        pass


class Dog(Animal):
    def move(self):
        return "Running on four legs 🐕"


class Bird(Animal):
    def move(self):
        return "Flying through the air 🐦"


class Fish(Animal):
    def move(self):
        return "Swimming in water 🐠"


class Snake(Animal):
    def move(self):
        return "Slithering on the ground 🐍"



# Demonstration of polymorphism
def demonstrate_movement(objects):
    for obj in objects:
        print(obj.move())


# Create instances
animals = [Dog(), Bird(), Fish(), Snake()]

print("Animal Movements:")
demonstrate_movement(animals)
