import sqlite3

# Connect to SQLite
connection = sqlite3.connect("employee_data.db")

# Create a cursor object to insert record and create table
cursor = connection.cursor()

# Create the tables
table_info_employees = """
CREATE TABLE IF NOT EXISTS Employees (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(25),
    Department VARCHAR(25),
    Salary INTEGER,
    Hire_Date DATE
);
"""
table_info_departments = """
CREATE TABLE IF NOT EXISTS Departments (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(25),
    Manager VARCHAR(25)
);
"""
cursor.execute(table_info_employees)
cursor.execute(table_info_departments)

# Insert records into Employees table
cursor.execute('''Insert Into Employees values(1,'Alice','Sales',50000,'2021-01-15')''')
cursor.execute('''Insert Into Employees values(2,'Bob','Engineering',70000,'2020-06-10')''')
cursor.execute('''Insert Into Employees values(3,'Charlie','Marketing',60000,'2022-03-20')''')
cursor.execute('''Insert Into Employees values(4,'Vikash','Sales',40000,'2023-06-30')''')
cursor.execute('''Insert Into Employees values(5,'Dipesh','Engineering',80000,'2020-09-15')''')
cursor.execute('''Insert Into Employees values(6,'Eva','Sales',55000,'2022-07-01')''')
cursor.execute('''Insert Into Employees values(7,'David','Engineering',75000,'2021-12-05')''')
cursor.execute('''Insert Into Employees values(8,'Grace','Marketing',65000,'2021-04-18')''')
cursor.execute('''Insert Into Employees values(9,'Hannah','Sales',48000,'2023-09-02')''')
cursor.execute('''Insert Into Employees values(10,'Isaac','Engineering',82000,'2022-11-25')''')
cursor.execute('''Insert Into Employees values(11,'Jack','Sales',53000,'2022-02-14')''')
cursor.execute('''Insert Into Employees values(12,'Kira','Engineering',77000,'2021-08-22')''')
cursor.execute('''Insert Into Employees values(13,'Liam','Marketing',69000,'2023-01-10')''')
cursor.execute('''Insert Into Employees values(14,'Megan','Sales',51000,'2023-05-09')''')
cursor.execute('''Insert Into Employees values(15,'Nina','Engineering',73000,'2020-11-12')''')

# Insert records into Departments table (use existing employee names as manager)
cursor.execute('''Insert Into Departments values(1,'Sales','Alice')''')
cursor.execute('''Insert Into Departments values(2,'Engineering','Bob')''')
cursor.execute('''Insert Into Departments values(3,'Marketing','Charlie')''')

# Display all the records
print("The inserted records are")

# Query and print Employees table (reset cursor before querying again)
cursor.execute('''Select * from Employees;''')
data_employees = cursor.fetchall()

cursor.execute('''Select * from Departments;''')
data_departments = cursor.fetchall()

print('Employees Table:')
for row in data_employees:
    print(row)

print('Departments Table:')
for row_ in data_departments:
    print(row_)

# Commit changes to the database
connection.commit()
connection.close()
