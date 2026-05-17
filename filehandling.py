# r - read only
# w - write only
# a - append
# x - create

# t - text mode
# b - byte mode

file = open(r"C:\python_virtual_mar26\bank.py", encoding="utf-8")
# print(file.read())
# print(file.readlines())
# print(file.readline())
# file.close()

# file = open("new.txt", mode="w")
# file = open("new.txt", mode="a")
# file.write("Welcome to File handling class\n")

# file = open("new.pdf", mode="x")

import os

# os.mkdir('new folder')
# os.rmdir('new folder')
# os.remove('new.txt')

# print(os.path.exists('new.pdf'))
# print(os.getcwd())

names = []
heights = []
with open("president_height.csv") as file:
    data = file.readlines()
    data.pop(0)
    # print(data)
    for each in data:
        # print(each.split(','))
        name = each.split(',')[1]
        height = each.split(',')[2]
        height = int(height.strip("\n"))
        names.append(name)
        heights.append(height)
        # print(height)
        
# print(names)
print(max(heights))

# who is/are the tallest president
# who is the shortest president
# what is the avarage height 
