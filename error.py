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
# try:
#     print(arr[1])
#     # print(arr / 2)
# except NameError as n:
#     print('Error occured:', n)
# except IndexError as i:
#     print('Error occured:', i)
# except Exception as e:
#     print('Error occured:', e)
    
# else: 
#     # it works if there is no 
#     print("No error")

# finally:
#     # it works if theres error or not
#     print("Finally")


balance = 0
def deposit():
    global balance
    try:
        amount = float(input("Amount: "))
        balance += amount
    except Exception as e:
        print("Error:", e)
        
    else:
        print("Transaction Successful")
    
    finally:
        print("Back home")

deposit()