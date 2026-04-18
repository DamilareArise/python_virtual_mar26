# print(2 + 2)
# commenting - 1. Debugging 2. Documentation
'''
how are you?
I hope you are good?

'''


# 1. Indentation

# print("My name is Damilare")

# def sayhello():
#     print("hello")
    
# sayhello()

# 2. Variables 
# bottle = "Water"
name = "Samson"
# name = "Tomiwa"

# print(name)

# The variable name
# The assignment operator (=)
# the value 

# rules guiding variable declaration
# 1. It can only start alphabets or underscore
# _firstname = "Samson"
# 2. It doesnt allow spaces, hence
    # i. Camel casing : firstNameOfTheStudent
    # ii. Snake casing: first_name_of_the_student
    # iii Pascal casing: FirstNameOfTheStudent

# 3. avoid using python dedicated syntax as a variable name 
# 4. Variable name should be descriptive enough

#    Types of variable declaration
# 1. single variable, single values 
bottle = "water"
# 2. single variable, multiple value
# bottle = "water", "soap", "oil"
# print(bottle)
# 3. multiple variable, single value 
# x = y = z = 5
# y = 20
# print(y)
# 4. Multiple variable, multiple value
# x, y, z = 10, 20, 30
# print(x)


# concatenation 
# print("Samson " + "Meshach")
name = "Samson"
age = 30

# print("My name is "+name)
# print("I am "+str(age)+" years old")

# print("My name is", name)
# print("I am",age,"years old")

# f-string
# print(f"My name is {name}. I am {age}years old")

# name, course, occupation, age, 


# Python Datatypes

# 1. Text type: str 
name = "Samson"
# print(type(name))
# 2. Number Types: int, float, complex
# num = 45
# num = 45.5
# num = 4 + 2j
# print(type(num))

# 3. Sequence type: list [], tuple (), range

# names = ['Ayo', 'Lola', 'Femi']
names = ('Ayo', 'Lola', 'Femi')
# print(type(names))

# nums = list(range(20))
# nums = list(range(2, 20, 1))
# print(nums)

# 4. Boolean Type: bool 
isActive = False

# 5. Set type: set
# names =  {'Ayo', 'Lola', 'Femi'}
# nums = {1, 4, 6, 5, 3, 2}
# print(nums)

# 6. Mapping Types: Dict
student = {
    "name": "Ayo Ade",
    "course": "Data science",
    "age": 30
}
# print(type(student))
# print(student["age"])

# 7. NoneType: None
name = None
# print(name)


# num = 5
# print(float(num))


# Python Operator
# 1. Arithmetic operator: +, -, /, *, **, //, %

# print(5//2)
# print(5**2)
# print(5 % 2)

# 2. Assignment operator: =, +=, -=, /=, *= etc.
# num = 5
# num += 1
# num -= 1
# print(num)

# 3. comparison operator: ==, !=, > , < , >=, <=
# num = 4
# print(num != 5)



# Conditional statement 
# if num == 5:
#     print('Valid')

# else:
#     print("Invalid")


# print(len("Dare"))
# password = input("Password: ")

# if len(password) >= 8:
#     print("Password is valid")
# else:
#     print('The length of password must be >= 8')


# USSD app
# ussd = input("USSD: ")
# if ussd == "*312#":
#     print("""
#         1. Buy Data
#         2. Check balance
#     """)
#     choice = input("Choice: ")
#     if choice == '1':
#         print("Buy Data")
        
#     elif choice == '2':
#         print('check blance')
#     else:
#         print('Invalid input')
        
# elif ussd == '*310#':
#     print("Your balance is #100.00")

# elif ussd == '*121#':
#     print("""
#         1. Data for me
#         2. get plan  
#     """)

# else:
#     print("Invalid ussd code")
    
    
# Build a grading system 
# 70 - 100 (A)
# 60 - 69 (B)
# 50 - 59 (C)
# 45 - 49 (D)
# 40 - 44 (E)
# 0 - 39 (F)  


# 4. logical operator: AND, OR, NOT
"""
A       B       AND     OR      NOT A
0       0       0       0       1
0       1       0       1       1
1       0       0       1       0
1       1       1       1       0
"""

rice = True
beans = False

# print(rice and beans)
# print(rice or beans)
# print(not rice)

# if not rice:
#     print("There is no rice")
# else:
#     print('Rice is available')


# score = float(input("Score: "))
# if score >= 70 and score <= 100:
#     print('A')
# elif score >= 60 and score <= 69:
#     print('B')
# elif score >= 50 and score <= 59:
#     print('C')
# elif score >= 45 and score <= 49:
#     print('D')
# elif score >= 40 and score <= 44:
#     print('E')
# elif score >= 0 and score <= 39:
#     print('F')
# else:
#     print('Invalid score')

