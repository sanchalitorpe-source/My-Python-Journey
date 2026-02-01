class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

animals = [Cat(), Dog()]

for a in animals:
    a.speak()
