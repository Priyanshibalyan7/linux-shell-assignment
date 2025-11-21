'''class vehicle stores brand and model .
class car inherits vehicle and adds sitting capacity 
class elctric_car (car) and adds batterty_range
display all details of electric car'''
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand: {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, seating_capacity):
        super().__init__(brand, model)
        self.seating_capacity = seating_capacity

    def display_info(self):
        base_info = super().display_info()
        print("{base_info}, Seating Capacity: {self.seating_capacity}")


class ElectricCar(Car):
    def __init__(self, brand, model, seating_capacity, battery_range):
        super().__init__(brand, model, seating_capacity)
        self.battery_range = battery_range

    def display_info(self):
        base_info = super().display_info()
        print("{base_info}, Battery Range: {self.battery_range} km")

''' make a class bank account with attributes account number and balance .
create three methods : deposit,withdraw(check condition for insufficient balance),display 
make it for two objects'''

class bank_account:
    def __init__(self, account_number,name, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.name=name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. Name: {self.name}.  New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance for withdrawal.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

a=bank_account("9834652998", "rajesh" ,500)
a.deposit(200)
a.withdraw(100)
a.display()