# 5. identity operator: is, is not
# val = 4
# val2 = 5
# print(val is not val2)

# 6. membership operator: in, not in
fruits = ['apple', 'orange', 'mango']
# print('cherry' in fruits)
# print('cherry' not in fruits)

# 7. bitwise operator
    # & -> and
    # | -> or
    # ~ -> not
    # ^ -> XOR
    
# print(bin(10))   # 1   0   1   0

# print(bin(5))    #     1   0   1

# print(bin(2))    #         1   0

# print(10 & 5) # 0

# print(10 | 5) # 1    1    1   1

# print(10 | 2)   # 1    0    1   0

# print(10 ^ 2)   # 1    0    0   0


# Assignment 
# build simple calculator

# Python Strings 
var = "Mango, is a kind of Fruit."  # ['M', 'a', 'n', 'g', 'o']
# print(var[0])
# print(var[-1])
# print(len(var))
# print(var)
# print(var.lower())  
# print(var.capitalize())
# print(var.upper())
# print(var.title())

# print("What is the capital of Nigeria a.) Ikeja b.) Abuja")
# ans = input("Ans: ").strip()
# if ans.lower() == 'b' or ans.capitalize() == 'Abuja':
#     print("correct")
# else:
#     print('wrong')

# print(var.strip())
# print(var.strip(')*#$'))

# print(var.split(','))

# task
# build a word counter

# essay = input("Essay: ").strip()
# no_of_words = len(essay.split())
# print("Words:",no_of_words)

# li = ['Mango', 'is', 'a', 'kind', 'of', 'Fruit.']
# print(" + ".join(li))

# print(var.startswith('Mango'))
# print(var.endswith('Mango'))

# print(var.find('isss'))

# build an email validator using .find()

# special character 
# \n => nextline
# \r => return
# \b => backspace
# \t => tab
# \ => escape character
# r => raw string  
# print(r"Hello\tWorld")


# Python Collections/Array
# 1. list - [] or list()
# - ordered, mutable/changeable, indexed, allows duplicate
cars = ['Audi', 'BMW', 'Toyota', 'Benz', 'Benz', 'Range Rover']
# print(cars[-2])
# print(cars[0:4])
# print(cars[0][1])
# print(cars[2][-1])

# cars[0] = 'Ferrari'
# print(cars)

# cars.append('Ferrari')
# cars.insert(0, 'Ferrari')
new_cars = ['Ferrari', 'Lambo']
# cars.extend('Ferrari')
# cars.append(new_cars)

# cars.pop(2)
# cars.clear()
# cars.remove('Toyotas')
# print(cars)

# print(cars.index('Toyota'))

# store = []

# while True:
#     print("""
#         1. Add an Item
#         2. Remove an Item 
#         #. Exit
#     """)
#     choice = input("Choice: ") 
#     if choice == '1':
#         item = input("Item: ").strip().title()
#         store.append(item)
#         print(store)
#     elif choice == '2':
#         print(store)
#         # ind = int(input("Index: "))
#         # store.pop(ind)
        
#         item = input('Item: ').strip().title()
#         if item in store:
#             confirm = input("Proceed (yes/no): ").strip().lower()
#             if confirm == 'yes':
#                 store.remove(item)
#                 print(f"{item} removed from store.")
#             else: 
#                 print("Operation terminated")
#         else: 
#             print(f"{item} is not in the store")
    
#     elif choice == '#': 
#         print('Bye..')
#         exit()
    
#     else:
#         print("Invalid Option")



# 2. tuple () or tuple()
# - ordered, indexed, allows duplicate but it is immutable/unchangeable
cars = ('Audi', 'BMW', 'Toyota', 'Benz', 'Ferrari')
# print(cars[0: 4])
# cars = list(cars)
# cars[0] = "Ferrari"
# print(cars)

# Unpacking
# a, b, c = cars
# *a, b, c = cars
# a, b, *c = cars

# print(b)
# print(cars.index('BMW'))

scores = [23, 45, 22, 50]
# print(sum(scores))
# print(min(scores))
# print(max(scores))

# print(sum(scores)/len(scores))

# items = ['Fufu', 'Efo', 'Eja panla']
# prices = [500, 400, 1500]
# print(zip(items, prices))
# for x in zip(items, prices):
#     print(x)

# for item, price in zip(items, prices):
#     # print(price)
#     print(f"{item} cost #{price}")


# items_prices = [('Fufu', 500),('Efo', 400),('Eja panla', 1500)]
# for item, price in items_prices:
#     print(price)


# exams = [
#     ('1. What is the capital of Nigeria a. Abuja b. Tokyo', 'a'),
#     ('2. What is the capital of Japan a. Abuja b. Tokyo', 'b')
# ]

