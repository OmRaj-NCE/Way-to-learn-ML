# 1. Student Profile System (OOP Basics)
# Problem:
# Design a system to represent a student.
# Required Classes:
# Student
# Expected Behavior:
# Store name, roll number, marks
# Method to display student details
# Create multiple student objects
# OOP Concepts:
# Class & object
# __init__
# Instance attributes
# Methods
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll 
        self.marks = marks
    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Roll No. : {self.roll}")
        print(f"Got Marks : {self.marks}")
s1 = Student("Raj",12,"A+")
s1.show_details()


# 2. Bank Account System (Encapsulation Intro)
# Problem:
# Create a bank account with controlled balance access.
# Required Classes:
# BankAccount
# Expected Behavior:
# Balance should be private
# Deposit and withdraw methods
# Prevent withdrawal beyond balance
# OOP Concepts:
# Encapsulation
# Private attributes
# Controlled access via methods
class BankAccount:
    def __init__(self, name, curr_balance):
        self.name = name
        self.__curr_balance = curr_balance
    def show_bal(self):
        print(f"The current balance: {self.__curr_balance}")
    def deposit(self, amount):
        self.__curr_balance += amount
        print(f"Successfully deposited {amount}.")
    def withdraw(self, amount):
        if amount > self.__curr_balance:
            print("Failed! Not enough balance")
        else:
            self.__curr_balance -= amount
            print(f"{amount} is successfully withdrawn.")
b1 = BankAccount("raj",20000)
print(b1.show_bal)
b1.show_bal()
b1.deposit(20000)
b1.show_bal()
b1.withdraw(40000)


# 3. Employee Salary Calculator
# Problem:
# Calculate employee salary with allowances.
# Required Classes:
# Employee
# Expected Behavior:
# Base salary stored
# Method to add bonus
# Method to calculate total salary
# OOP Concepts:
# Object behavior
# Instance data
# Method logic
class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.__salary = salary
        self.position = position
    def salary_store(self):
        self.__salary
    def add_bonus(self,amnt):
        if amnt > 0:
            self.__salary += amnt
    def total_sal(self):
        print(f"{self.__salary}")
e1 = Employee("raj",20000, "video")
e1.total_sal()
e1.add_bonus(40000)
e1.total_sal()


# 4. Shape Area Calculator (Inheritance Intro)
# Problem:
# Calculate area for different shapes.
# Required Classes:
# Shape (parent)
# Rectangle, Circle (child)
# Expected Behavior:
# Each shape calculates its own area
# Common interface for area calculation
# OOP Concepts:
# Inheritance
# Method overriding
# Polymorphism (same method name)
class Shape:
    def area(self):
        pass
    def info(self):
        print(f"The area is {self.area()}")
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        # Using π ≈ 3.14 for simplicity
        return 3.14 * self.radius ** 2
# Now we can create objects and call info()
r1 = Rectangle(10, 23)      # No extra 'area' argument needed
c1 = Circle(5)
r1.info()   # Output: The area is 230
c1.info()   # Output: The area is 78.5


# 5. User Login System (Encapsulation + Validation)
# Problem:
# Design a login system.
# Required Classes:
# User
# Expected Behavior:
# Username and password stored privately
# Method to validate login
# Prevent direct access to password
# OOP Concepts:
# Encapsulation
# Private attributes
# Data protection
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == self.__username and password == self.__password:
            print("Successfully Logged in")
        else:
            print("Invalid")
m1 = User("saras", "121323")
m1.login()


# 6. Vehicle System (Inheritance + super())
# Problem:
# Model different vehicles.
# Required Classes:
# Vehicle
# Car, Bike
# Expected Behavior:
# Parent stores brand and speed
# Child adds specific features
# Use super() properly
# OOP Concepts:
# Inheritance
# super()
# Code reuse
'''class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def info(self):
        print(f"Brand: {self.brand}")
        print((f"Max Speed: {self.speed} km/h"))
class Car(Vehicle):
    def __init__(self, brand, speed, nitro, height):
        super().__init__(brand, speed)
        self.nitro = nitro
        self.height = height
    def gears(self):
        print(f"It has {self.nitro}")
    def suspension(self):
        print(f"It has {self.height}cm of suspension")
class Bike(Vehicle):
    def __init__(self, brand, speed, shape):
        super().__init__(brand, speed)
        self.shape = shape
    def body_shape(self):
        print(f"It has premium body in {self.shape} shape")'''
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def info(self):
        print(f"Brand: {self.brand}")
        print(f"Max Speed: {self.speed} km/h")
class Car(Vehicle):
    def __init__(self, brand, speed, gears, suspension_height):
        super().__init__(brand, speed)
        self.gears = gears
        self.suspension_height = suspension_height
    def info(self):
        super().info()
        print(f"Gears: {self.gears}")
        print(f"Suspension Height: {self.suspension_height} cm")
class Bike(Vehicle):
    def __init__(self, brand, speed, frame_shape):
        super().__init__(brand, speed)
        self.frame_shape = frame_shape
    def info(self):
        super().info()
        print(f"Frame Shape: {self.frame_shape}")
car = Car("Toyota", 220, 6, 15)
bike = Bike("Yamaha", 180, "Aerodynamic")
car.info()
print("---")
bike.info()
