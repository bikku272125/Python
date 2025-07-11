# Part 1: OOPs Concepts in Python (With Explanation & Examples)
# 1.Class and objects 
class car:
    def __init__(self, model, color, type='Sedan'):
        self.model = model
        self.color = color
        self.type = type


    def display(self):
        print(f"Car Model: {self.model}, Color: {self.color}, type: {self.type}")
# Creating an object of the class
my_car = car("Toyota", "Red")
# Accessing attributes and methods
my_car.display()

# 2. Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print(f"Brand: {self.brand}")   
# Inheriting from Vehicle class         
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
# Creating an object of the Car class
my_car = Car("Toyota", "Corolla")
# Accessing methods from both classes
my_car.display_brand()
my_car.display()

# 3. Polymorphism
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Woof"
class Cat(Animal):
    def sound(self):
        return "Meow"                   

# Function to demonstrate polymorphism
def make_sound(animal):
    print(animal.sound())
# Creating objects of Dog and Cat
dog = Dog()
cat = Cat()
# Calling the function with different objects                   
make_sound(dog)  # Output: Woof
make_sound(cat)  # Output: Meow
# 4. Encapsulation
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance