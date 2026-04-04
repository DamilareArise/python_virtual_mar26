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
    
print(bin(10))   # 1   0   1   0

print(bin(5))    #     1   0   1

print(bin(2))    #         1   0

# print(10 & 5) # 0

# print(10 | 5) # 1    1    1   1

# print(10 | 2)   # 1    0    1   0

# print(10 ^ 2)   # 1    0    0   0



# build simple calculator