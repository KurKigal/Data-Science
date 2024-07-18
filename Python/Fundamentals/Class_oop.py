#Classes in Python are blueprints for creating objects. They define properties (attributes) and behaviors (methods) that objects of that class should have.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"{self.make} {self.model}")

# Creating instances of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Ford", "Mustang")

car1.display_info()  # Output: Toyota Corolla
car2.display_info()  # Output: Ford Mustang


#ABSTRACTION

'''
Abstraction is the concept of hiding the complex implementation details and exposing only the essential features of an object. 
In Python, this is often achieved through abstract base classes (ABCs) and interfaces.
'''


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Cannot instantiate abstract class Shape
# shape = Shape()  

# Creating an instance of Rectangle
rectangle = Rectangle(5, 3)
print(rectangle.area())  # Output: 15


#ENCAPSULATION

'''
Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit (class). 
It restricts direct access to some of an object's components, protecting its internal state.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.__age}")

person1 = Person("Alice", 30)
person1.display_info()  # Output: Name: Alice, Age: 30

# Attempting to access private attribute directly will raise an error
# print(person1.__age)  # AttributeError: 'Person' object has no attribute '__age'


#INHERITANCE

'''
Inheritance allows one class (subclass) to inherit the attributes and methods from another class (superclass).
It promotes code reusability and allows extending the functionality of existing classes.
'''


class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Woof
print(cat.sound())  # Output: Meow



#POLYMORPHISM

'''
Polymorphism means the ability to present the same interface for different data types (classes).
It allows methods to be written that can work with objects of various types and classes, enabling flexibility and dynamic behavior.
'''


class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

def make_sound(animal):
    print(animal.sound())

# Different objects passed to the same function
dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Woof
make_sound(cat)  # Output: Meow