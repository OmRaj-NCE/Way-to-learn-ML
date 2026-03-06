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

# 7. Notification System (Polymorphism)
# Problem:
# Send notifications via different methods.
# Required Classes:
# Notification
# EmailNotification, SMSNotification
# Expected Behavior:
# Each class implements send() differently
# Loop through objects and call send()
# OOP Concepts:
# Polymorphism
# Method overriding
class Notification:
    def __init__(self):
        pass
    def receive_(self):
        print("You received a Message !.....")
    def send_(self):
        print("Message send successfully.")
class EmailNotification(Notification):
    def __init__(self):
        super().__init__()
    def receive_(self):
        print("A new Email notification received")
    def send_(self):
        print("Message send successfully via email.")
class SMSNotification(Notification):
    def __init__(self):
        super().__init__()
    def receive_(self):
        print("A new SMS message you got")
    def send_(self):
        print("Message send successfully via SMS.")
a = [EmailNotification(), SMSNotification()]
for i in a:
    i.send_()
    

# 8. Product Inventory Manager
# Problem:
# Manage product stock.
# Required Classes:
# Product
# Inventory
# Expected Behavior:
# Add products
# Reduce stock after sale
# Prevent negative stock
# OOP Concepts:
# Object interaction
# Encapsulation
# State management
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self._stock = stock          # "protected" attribute – not meant to be accessed directly
    def show_info(self):
        print(f"Product: {self.name}\nPrice: ₹{self.price}\nStock: {self._stock}")
    def reduce_stock(self, quantity):
        """Reduce stock safely – prevents negative stock."""
        if quantity > self._stock:
            print(f"Insufficient stock! Only {self._stock} available.")
            return False
        self._stock -= quantity
        print(f"Sold {quantity} {self.name}(s). Remaining stock: {self._stock}")
        return True
    # Optional: getter for stock if needed
    def get_stock(self):
        return self._stock
class Inventory:
    def __init__(self):
        self.products = []            # composition: Inventory has a list of Products
    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product.name} to inventory.")
    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        print(f"Product '{name}' not found.")
        return None
    def sell_product(self, name, quantity):
        product = self.find_product(name)
        if product:
            product.reduce_stock(quantity)
# --- Demonstration ---
# Create some products
iphone = Product("iPhone 15", 129999, 20)
samsung = Product("Galaxy S24", 89999, 15)
# Create inventory and add products
inventory = Inventory()
inventory.add_product(iphone)
inventory.add_product(samsung)
# Find product that not there
inventory.find_product("Nothing")
# Show product info
iphone.show_info()
print("---")
# Try selling
inventory.sell_product("iPhone 15", 5)      # normal sale
inventory.sell_product("iPhone 15", 20)     # insufficient stock
inventory.sell_product("Galaxy S24", 10)    # another sale
# Check updated stock
print("---")
iphone.show_info()


# 9. Library Management System
# Problem:
# Track books and borrowing.
# Required Classes:
# Book
# Library
# Expected Behavior:
# Add books
# Issue and return books
# Track availability
# OOP Concepts:
# Class collaboration
# Encapsulation
# Business logic in methods
class Book:
    def __init__(self, name, price, author, genre):
        self.name = name
        self.price = price
        self.author = author
        self.genre = genre
        self.is_available = True   # Track availability
    def show_info(self, show_genre=False):
        print(f"Name: {self.name}\nAuthor: {self.author}\nPrice: {self.price}")
        if show_genre:
            print(f"Genre: {self.genre}")
        print(f"Available: {'Yes' if self.is_available else 'No'}")
class Library:
    def __init__(self):
        self._books = []   # Protected list of Book objects
    def add_book(self, book):
        self._books.append(book)
        print(f"Book '{book.name}' added to library.")
    def find_book(self, name):
        """Return the Book object if found, else None."""
        for book in self._books:
            if book.name.lower() == name.lower():
                return book
        return None
    def issue(self, name, days):
        book = self.find_book(name)
        if not book:
            print(f"No book found with name '{name}'.")
            return
        if not book.is_available:
            print(f"Sorry, '{name}' is already issued.")
            return
        # Mark as unavailable
        book.is_available = False
        print(f"Book '{name}' issued for {days} days. Please return on time.")
    def return_book(self, name):
        book = self.find_book(name)
        if not book:
            print(f"No book found with name '{name}'.")
            return
        if book.is_available:
            print(f"Book '{name}' was not issued.")
            return
        book.is_available = True
        print(f"Book '{name}' returned successfully. Thank you!")
# --- Demonstration ---
b1 = Book("Safar", 1290, "OmRAJ", "life")
b2 = Book("Python 101", 999, "Guido", "Programming")
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
b1.show_info(True)          # Show details including genre and availability
print("-----")
lib.issue("Safar", 14)      # Issue for 14 days
lib.issue("Safar", 7)       # Try to issue again – should fail
lib.issue("Java", 10)        # Non‑existent book
print("-----")
b1.show_info(True)           # Now availability should be 'No'
lib.return_book("Safar")     # Return
lib.return_book("Safar")     # Try to return again – should say not issued


