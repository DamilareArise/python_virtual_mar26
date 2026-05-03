# oop + sql
# bank application
# account table - id, fullname, email, password, account_no, balance, created_at

# ALTER TABLE user_table ADD COLUMN account_no VARCHAR(10) UNIQUE;
# ALTER TABLE user_table ADD COLUMN balance FLOAT(10, 2) DEFAULT 0.00;

import mysql.connector as sql
from random import randint
from pwinput import pwinput


class Config:
    __conn = None
    
    def __init__(self):
        self.__conn = sql.connect(
            host="127.0.0.1",
            user="root",
            password="password",
            port="3306",
            database="mar2026"
        )
        self.__conn.autocommit = True
        self.mycursor = self.__conn.cursor()
        
    
    def register(self, fullname, email, password):
        if fullname =="" or email == "" or password == "":
            return "All fields are required. Try again"
        
        account_no = randint(2000000000, 2099999999)
        query = "INSERT INTO user_table(fullname, email, password, account_no) VALUES(%s, %s, %s, %s)"
        values = (fullname, email, password, account_no)
        self.mycursor.execute(query, values)  
        return "Registration successfull"
    
    def set_password(self):
        password1 = pwinput()
        password2 = pwinput(prompt="Confirm Password: ")
        if password1 != password2:
            print("\nPasswords does not match\n")
            return self.set_password()
        
        return password1
    

# obj = Config()   
# res = obj.register("Ade Ola","ade@gmail.com","1234")
# print(res)

class BankApp(Config):
    
    
    def menu(self):
        print("""
            
            1. Sign in
            2. Sign up
            3. Exit
        """)

        choice = input("Choice: ")
        if choice == "1":
            self.signin()
        elif choice == "2":
            self.signup()
        elif choice == "#":
            exit()
        else:
            print("Invalid Choice")
            self.menu()
    
    def signup(self):
        fullname = input("Fullname: ").strip().title()
        email = input("email: ").strip().lower()
        password = self.set_password()
        response = self.register(fullname, email, password)
        print(response)
        self.menu()


bk = BankApp()
bk.menu()