# score = 0
# for ques, ans in exams:
#     print(ques)
#     user_ans = input('Answer: ').strip().lower()
#     if user_ans == ans:
#         print('Correct')
#         score +=5
#     else:
#         print('Wrong')

# print(f"Score: {score}")


# 3. set {} or set()
# - unordered, unindexed, immutable/unchangeable, doesn't allow duplicate
cars = {'Audi', 'BMW', 'Toyota', 'Benz', 'Ferrari', 'Benz'}
# cars.add('Range rover')
# cars.update(["Range rover", 'Ford'])
# cars.pop()
# cars.remove('Audia')
# cars.discard('Audia')
# print(cars)

setA = {1, 3, 5, 6, 2, 7, 9, 8}
setB = {2, 3, 4, 10,}

# print(setA.union(setB))

# print(setA.intersection(setB))
# print(setA.difference(setB))
# print(setA - setB)

# 4. dictionary - {key:value, key:value}
car = {
    "brand": "Lexus",
    "model": "Rx 350",
    "color": "White",
    "transmission": "Automatic",
    "iSBrandNew": False,
    # "owner": {
    #     "fullname": "John Doe",
    #     "gender": "Male",
    #     "address": {
    #         "state": "Texas",
    #         "country": "US"
    #     }
    # }
}

# print(car['brands'])
# car['model'] = "Lx 350"
# car['iSBrandNew'] = True
# car['engineType'] = "v6"
# print(car)

# print(car['owner']['address']['country'])



# print(car.keys())

# for key in car.keys():
#     print(key)

# print(car.values())

# for val in car.values():
#     print(val)

# print(car.items())

# for key, val in car.items():
#     print(key, val)


# exams = {
#     '1. What is the capital of Nigeria a. Abuja b. Tokyo': 'a',
#     '2. What is the capital of Japan a. Abuja b. Tokyo': 'b'
# }

# for ques, ans in exams.items():
#     print(ques)
#     user_ans = input("Ans: ")
#     if user_ans == ans:
#         print("correct")
#     else:
#         print("wrong")

# print(car.get('brands', 'Not found'))
# car.update({"brand": "Toyota"})

# car.pop('brand')
# car.popitem()
# print(car)


# task: create a simple register and login function using dict as your db structure

# db = {
#     "ade@gmail.com": ("ade ojo", "ade@gmail.com", "1234"),
#     "ife@gmail.com": ("ade ife", "ife@gmail.com", "12345"),
# }
# db['ade@gmail.com'][2]
# print("ife@gmail.com" not in db)

# db = {}
# while True:
#     print("""
#         1. Sign up 
#         2. Sign in
#         #. Exit
#     """)
#     option = input("Option: ")
#     if option == "1":
#         print("Sign up")
#         fullname = input("Fullname: ").strip().title()
#         email = input("Email: ").strip().lower()
#         password = input("Password: ")
        
#         if email in db:
#             print("Email already exist")
#             continue
        
#         db.update({email:(fullname, email, password)})
#         # db[email] = (fullname, email, password)
#         print("registration successfull")
        
#     elif option == "2":
#         print("Sign in")
#         email = input("Email: ").strip().lower()
#         password = input("Password: ")
#         if email in db and password == db[email][2]:
#             print("Login in successful")
            
#         else:
#             print("Invalid email or password")

#     elif option == "#":
#         exit()
    
#     else:
#         print("Invalid option")




# classwork : create a simple register and login function using;
db = [
    {
        "fullname": "Ade ojo",
        "email": "ade@gmail.com",
        "password": "1234"    
    },
    {
        "fullname": "ola ojo",
        "email": "ola@gmail.com",
        "password": "1234"
    }
]

# db = []



# Python Loop 
# 1. For Loop : It iterate over a sequence(e.g String, list e.t.c)
# cars = ['Audi', 'BMW', 'Toyota', 'Benz']
# for item in cars:
#     print(f"The {item} is one of my cars")
#     print('--------')

# for x in range(1, 7):
#     print(x, 'Times Table')
    
#     for y in range(1, 13):
#         print(f"{x} x {y} = {x*y}")


# 2. While Loop : It works based on a condition

# x = 10
# while x > 0:
#     print(x)
#     x -= 1
    
# plates = 10 
# while plates > 0:
#     user = input("Do you want to eat (yes/no): ").strip().lower()
#     if user == 'no':
#         print('skipping')
#         continue
    
#     plates -= 1
#     print(f'Take your food, it remains {plates} plates of food')
    
#     if plates == 2:
#         break
    
# else:
#     print("Food has finished!")


# Assignment - Build a simple Todo application. add todo, delete todo, clear all, view todo, and edit 


