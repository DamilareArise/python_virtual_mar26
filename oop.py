# OOP -> Object Oriented Progamming


# object -> Anything that has property and can perform a function 

# An object is created from a class / an object is an instance of a class


class CarModel:
    brand = 'Toyota'
    model = 'Corolla 2025'
    color = 'wine'
    
    def drive(self):
        print(f"{self.brand} {self.model} {self.color} color is driving...")
        
    def stop(self):
        print(f"{self.model} stopped")
    
    

car1 = CarModel()
car2 = CarModel()
# print(car1 == car2)

car2.model = "Camry 2025"
# print(car2.model)
# print(car1.model)

# car1.drive()
# car2.stop()


class Calculator:
    name = "Cascio"
    
    def home(self):
        print("""
            1. Addition
            2. Subtraction
            #. Exit 
        """)
        choice = input("Choice: ")
        if choice == '1':
            self.add()
        elif choice == '2':
            self.subtract()
        elif choice == "#":
            print("Bye!")
            exit()
        else:
            print("Invalid...")
            self.home()
            
    def add(self):
        val1 = float(input("value 1: "))
        val2 = float(input("value 2: "))
        result = val1 + val2
        print(result)
        self.home()
        
        
    def subtract(self):
        val1 = float(input("value 1: "))
        val2 = float(input("value 2: "))
        result = val1 - val2
        print(result)
        self.home()
        
        
# calc1 = Calculator()
# calc1.home()




# name = "stephen"
# name2 = set()
# print(type(name))

    

class Human:
    complexion = "Dark"
    name = None
    gender = "Male"
    
    def __init__(self, username):
        # print("welcome")
        self.name = username
        
    
    def walk(self):
        print(f"{self.name} is Walking...")
        
    def respiration(self):
        print("Let me breathe")
    
    
olisa =  Human('Olisa')
tolulope = Human('Tolulope')
# print(olisa == tolulope)

# tolulope.gender = "Female"
# tolulope.name = "Tolulope"
# print(tolulope.gender)

# olisa.walk()

# tolulope.walk()




class BankAccount:
    __account_name = None
    __balance = 0.0
    
    def __init__(self, name):
        self.__account_name = name
    
    def menu(self):
        print(f"""
        Welcome back {self.__account_name}
        
            1. Deposit
            2. Withdrawal
            3. Check balance
            #. Exit
        """)
        option = input("Option: ")
        if option == "1":
            self.__deposit()
        elif option == "2":
            self.__withdraw()
        elif option == '3':
            self.__check_balance()
        elif option == "#":
            print("Goodbye!")
            exit()
        else:
            print("Invalid option")
            self.menu()
            
    def __deposit(self):
        amount = float(input("Amount: "))
        if amount < 1:
            print("amount can't be less that 1.")
            self.menu()
        
        self.__balance += amount
        print("Deposit successfull")
        self.menu()
    
    def __withdraw(self):
        amount = float(input("Amount: "))
        if amount < 1:
            print("amount can't be less that 1.")
            self.menu()
        
        if amount > self.__balance:
            print("Insufficient fund")
            self.menu()
        
        
        self.__balance -= amount
        print("Withdrawal successfull")
        self.menu()
    
    def __check_balance(self):
        print(f"Balance: ${self.__balance}")
        self.menu()
    
    

ade_account = BankAccount('Ade')

# print(ade_account.__balance)
# ade_account.__balance = 100000
# ade_account.menu()
# ade_account.__withdraw()

# pillars of OOP
# 1. encapsulation :- public, private, protected, static
# 2. inheritance





