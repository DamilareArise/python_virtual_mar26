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
        
        
calc1 = Calculator()
calc1.home()