# # 10. Payment System (Polymorphic Design)
# # Problem:
# # Handle multiple payment modes.
# # Required Classes:
# # Payment
# # CashPayment, CardPayment
# # Expected Behavior:
# # Same method pay()
# # Different implementations
# # Payment handled generically
# # OOP Concepts:
# # Polymorphism
# # Method overriding
class Payment:
    def __init__(self):
        print("Welcome")
    def payment(self):
        print("Successfully payment done.")
class CashPayment(Payment):
    def payment(self):
        print("Payment Done via Cash")
        return super().payment()
class CardPayment(Payment):
    def payment(self):
        print("Payment Done via Card")
        return super().payment()
a = [CashPayment(), CardPayment()]
for i in a:
    i.payment()
    
    
# # 11. Attendance Tracking System
# # Problem:
# # Track student attendance.
# # Required Classes:
# # Student
# # AttendanceSystem
# # Expected Behavior:
# # Mark present/absent
# # Calculate attendance percentage
# # OOP Concepts:
# # Object collaboration
# # Encapsulation
# # Data tracking
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.__attendance = {}
    def mark_attend(self, date, status):
        # Store status as string, not list
        self.__attendance[date] = status
    def mark_attendance(self):
        total_days = len(self.__attendance)
        if total_days == 0:
            return 0
        present_days = list(self.__attendance.values()).count('Y')
        percentage = (present_days / total_days) * 100
        return round(percentage, 2)
    def show_attend(self):
        print(f"Attendance record of {self.name} (Roll {self.roll}):")
        for date, status in self.__attendance.items():
            print(f"{date} : {'Present' if status == 'Y' else 'Absent'}")
        # if status == 'Y':
        #     result = "Present"
        # else:
        #     result = "Absent"
        # print(f"{date} : {result}")
class AttendanceSystem:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def mark_attendance_for_student(self, student, date, status):
        student.mark_attend(date, status)
    def show_report(self, student):
        student.show_attend()
        print(f"Attendance Percentage: {student.mark_attendance()}%")
# Creating a student
s1 = Student("Raj", 101)
# Creating attendance system
system = AttendanceSystem()
system.add_student(s1)
# Marking attendance
system.mark_attendance_for_student(s1, "2026-02-15", "Y")
system.mark_attendance_for_student(s1, "2026-02-16", "A")
system.mark_attendance_for_student(s1, "2026-02-17", "Y")
# Generate report
system.show_report(s1)


# 12. Order Processing System
# Problem:
# Process customer orders.
# Required Classes:
# Order
# Customer
# Expected Behavior:
# Add items to order
# Calculate total price
# Display order summary
# OOP Concepts:
# Class interaction
# Encapsulation
# Real-world modeling
class Order:
    def __init__(self):
        self.menu = {"samosa": 50, "golgape": 40, "matrino": 480}
        self._order = {}
    def show_menu(self):
        print("==== MENU ====")
        for item, price in self.menu.items():
            print(f"{item} : ₹{price}")
        print("==============")
    def take_order(self, item, quantity):
        if item in self.menu:
            self._order[item] = quantity
        else:
            print("Item not available")
    def total_bill(self):
        total = 0
        for item, qty in self._order.items():
            price = self.menu[item]
            total += price * qty
        return total
    def show_order(self):
        print("Your Order:")
        for item, qty in self._order.items():
            print(f"{item} x {qty}")
class Customer:
    def __init__(self, name):
        self.name = name
        print("----WELCOME----")
    def show_final(self, order):
        print(f"\nOrder for {self.name}")
        order.show_order()
        print("Total Bill:", order.total_bill())
order1 = Order()
order1.show_menu()
order1.take_order("samosa", 2)
order1.take_order("golgape", 3)
customer1 = Customer("Rajesh")
customer1.show_final(order1)


# 13. Access Control System (Advanced Encapsulation)
# Problem:
# Restrict sensitive actions.
# Required Classes:
# AdminUser
# NormalUser
# Expected Behavior:
# Admin can delete data
# Normal user cannot
# Permissions enforced by class design
# OOP Concepts:
# Inheritance
# Method overriding
# Access control
class User:
    def __init__(self, name):
        self.name = name
        self._data = ["File1", "File2", "File3"]
    def view_data(self):
        print("Available Data:")
        for item in self._data:
            print(item)
    def delete_data(self):
        print("Permission denied. Only admin can delete data.")
class AdminUser(User):
    def delete_data(self, item):
        if item in self._data:
            self._data.remove(item)
            print("Admin deleted:", item)
        else:
            print("Item not found")
class NormalUser(User):
    def delete_data(self, item):
        print("Normal users cannot delete data")
# -------- Program --------
admin = AdminUser("Raj")
user = NormalUser("Amit")
print("\nAdmin View:")
admin.view_data()
print("\nAdmin deletes File2")
admin.delete_data("File2")
print("\nUser tries to delete File1")
user.delete_data("File1")
print("\nFinal Data (Admin view):")
admin.view_data()
