# 1. Runtime error
# 2. Compile type error
# try, except, else, finally

# x = 10
# try:
#     print(x)
# except:
#    print("Danger danger") 
   

arr = [1, 3, 5, 4]
# print(arr / 2)
try:
    print(arr[1])
    print(arr / 2)
except NameError as n:
    print('Error occured:', n)
except IndexError as i:
    print('Error occured:', i)
except Exception as e:
    print('Error occured:', e)




