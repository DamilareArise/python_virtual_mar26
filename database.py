# Database: Is a place where data can be stored, retrieved and managed
# Database management system (DBMS)
# 1. Relational DBMS (SQL - Structured Query Language)
# i.Its basically work with structured data (tabular form)
# ii. It also create relationships between the tables using the keys
# iii. e.g MySQL, ORACLE, SQLLITE, MSSQL, MARIADB, POSTGRESQL
'''
user_table
id(pk)      fullname    email
1           Ade Ola     ade@gmail.com
2           Ife Ade     ife@gmail.com

transaction_table
id(pk)      amount      type        user_id(fk) 
1           1000        debit       1
'''

# Categories of Queries
# 1. DDL - Data Definition Language e.g CREATE, ALTER, DROP, TRUNCATE 
# 2. DML - Data Manipulation Language e.g INSERT, UPDATE, DELETE
# 3. DQL - Data Query Language e.g SELECT



# 2. Non Relational DBMS (NoSQL)
# i. It works semi-structured or non-structured data 
# ii. e.g Mongodb, google firebase, redis


import mysql.connector as sql
from pwinput import pwinput


conn = sql.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    port="3306",
    database="mar2026"
)
conn.autocommit = True
mycursor = conn.cursor()

# DDL

# mycursor.execute("DROP DATABASE mar2026")
# mycursor.execute("CREATE DATABASE mar2026")
# mycursor.execute("SHOW DATABASES")
# print(mycursor.fetchall())


# mycursor.execute("""
#     CREATE TABLE user_table(
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         fullname VARCHAR(50),
#         email VARCHAR(50) UNIQUE,
#         password VARCHAR(50),
#         created_at DATETIME DEFAULT CURRENT_TIMESTAMP
#     )      
# """)

# mycursor.execute("ALTER TABLE user_table ADD location VARCHAR(50) AFTER email")

# mycursor.execute("ALTER TABLE user_table CHANGE COLUMN location address VARCHAR(50)")

# mycursor.execute("ALTER TABLE user_table DROP COLUMN address")



# DML

def register():
    print("="*10)
    print("Sign up")
    print("="*10)
    
    fullname = input("Fullname: ").strip().title()
    email = input("email: ").strip().lower()
    address = input("address: ").strip()
    password = pwinput()
    
    query = "INSERT INTO user_table(fullname, email, address, password) VALUES(%s, %s, %s, %s)"
    # values = ('John Smith', "john@gmail.com", 'Lagos', '1234')
    values = (fullname, email, address, password)
    mycursor.execute(query, values)
    # conn.commit()
    print("Registration successfull")
    
# register()


# query = "UPDATE user_table SET password=%s WHERE email=%s"
# values = ('12345', 'ade@gmail.com')
# mycursor.execute(query, values)

# query = "DELETE FROM user_table WHERE id=%s"
# value = (2,)
# mycursor.execute(query, value)


# DQL 
# mycursor.execute("SELECT fullname, email, address FROM user_table")
# details = mycursor.fetchall()
# print(details)


# mycursor.execute("SELECT * FROM user_table WHERE id=3")
# details = mycursor.fetchone()
# print(details)


def login():
    email = input("email: ").strip().lower()
    password = pwinput()
    
    query = "SELECT * FROM user_table WHERE email=%s AND password=%s"
    values=(email, password)
    mycursor.execute(query, values)
    details = mycursor.fetchone()
    
    if details:
        print(f"Welcome back {details[1]}")
        
    else:
        print("Invalid email or password")
        
# login()